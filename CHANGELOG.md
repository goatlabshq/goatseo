# Changelog

## [0.1.1](https://github.com/goatlabshq/goatseo/compare/v0.1.0...v0.1.1) (2026-10-23)


### Documentation

* clarify title_template, site_name and X-Robots-Tag precedence ([5eeb677](https://github.com/goatlabshq/goatseo/commit/5eeb677ba252966257d3cc3b42ba44963a218169))

## 0.1.0 (2026-10-19)


### Features

* add the goatseo facade distribution ([61561eb](https://github.com/goatlabshq/goatseo/commit/61561ebe9860db9f4288b0bfbcef9daf29e75b61))
* **core:** add metadata, precedence, URL safety and HTML rendering ([99d7134](https://github.com/goatlabshq/goatseo/commit/99d71345c11d2b0d92339fefb77a13407b2b663a))
* **django:** add the Django integration ([07d56e4](https://github.com/goatlabshq/goatseo/commit/07d56e46c78e6d1f98ccf381898449f538864806))
* **django:** report invalid GOATSEO_DEFAULTS in manage.py check ([694846c](https://github.com/goatlabshq/goatseo/commit/694846ceb01f4501a94e9c6f0cb336666a38e346))
* **django:** treat blank model fields as unset with model_metadata ([10baea0](https://github.com/goatlabshq/goatseo/commit/10baea024552a4b9909f7fba9451fd7b73e5748b))
* **fastapi:** add the FastAPI integration ([a133921](https://github.com/goatlabshq/goatseo/commit/a133921c5450b3cc463ed1057ebc9d9961ecf2c5))
* **flask:** add the Flask integration ([927e0b2](https://github.com/goatlabshq/goatseo/commit/927e0b27f5df3a1a6356dcf1b41b5cf59a42081f))
* **opengraph:** add typed Open Graph models and renderer ([956b0f4](https://github.com/goatlabshq/goatseo/commit/956b0f4b199c1b93036c36134f73d86c10f3305b))
* **schema-generator:** generate Schema.org models from the official ontology ([23f8a1e](https://github.com/goatlabshq/goatseo/commit/23f8a1e09dfe3d9c36fd21d2b34ea17e605531fb))
* **schema:** add generated Schema.org models and JSON-LD serialization ([ce931d4](https://github.com/goatlabshq/goatseo/commit/ce931d464bf86c29ec504641458dea1033ba6ae6))
* **seo:** add the framework-independent SEO builder ([c2fc106](https://github.com/goatlabshq/goatseo/commit/c2fc106a16319a64e9a7e694421fdce797e7d5f6))
* **twitter:** add typed Twitter/X Cards models and renderer ([3e773cf](https://github.com/goatlabshq/goatseo/commit/3e773cf3e360f5eecc3624e7b0de80ce6fe6bc64))


### Bug Fixes

* **ci:** claim every pending PyPI project before uploading ([5fa77e0](https://github.com/goatlabshq/goatseo/commit/5fa77e08cc8e40e5ca6ff0f5f3265ef3b2712fdb))
* **ci:** publish without attestations from the reusable release workflow ([b148265](https://github.com/goatlabshq/goatseo/commit/b14826505efc6125e744ca9fbd9d5bd131563b00))


### Documentation

* add README and documentation site ([9753eaf](https://github.com/goatlabshq/goatseo/commit/9753eafcd81a34f75672da21643dc1eba60bd58b))
* generate llms.txt and llms-full.txt with mkdocs-llmstxt ([899ea82](https://github.com/goatlabshq/goatseo/commit/899ea82a02afd6bf80b3262fb4e875b2b213243e))
* guard blank model fields in the Django metadata example ([53922cd](https://github.com/goatlabshq/goatseo/commit/53922cd6a11a886bb51d787e82e28b721ed3ea4a))
* install framework adapters through the goatseo extras ([37d34bb](https://github.com/goatlabshq/goatseo/commit/37d34bb8daa059025ecb020356c8314f1c42b662))
* point documentation links to GitHub Pages ([d0b538a](https://github.com/goatlabshq/goatseo/commit/d0b538a7d2c5a096e0e579c09a58f16f4ea1e624))
* point project links to the goatlabshq organization ([dde3a30](https://github.com/goatlabshq/goatseo/commit/dde3a30f88f42cfd5b8324f49f29bfe3158027ee))
* state that the robots header follows every templated response ([22a92f0](https://github.com/goatlabshq/goatseo/commit/22a92f0c8654f13420ec91dca5e6949feb4f743d))
