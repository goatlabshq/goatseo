from dataclasses import dataclass

from goatseo.core import Metadata, MetadataStack, Precedence, Robots, SupportsMetadata


def test_most_specific_layer_wins_regardless_of_insertion_order() -> None:
    stack = MetadataStack()
    for precedence in reversed(Precedence):
        stack.set(precedence, Metadata(title=precedence.name, author=precedence.name))
    stack.set(Precedence.GLOBAL, Metadata(description="global"))
    resolved = stack.resolve()
    assert resolved.title == "REQUEST"
    assert resolved.description == "global"


def test_each_level_overrides_the_previous_ones() -> None:
    levels = list(Precedence)
    assert levels == sorted(levels)
    for index, level in enumerate(levels):
        stack = MetadataStack({lower: Metadata(title=lower.name) for lower in levels[: index + 1]})
        assert stack.resolve().title == level.name


def test_update_merges_into_existing_layer() -> None:
    stack = MetadataStack()
    stack.set(Precedence.VIEW, Metadata(title="View", description="Kept"))
    stack.update(Precedence.VIEW, Metadata(title="Updated"))
    layer = stack.layer(Precedence.VIEW)
    assert layer == Metadata(title="Updated", description="Kept")
    assert stack.layer(Precedence.MODEL) is None


def test_set_replaces_layer_and_invalidates_cache() -> None:
    stack = MetadataStack().set(Precedence.SITE, Metadata(title="One"))
    assert stack.resolve().title == "One"
    stack.set(Precedence.SITE, Metadata(description="Two"))
    assert stack.resolve() == Metadata(description="Two")


def test_resolve_is_cached() -> None:
    stack = MetadataStack({Precedence.SITE: Metadata(title="x")})
    assert stack.resolve() is stack.resolve()


def test_robots_merge_across_layers() -> None:
    stack = MetadataStack(
        {
            Precedence.SITE: Metadata(robots=Robots(index=True, follow=True)),
            Precedence.REQUEST: Metadata(robots=Robots(index=False)),
        }
    )
    assert stack.resolve().robots == Robots(index=False, follow=True)


def test_copy_is_independent() -> None:
    stack = MetadataStack({Precedence.SITE: Metadata(title="Site")})
    clone = stack.copy()
    clone.set(Precedence.REQUEST, Metadata(title="Page"))
    assert stack.resolve().title == "Site"
    assert clone.resolve().title == "Page"


@dataclass
class _Article:
    title: str

    def seo_metadata(self) -> Metadata:
        return Metadata(title=self.title)


def test_supports_metadata_protocol_is_runtime_checkable() -> None:
    assert isinstance(_Article("x"), SupportsMetadata)
    assert not isinstance(object(), SupportsMetadata)
