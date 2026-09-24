"""Schema.org types, generated from Schema.org 30.1.

Do not edit: run `uv run goatseo-schema generate` instead.
"""

import datetime as _dt
from typing import Annotated, ClassVar

from goatseo.schema._enumerations import (
    ActionStatusType,
    BoardingPolicyType,
    BodyMeasurementTypeEnumeration,
    BookFormatType,
    CarUsageType,
    CertificationStatusEnumeration,
    ContactPointOption,
    DayOfWeek,
    DeliveryMethod,
    DigitalDocumentPermissionType,
    DigitalPlatformEnumeration,
    DriveWheelConfigurationValue,
    DrugCostCategory,
    DrugPregnancyCategory,
    DrugPrescriptionStatus,
    EnergyStarEnergyEfficiencyEnumeration,
    EUEnergyEfficiencyEnumeration,
    EventAttendanceModeEnumeration,
    EventStatusType,
    FulfillmentTypeEnumeration,
    GameAvailabilityEnumeration,
    GamePlayMode,
    GameServerStatus,
    GenderType,
    GovernmentBenefitsType,
    HealthAspectEnumeration,
    IncentiveQualifiedExpenseType,
    IncentiveStatus,
    IncentiveType,
    InfectiousAgentClass,
    IPTCDigitalSourceEnumeration,
    ItemAvailability,
    ItemListOrderType,
    LegalForceStatus,
    LegalValueLevel,
    MapCategoryType,
    MeasurementMethodEnum,
    MediaManipulationRatingEnumeration,
    MedicalAudienceType,
    MedicalEvidenceLevel,
    MedicalImagingTechnique,
    MedicalObservationalStudyDesign,
    MedicalProcedureType,
    MedicalSpecialty,
    MedicalStudyStatus,
    MedicalTrialDesign,
    MedicineSystem,
    MerchantReturnEnumeration,
    MusicAlbumProductionType,
    MusicAlbumReleaseType,
    MusicReleaseFormatType,
    NLNonprofitType,
    OfferItemCondition,
    OrderStatus,
    PaymentMethodType,
    PaymentStatusType,
    PhysicalActivityCategory,
    PhysicalExam,
    PriceComponentTypeEnumeration,
    PriceTypeEnumeration,
    PurchaseType,
    RefundTypeEnumeration,
    ReservationStatusType,
    RestrictedDiet,
    ReturnFeesEnumeration,
    ReturnLabelSourceEnumeration,
    ReturnMethodEnumeration,
    RsvpResponseType,
    SizeSystemEnumeration,
    SteeringPositionValue,
    TierBenefitEnumeration,
    UKNonprofitType,
    USNonprofitType,
    WearableMeasurementTypeEnumeration,
    WearableSizeGroupEnumeration,
    WearableSizeSystemEnumeration,
)
from goatseo.schema.base import SchemaEnumeration, SchemaModel, prop

__all__ = [
    "NGO",
    "AMRadioChannel",
    "APIReference",
    "AboutPage",
    "AcceptAction",
    "Accommodation",
    "AccountingService",
    "AchieveAction",
    "Action",
    "ActionAccessSpecification",
    "ActivateAction",
    "AddAction",
    "AdministrativeArea",
    "AdultEntertainment",
    "AdvertiserContentArticle",
    "AggregateOffer",
    "AggregateRating",
    "AgreeAction",
    "Airline",
    "Airport",
    "AlignmentObject",
    "AllocateAction",
    "AmusementPark",
    "AnalysisNewsArticle",
    "AnatomicalStructure",
    "AnatomicalSystem",
    "AnimalShelter",
    "Answer",
    "Apartment",
    "ApartmentComplex",
    "AppendAction",
    "ApplyAction",
    "ApprovedIndication",
    "Aquarium",
    "ArchiveComponent",
    "ArchiveOrganization",
    "ArriveAction",
    "ArtGallery",
    "Artery",
    "Article",
    "AskAction",
    "AskPublicNewsArticle",
    "AssessAction",
    "AssignAction",
    "Atlas",
    "Attorney",
    "Audience",
    "AudioObject",
    "AudioObjectSnapshot",
    "Audiobook",
    "AuthorizeAction",
    "AutoBodyShop",
    "AutoDealer",
    "AutoPartsStore",
    "AutoRental",
    "AutoRepair",
    "AutoWash",
    "AutomatedTeller",
    "AutomotiveBusiness",
    "BackgroundNewsArticle",
    "Bakery",
    "BankAccount",
    "BankOrCreditUnion",
    "BarOrPub",
    "Barcode",
    "Beach",
    "BeautySalon",
    "BedAndBreakfast",
    "BedDetails",
    "BedType",
    "BefriendAction",
    "BikeStore",
    "Blog",
    "BlogPosting",
    "BloodTest",
    "BoatReservation",
    "BoatTerminal",
    "BoatTrip",
    "BodyOfWater",
    "Bone",
    "Book",
    "BookSeries",
    "BookStore",
    "BookmarkAction",
    "BorrowAction",
    "BowlingAlley",
    "BrainStructure",
    "Brand",
    "BreadcrumbList",
    "Brewery",
    "Bridge",
    "BroadcastChannel",
    "BroadcastEvent",
    "BroadcastFrequencySpecification",
    "BroadcastService",
    "BrokerageAccount",
    "BuddhistTemple",
    "BusOrCoach",
    "BusReservation",
    "BusStation",
    "BusStop",
    "BusTrip",
    "BusinessAudience",
    "BusinessEntityType",
    "BusinessEvent",
    "BusinessFunction",
    "BuyAction",
    "CDCPMDRecord",
    "CableOrSatelliteService",
    "CafeOrCoffeeShop",
    "Campground",
    "CampingPitch",
    "Canal",
    "CancelAction",
    "Car",
    "Casino",
    "CategoryCode",
    "CategoryCodeSet",
    "CatholicChurch",
    "Cemetery",
    "Certification",
    "Chapter",
    "CheckAction",
    "CheckInAction",
    "CheckOutAction",
    "CheckoutPage",
    "ChildCare",
    "ChildrensEvent",
    "ChooseAction",
    "Church",
    "City",
    "CityHall",
    "CivicStructure",
    "Claim",
    "ClaimReview",
    "Clip",
    "ClothingStore",
    "Code",
    "Collection",
    "CollectionPage",
    "CollegeOrUniversity",
    "ComedyClub",
    "ComedyEvent",
    "ComicCoverArt",
    "ComicIssue",
    "ComicSeries",
    "ComicStory",
    "Comment",
    "CommentAction",
    "CommunicateAction",
    "CompleteDataFeed",
    "CompoundPriceSpecification",
    "ComputerLanguage",
    "ComputerStore",
    "ConfirmAction",
    "Consortium",
    "ConstraintNode",
    "ConsumeAction",
    "ContactPage",
    "ContactPoint",
    "Continent",
    "ControlAction",
    "ConvenienceStore",
    "Conversation",
    "CookAction",
    "Cooperative",
    "Corporation",
    "CorrectionComment",
    "Country",
    "Course",
    "CourseInstance",
    "Courthouse",
    "CoverArt",
    "CovidTestingFacility",
    "CreateAction",
    "CreativeWork",
    "CreativeWorkSeason",
    "CreativeWorkSeries",
    "CreditCard",
    "Crematorium",
    "CriticReview",
    "CurrencyConversionService",
    "DDxElement",
    "DanceEvent",
    "DanceGroup",
    "DataCatalog",
    "DataDownload",
    "DataFeed",
    "DataFeedItem",
    "Dataset",
    "DatedMoneySpecification",
    "DaySpa",
    "DeactivateAction",
    "DefenceEstablishment",
    "DefinedRegion",
    "DefinedTerm",
    "DefinedTermSet",
    "DeleteAction",
    "DeliveryChargeSpecification",
    "DeliveryEvent",
    "DeliveryTimeSettings",
    "Demand",
    "Dentist",
    "DepartAction",
    "DepartmentStore",
    "DepositAccount",
    "DiagnosticLab",
    "DiagnosticProcedure",
    "Diet",
    "DietarySupplement",
    "DigitalDocument",
    "DigitalDocumentPermission",
    "DisagreeAction",
    "DiscoverAction",
    "DiscussionForumPosting",
    "DislikeAction",
    "Distillery",
    "DonateAction",
    "DoseSchedule",
    "DownloadAction",
    "DrawAction",
    "Drawing",
    "DrinkAction",
    "Drug",
    "DrugClass",
    "DrugCost",
    "DrugLegalStatus",
    "DrugStrength",
    "DryCleaningOrLaundry",
    "EatAction",
    "EducationEvent",
    "EducationalAudience",
    "EducationalOccupationalProgram",
    "EducationalOrganization",
    "Electrician",
    "ElectronicsStore",
    "ElementarySchool",
    "EmailMessage",
    "Embassy",
    "EmergencyService",
    "EmployeeRole",
    "EmployerAggregateRating",
    "EmploymentAgency",
    "EndorseAction",
    "EndorsementRating",
    "EnergyConsumptionDetails",
    "EnergyEfficiencyEnumeration",
    "EngineSpecification",
    "EntertainmentBusiness",
    "EntryPoint",
    "Enumeration",
    "Episode",
    "Event",
    "EventReservation",
    "EventSeries",
    "EventVenue",
    "ExchangeRateSpecification",
    "ExerciseAction",
    "ExerciseGym",
    "ExercisePlan",
    "ExhibitionEvent",
    "FAQPage",
    "FMRadioChannel",
    "FastFoodRestaurant",
    "Festival",
    "FilmAction",
    "FinancialIncentive",
    "FinancialProduct",
    "FinancialService",
    "FindAction",
    "FireStation",
    "Flight",
    "FlightReservation",
    "FloorPlan",
    "Florist",
    "FollowAction",
    "FoodEstablishment",
    "FoodEstablishmentReservation",
    "FoodEvent",
    "FoodService",
    "FundingAgency",
    "FundingScheme",
    "FurnitureStore",
    "Game",
    "GameServer",
    "GardenStore",
    "GasStation",
    "GatedResidenceCommunity",
    "GeneralContractor",
    "GeoCircle",
    "GeoCoordinates",
    "GeoShape",
    "GiveAction",
    "GolfCourse",
    "GovernmentBuilding",
    "GovernmentOffice",
    "GovernmentOrganization",
    "GovernmentPermit",
    "GovernmentService",
    "Grant",
    "GroceryStore",
    "Guide",
    "HVACBusiness",
    "Hackathon",
    "HairSalon",
    "HardwareStore",
    "HealthAndBeautyBusiness",
    "HealthClub",
    "HealthTopicContent",
    "HighSchool",
    "HinduTemple",
    "HobbyShop",
    "HomeAndConstructionBusiness",
    "HomeGoodsStore",
    "Hospital",
    "Hostel",
    "Hotel",
    "HotelRoom",
    "House",
    "HousePainter",
    "HowTo",
    "HowToDirection",
    "HowToItem",
    "HowToSection",
    "HowToStep",
    "HowToSupply",
    "HowToTip",
    "HowToTool",
    "IceCreamShop",
    "IgnoreAction",
    "ImageGallery",
    "ImageObject",
    "ImageObjectSnapshot",
    "ImagingTest",
    "IndividualPhysician",
    "IndividualProduct",
    "InfectiousDisease",
    "InformAction",
    "InsertAction",
    "InstallAction",
    "InsuranceAgency",
    "Intangible",
    "InteractAction",
    "InteractionCounter",
    "InternetCafe",
    "InvestmentFund",
    "InvestmentOrDeposit",
    "InviteAction",
    "Invoice",
    "ItemList",
    "ItemPage",
    "JewelryStore",
    "JobPosting",
    "JoinAction",
    "Joint",
    "LakeBodyOfWater",
    "Landform",
    "LandmarksOrHistoricalBuildings",
    "Language",
    "LeaveAction",
    "LegalService",
    "Legislation",
    "LegislationObject",
    "LegislativeBuilding",
    "LendAction",
    "Library",
    "LibrarySystem",
    "LifestyleModification",
    "Ligament",
    "LikeAction",
    "LinkRole",
    "LiquorStore",
    "ListItem",
    "ListenAction",
    "LiteraryEvent",
    "LiveBlogPosting",
    "LoanOrCredit",
    "LocalBusiness",
    "LocationFeatureSpecification",
    "Locksmith",
    "LodgingBusiness",
    "LodgingReservation",
    "LoseAction",
    "LymphaticVessel",
    "Manuscript",
    "Map",
    "MarryAction",
    "MaximumDoseSchedule",
    "MeasurementTypeEnumeration",
    "MediaEnumeration",
    "MediaGallery",
    "MediaObject",
    "MediaReview",
    "MediaReviewItem",
    "MediaSubscription",
    "MedicalAudience",
    "MedicalBusiness",
    "MedicalCause",
    "MedicalClinic",
    "MedicalCode",
    "MedicalCondition",
    "MedicalConditionStage",
    "MedicalContraindication",
    "MedicalDevice",
    "MedicalEntity",
    "MedicalEnumeration",
    "MedicalGuideline",
    "MedicalGuidelineContraindication",
    "MedicalGuidelineRecommendation",
    "MedicalIndication",
    "MedicalIntangible",
    "MedicalObservationalStudy",
    "MedicalOrganization",
    "MedicalProcedure",
    "MedicalRiskCalculator",
    "MedicalRiskEstimator",
    "MedicalRiskFactor",
    "MedicalRiskScore",
    "MedicalScholarlyArticle",
    "MedicalSign",
    "MedicalSignOrSymptom",
    "MedicalStudy",
    "MedicalSymptom",
    "MedicalTest",
    "MedicalTestPanel",
    "MedicalTherapy",
    "MedicalTrial",
    "MedicalWebPage",
    "MeetingRoom",
    "MemberProgram",
    "MemberProgramTier",
    "MensClothingStore",
    "Menu",
    "MenuItem",
    "MenuSection",
    "MerchantReturnPolicy",
    "MerchantReturnPolicySeasonalOverride",
    "Message",
    "MiddleSchool",
    "MobileApplication",
    "MobilePhoneStore",
    "Model3D",
    "MonetaryAmount",
    "MonetaryAmountDistribution",
    "MonetaryGrant",
    "MoneyTransfer",
    "MortgageLoan",
    "Mosque",
    "Motel",
    "Motorcycle",
    "MotorcycleDealer",
    "MotorcycleRepair",
    "MotorizedBicycle",
    "Mountain",
    "MoveAction",
    "Movie",
    "MovieClip",
    "MovieRentalStore",
    "MovieSeries",
    "MovieTheater",
    "MovingCompany",
    "Muscle",
    "Museum",
    "MusicAlbum",
    "MusicComposition",
    "MusicEvent",
    "MusicGroup",
    "MusicPlaylist",
    "MusicRecording",
    "MusicRelease",
    "MusicStore",
    "MusicVenue",
    "MusicVideoObject",
    "NailSalon",
    "Nerve",
    "NewsArticle",
    "NewsMediaOrganization",
    "Newspaper",
    "NightClub",
    "NonprofitType",
    "Notary",
    "NoteDigitalDocument",
    "NutritionInformation",
    "Observation",
    "Occupation",
    "OccupationalTherapy",
    "OceanBodyOfWater",
    "Offer",
    "OfferCatalog",
    "OfferShippingDetails",
    "OfficeEquipmentStore",
    "OnDemandEvent",
    "OnlineBusiness",
    "OnlineMarketplace",
    "OnlineStore",
    "OpeningHoursSpecification",
    "OpinionNewsArticle",
    "Optician",
    "Order",
    "OrderAction",
    "OrderItem",
    "Organization",
    "OrganizationRole",
    "OrganizeAction",
    "OutletStore",
    "OwnershipInfo",
    "PaintAction",
    "Painting",
    "PalliativeProcedure",
    "ParcelDelivery",
    "ParentAudience",
    "Park",
    "ParkingFacility",
    "PathologyTest",
    "Patient",
    "PawnShop",
    "PayAction",
    "PaymentCard",
    "PaymentChargeSpecification",
    "PaymentMethod",
    "PaymentService",
    "PeopleAudience",
    "PerformAction",
    "PerformanceRole",
    "PerformingArtsTheater",
    "PerformingGroup",
    "Periodical",
    "Permit",
    "Person",
    "PetStore",
    "Pharmacy",
    "Photograph",
    "PhotographAction",
    "PhysicalActivity",
    "PhysicalTherapy",
    "Physician",
    "PhysiciansOffice",
    "Place",
    "PlaceOfWorship",
    "PlanAction",
    "Play",
    "PlayAction",
    "PlayGameAction",
    "Playground",
    "Plumber",
    "PoliceStation",
    "PoliticalParty",
    "Pond",
    "PostOffice",
    "PostalAddress",
    "PostalCodeRangeSpecification",
    "Poster",
    "PreOrderAction",
    "PrependAction",
    "Preschool",
    "PresentationDigitalDocument",
    "PreventionIndication",
    "PriceSpecification",
    "Product",
    "ProductGroup",
    "ProductModel",
    "ProductReturnPolicy",
    "ProfessionalService",
    "ProfilePage",
    "ProgramMembership",
    "Project",
    "PropertyValue",
    "PropertyValueSpecification",
    "PsychologicalTreatment",
    "PublicSwimmingPool",
    "PublicToilet",
    "PublicationEvent",
    "PublicationIssue",
    "PublicationVolume",
    "QAPage",
    "QualitativeValue",
    "QuantitativeValue",
    "QuantitativeValueDistribution",
    "Question",
    "QuoteAction",
    "RVPark",
    "RadiationTherapy",
    "RadioBroadcastService",
    "RadioChannel",
    "RadioClip",
    "RadioEpisode",
    "RadioSeason",
    "RadioSeries",
    "RadioStation",
    "Rating",
    "ReactAction",
    "ReadAction",
    "RealEstateAgent",
    "ReceiveAction",
    "Recipe",
    "Recommendation",
    "RecommendedDoseSchedule",
    "RecyclingCenter",
    "RegisterAction",
    "RejectAction",
    "RentAction",
    "RentalCarReservation",
    "RepaymentSpecification",
    "ReplaceAction",
    "ReplyAction",
    "Report",
    "ReportageNewsArticle",
    "ReportedDoseSchedule",
    "ResearchProject",
    "Researcher",
    "Reservation",
    "ReservationPackage",
    "ReserveAction",
    "Reservoir",
    "Residence",
    "Resort",
    "Restaurant",
    "ResumeAction",
    "ReturnAction",
    "Review",
    "ReviewAction",
    "ReviewNewsArticle",
    "RiverBodyOfWater",
    "Role",
    "RoofingContractor",
    "Room",
    "RsvpAction",
    "SaleEvent",
    "SatiricalArticle",
    "Schedule",
    "ScheduleAction",
    "ScholarlyArticle",
    "School",
    "ScreeningEvent",
    "Sculpture",
    "SeaBodyOfWater",
    "SearchAction",
    "SearchResultsPage",
    "Season",
    "Seat",
    "SelfStorage",
    "SellAction",
    "SendAction",
    "SequentialArt",
    "Series",
    "Service",
    "ServiceChannel",
    "ServicePeriod",
    "ShareAction",
    "SheetMusic",
    "ShippingConditions",
    "ShippingDeliveryTime",
    "ShippingRateSettings",
    "ShippingService",
    "ShoeStore",
    "ShoppingCenter",
    "ShortStory",
    "SingleFamilyResidence",
    "SiteNavigationElement",
    "SizeGroupEnumeration",
    "SizeSpecification",
    "SkiResort",
    "SocialEvent",
    "SocialMediaPosting",
    "SoftwareApplication",
    "SoftwareSourceCode",
    "SomeProducts",
    "SpeakableSpecification",
    "SpecialAnnouncement",
    "Specialty",
    "SportingGoodsStore",
    "SportsActivityLocation",
    "SportsClub",
    "SportsEvent",
    "SportsOrganization",
    "SportsTeam",
    "SpreadsheetDigitalDocument",
    "StadiumOrArena",
    "State",
    "Statement",
    "StatisticalPopulation",
    "StatisticalVariable",
    "StatusEnumeration",
    "Store",
    "StructuredValue",
    "SubscribeAction",
    "Substance",
    "SubwayStation",
    "Suite",
    "SuperficialAnatomy",
    "SurgicalProcedure",
    "SuspendAction",
    "Syllabus",
    "Synagogue",
    "TVClip",
    "TVEpisode",
    "TVSeason",
    "TVSeries",
    "Table",
    "TakeAction",
    "TattooParlor",
    "Taxi",
    "TaxiReservation",
    "TaxiService",
    "TaxiStand",
    "TechArticle",
    "TelevisionChannel",
    "TelevisionStation",
    "TennisComplex",
    "TextDigitalDocument",
    "TextObject",
    "TheaterEvent",
    "TheaterGroup",
    "TherapeuticProcedure",
    "Thesis",
    "Thing",
    "Ticket",
    "TieAction",
    "TipAction",
    "TireShop",
    "TouristAttraction",
    "TouristInformationCenter",
    "ToyStore",
    "TrackAction",
    "TradeAction",
    "TrainReservation",
    "TrainStation",
    "TrainTrip",
    "TransferAction",
    "TravelAction",
    "TravelAgency",
    "TreatmentIndication",
    "Trip",
    "TypeAndQuantityNode",
    "UnRegisterAction",
    "UnitPriceSpecification",
    "UpdateAction",
    "UseAction",
    "UserBlocks",
    "UserCheckins",
    "UserComments",
    "UserDownloads",
    "UserInteraction",
    "UserLikes",
    "UserPageVisits",
    "UserPlays",
    "UserPlusOnes",
    "UserReview",
    "UserTweets",
    "VacationRental",
    "Vehicle",
    "Vein",
    "Vessel",
    "VeterinaryCare",
    "VideoGallery",
    "VideoGame",
    "VideoGameClip",
    "VideoGameSeries",
    "VideoObject",
    "VideoObjectSnapshot",
    "ViewAction",
    "VirtualLocation",
    "VisualArtsEvent",
    "VisualArtwork",
    "VitalSign",
    "Volcano",
    "VoteAction",
    "WPAdBlock",
    "WPFooter",
    "WPHeader",
    "WPSideBar",
    "WantAction",
    "WarrantyPromise",
    "WarrantyScope",
    "WatchAction",
    "Waterfall",
    "WearAction",
    "WebAPI",
    "WebApplication",
    "WebPage",
    "WebPageElement",
    "WebSite",
    "WholesaleStore",
    "WinAction",
    "Winery",
    "WorkBasedProgram",
    "WorkersUnion",
    "WriteAction",
    "Zoo",
]


class Thing(SchemaModel):
    """The most generic type of item.

    https://schema.org/Thing
    """

    jsonld_type: ClassVar[str] = "Thing"
    additional_type: Annotated[str | list[str] | None, prop("additionalType")] = None
    alternate_name: Annotated[str | list[str] | None, prop("alternateName")] = None
    description: Annotated[
        str | TextObject | list[str | TextObject] | None, prop("description")
    ] = None
    disambiguating_description: Annotated[
        str | list[str] | None, prop("disambiguatingDescription")
    ] = None
    identifier: Annotated[
        str | PropertyValue | list[str | PropertyValue] | None, prop("identifier")
    ] = None
    image: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("image")] = None
    main_entity_of_page: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("mainEntityOfPage")
    ] = None
    name: Annotated[str | list[str] | None, prop("name")] = None
    owner: Annotated[Organization | Person | list[Organization | Person] | None, prop("owner")] = (
        None
    )
    potential_action: Annotated[Action | list[Action] | None, prop("potentialAction")] = None
    same_as: Annotated[str | list[str] | None, prop("sameAs")] = None
    subject_of: Annotated[
        CreativeWork | Event | list[CreativeWork | Event] | None, prop("subjectOf")
    ] = None
    url: Annotated[str | list[str] | None, prop("url")] = None


class Action(Thing):
    """An action performed by a direct agent and indirect participants upon a direct object.

    https://schema.org/Action
    """

    jsonld_type: ClassVar[str] = "Action"
    action_process: Annotated[HowTo | list[HowTo] | None, prop("actionProcess")] = None
    action_status: Annotated[
        ActionStatusType | list[ActionStatusType] | None, prop("actionStatus")
    ] = None
    agent: Annotated[Organization | Person | list[Organization | Person] | None, prop("agent")] = (
        None
    )
    end_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("endTime")
    ] = None
    error: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("error")
    ] = None
    instrument: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("instrument")
    ] = None
    location: Annotated[
        str
        | Place
        | PostalAddress
        | VirtualLocation
        | list[str | Place | PostalAddress | VirtualLocation]
        | None,
        prop("location"),
    ] = None
    object: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("object")
    ] = None
    participant: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("participant")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    result: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("result")
    ] = None
    start_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("startTime")
    ] = None
    target: Annotated[str | EntryPoint | list[str | EntryPoint] | None, prop("target")] = None


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies, photographs, software programs, etc.

    https://schema.org/CreativeWork
    """

    jsonld_type: ClassVar[str] = "CreativeWork"
    about: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("about")
    ] = None
    abstract: Annotated[str | list[str] | None, prop("abstract")] = None
    access_mode: Annotated[str | list[str] | None, prop("accessMode")] = None
    access_mode_sufficient: Annotated[
        ItemList | list[ItemList] | None, prop("accessModeSufficient")
    ] = None
    accessibility_api: Annotated[str | list[str] | None, prop("accessibilityAPI")] = None
    accessibility_control: Annotated[str | list[str] | None, prop("accessibilityControl")] = None
    accessibility_feature: Annotated[str | list[str] | None, prop("accessibilityFeature")] = None
    accessibility_hazard: Annotated[str | list[str] | None, prop("accessibilityHazard")] = None
    accessibility_summary: Annotated[str | list[str] | None, prop("accessibilitySummary")] = None
    accountable_person: Annotated[Person | list[Person] | None, prop("accountablePerson")] = None
    acquire_license_page: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("acquireLicensePage")
    ] = None
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    alternative_headline: Annotated[str | list[str] | None, prop("alternativeHeadline")] = None
    archived_at: Annotated[str | WebPage | list[str | WebPage] | None, prop("archivedAt")] = None
    assesses: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("assesses")] = None
    associated_media: Annotated[MediaObject | list[MediaObject] | None, prop("associatedMedia")] = (
        None
    )
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    audio: Annotated[
        AudioObject | Clip | MusicRecording | list[AudioObject | Clip | MusicRecording] | None,
        prop("audio"),
    ] = None
    author: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("author")
    ] = None
    award: Annotated[str | list[str] | None, prop("award")] = None
    awards: Annotated[str | list[str] | None, prop("awards", superseded_by=("award",))] = None
    character: Annotated[Person | list[Person] | None, prop("character")] = None
    citation: Annotated[str | CreativeWork | list[str | CreativeWork] | None, prop("citation")] = (
        None
    )
    comment: Annotated[Comment | list[Comment] | None, prop("comment")] = None
    comment_count: Annotated[int | list[int] | None, prop("commentCount")] = None
    conditions_of_access: Annotated[str | list[str] | None, prop("conditionsOfAccess")] = None
    content_location: Annotated[Place | list[Place] | None, prop("contentLocation")] = None
    content_rating: Annotated[str | Rating | list[str | Rating] | None, prop("contentRating")] = (
        None
    )
    content_reference_time: Annotated[
        _dt.datetime | list[_dt.datetime] | None, prop("contentReferenceTime")
    ] = None
    contributor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("contributor")
    ] = None
    copyright_holder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("copyrightHolder")
    ] = None
    copyright_notice: Annotated[str | list[str] | None, prop("copyrightNotice")] = None
    copyright_year: Annotated[int | float | list[int | float] | None, prop("copyrightYear")] = None
    correction: Annotated[
        str | CorrectionComment | list[str | CorrectionComment] | None, prop("correction")
    ] = None
    country_of_origin: Annotated[Country | list[Country] | None, prop("countryOfOrigin")] = None
    creator: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("creator")
    ] = None
    credit_text: Annotated[str | list[str] | None, prop("creditText")] = None
    date_created: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateCreated")
    ] = None
    date_modified: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateModified")
    ] = None
    date_published: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("datePublished")
    ] = None
    digital_source_type: Annotated[
        IPTCDigitalSourceEnumeration | list[IPTCDigitalSourceEnumeration] | None,
        prop("digitalSourceType"),
    ] = None
    discussion_url: Annotated[str | list[str] | None, prop("discussionUrl")] = None
    edit_eidr: Annotated[str | list[str] | None, prop("editEIDR")] = None
    editor: Annotated[Person | list[Person] | None, prop("editor")] = None
    educational_alignment: Annotated[
        AlignmentObject | list[AlignmentObject] | None, prop("educationalAlignment")
    ] = None
    educational_use: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("educationalUse")
    ] = None
    encoding: Annotated[MediaObject | list[MediaObject] | None, prop("encoding")] = None
    encoding_format: Annotated[str | list[str] | None, prop("encodingFormat")] = None
    encodings: Annotated[
        MediaObject | list[MediaObject] | None, prop("encodings", superseded_by=("encoding",))
    ] = None
    example_of_work: Annotated[CreativeWork | list[CreativeWork] | None, prop("exampleOfWork")] = (
        None
    )
    expires: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("expires")
    ] = None
    file_format: Annotated[
        str | list[str] | None, prop("fileFormat", superseded_by=("encodingFormat",))
    ] = None
    funder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("funder")
    ] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    genre: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("genre")] = None
    has_part: Annotated[CreativeWork | list[CreativeWork] | None, prop("hasPart")] = None
    headline: Annotated[str | list[str] | None, prop("headline")] = None
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    interaction_statistic: Annotated[
        InteractionCounter | list[InteractionCounter] | None, prop("interactionStatistic")
    ] = None
    interactivity_type: Annotated[str | list[str] | None, prop("interactivityType")] = None
    interpreted_as_claim: Annotated[Claim | list[Claim] | None, prop("interpretedAsClaim")] = None
    is_accessible_for_free: Annotated[bool | list[bool] | None, prop("isAccessibleForFree")] = None
    is_based_on: Annotated[
        str | CreativeWork | Product | list[str | CreativeWork | Product] | None, prop("isBasedOn")
    ] = None
    is_based_on_url: Annotated[
        str | CreativeWork | Product | list[str | CreativeWork | Product] | None,
        prop("isBasedOnUrl", superseded_by=("isBasedOn",)),
    ] = None
    is_family_friendly: Annotated[bool | list[bool] | None, prop("isFamilyFriendly")] = None
    is_part_of: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("isPartOf")
    ] = None
    keywords: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("keywords")] = None
    learning_resource_type: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("learningResourceType")
    ] = None
    license: Annotated[str | CreativeWork | list[str | CreativeWork] | None, prop("license")] = None
    location_created: Annotated[Place | list[Place] | None, prop("locationCreated")] = None
    main_entity: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("mainEntity")
    ] = None
    maintainer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("maintainer")
    ] = None
    material: Annotated[str | Product | list[str | Product] | None, prop("material")] = None
    material_extent: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("materialExtent")
    ] = None
    mentions: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("mentions")
    ] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    pattern: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("pattern")] = None
    position: Annotated[str | int | list[str | int] | None, prop("position")] = None
    producer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("producer")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    publication: Annotated[
        PublicationEvent | list[PublicationEvent] | None, prop("publication")
    ] = None
    publisher: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("publisher")
    ] = None
    publisher_imprint: Annotated[
        Organization | list[Organization] | None, prop("publisherImprint")
    ] = None
    publishing_principles: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("publishingPrinciples")
    ] = None
    recorded_at: Annotated[Event | list[Event] | None, prop("recordedAt")] = None
    released_event: Annotated[
        PublicationEvent | list[PublicationEvent] | None, prop("releasedEvent")
    ] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    reviews: Annotated[Review | list[Review] | None, prop("reviews", superseded_by=("review",))] = (
        None
    )
    schema_version: Annotated[str | list[str] | None, prop("schemaVersion")] = None
    sd_date_published: Annotated[_dt.date | list[_dt.date] | None, prop("sdDatePublished")] = None
    sd_license: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("sdLicense")
    ] = None
    sd_publisher: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sdPublisher")
    ] = None
    size: Annotated[
        str
        | DefinedTerm
        | QuantitativeValue
        | SizeSpecification
        | list[str | DefinedTerm | QuantitativeValue | SizeSpecification]
        | None,
        prop("size"),
    ] = None
    source_organization: Annotated[
        Organization | list[Organization] | None, prop("sourceOrganization")
    ] = None
    spatial: Annotated[Place | list[Place] | None, prop("spatial")] = None
    spatial_coverage: Annotated[Place | list[Place] | None, prop("spatialCoverage")] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None
    teaches: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("teaches")] = None
    temporal: Annotated[str | _dt.datetime | list[str | _dt.datetime] | None, prop("temporal")] = (
        None
    )
    temporal_coverage: Annotated[
        str | _dt.datetime | list[str | _dt.datetime] | None, prop("temporalCoverage")
    ] = None
    text: Annotated[str | list[str] | None, prop("text")] = None
    thumbnail: Annotated[ImageObject | list[ImageObject] | None, prop("thumbnail")] = None
    thumbnail_url: Annotated[str | list[str] | None, prop("thumbnailUrl")] = None
    time_required: Annotated[str | list[str] | None, prop("timeRequired")] = None
    translation_of_work: Annotated[
        CreativeWork | list[CreativeWork] | None, prop("translationOfWork")
    ] = None
    translator: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("translator")
    ] = None
    typical_age_range: Annotated[str | list[str] | None, prop("typicalAgeRange")] = None
    usage_info: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("usageInfo")
    ] = None
    version: Annotated[str | int | float | list[str | int | float] | None, prop("version")] = None
    video: Annotated[Clip | VideoObject | list[Clip | VideoObject] | None, prop("video")] = None
    word_count: Annotated[int | list[int] | None, prop("wordCount")] = None
    work_example: Annotated[CreativeWork | list[CreativeWork] | None, prop("workExample")] = None
    work_translation: Annotated[
        CreativeWork | list[CreativeWork] | None, prop("workTranslation")
    ] = None


class Event(Thing):
    """An event happening at a certain time and location, such as a concert, lecture, or festival.

    https://schema.org/Event
    """

    jsonld_type: ClassVar[str] = "Event"
    about: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("about")
    ] = None
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    attendee: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("attendee")
    ] = None
    attendees: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("attendees", superseded_by=("attendee",)),
    ] = None
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    composer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("composer")
    ] = None
    contributor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("contributor")
    ] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    door_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("doorTime")
    ] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    event_attendance_mode: Annotated[
        EventAttendanceModeEnumeration | list[EventAttendanceModeEnumeration] | None,
        prop("eventAttendanceMode"),
    ] = None
    event_schedule: Annotated[Schedule | list[Schedule] | None, prop("eventSchedule")] = None
    event_status: Annotated[EventStatusType | list[EventStatusType] | None, prop("eventStatus")] = (
        None
    )
    funder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("funder")
    ] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    is_accessible_for_free: Annotated[bool | list[bool] | None, prop("isAccessibleForFree")] = None
    keywords: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("keywords")] = None
    location: Annotated[
        str
        | Place
        | PostalAddress
        | VirtualLocation
        | list[str | Place | PostalAddress | VirtualLocation]
        | None,
        prop("location"),
    ] = None
    maximum_attendee_capacity: Annotated[
        int | list[int] | None, prop("maximumAttendeeCapacity")
    ] = None
    maximum_physical_attendee_capacity: Annotated[
        int | list[int] | None, prop("maximumPhysicalAttendeeCapacity")
    ] = None
    maximum_virtual_attendee_capacity: Annotated[
        int | list[int] | None, prop("maximumVirtualAttendeeCapacity")
    ] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    organizer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("organizer")
    ] = None
    performer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("performer")
    ] = None
    performers: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("performers", superseded_by=("performer",)),
    ] = None
    previous_start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("previousStartDate")
    ] = None
    recorded_in: Annotated[CreativeWork | list[CreativeWork] | None, prop("recordedIn")] = None
    remaining_attendee_capacity: Annotated[
        int | list[int] | None, prop("remainingAttendeeCapacity")
    ] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None
    sub_event: Annotated[Event | list[Event] | None, prop("subEvent")] = None
    sub_events: Annotated[
        Event | list[Event] | None, prop("subEvents", superseded_by=("subEvent",))
    ] = None
    super_event: Annotated[Event | list[Event] | None, prop("superEvent")] = None
    translator: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("translator")
    ] = None
    typical_age_range: Annotated[str | list[str] | None, prop("typicalAgeRange")] = None
    work_featured: Annotated[CreativeWork | list[CreativeWork] | None, prop("workFeatured")] = None
    work_performed: Annotated[CreativeWork | list[CreativeWork] | None, prop("workPerformed")] = (
        None
    )


class Intangible(Thing):
    """A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.

    https://schema.org/Intangible
    """

    jsonld_type: ClassVar[str] = "Intangible"


class MedicalEntity(Thing):
    """The most generic type of entity related to health and the practice of medicine.

    https://schema.org/MedicalEntity
    """

    jsonld_type: ClassVar[str] = "MedicalEntity"
    code: Annotated[MedicalCode | list[MedicalCode] | None, prop("code")] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    guideline: Annotated[MedicalGuideline | list[MedicalGuideline] | None, prop("guideline")] = None
    legal_status: Annotated[
        str
        | DrugLegalStatus
        | MedicalEnumeration
        | SchemaEnumeration
        | list[str | DrugLegalStatus | MedicalEnumeration | SchemaEnumeration]
        | None,
        prop("legalStatus"),
    ] = None
    medicine_system: Annotated[
        MedicineSystem | list[MedicineSystem] | None, prop("medicineSystem")
    ] = None
    recognizing_authority: Annotated[
        Organization | list[Organization] | None, prop("recognizingAuthority")
    ] = None
    relevant_specialty: Annotated[
        MedicalSpecialty | list[MedicalSpecialty] | None, prop("relevantSpecialty")
    ] = None
    study: Annotated[MedicalStudy | list[MedicalStudy] | None, prop("study")] = None


class Organization(Thing):
    """An organization such as a school, NGO, corporation, club, etc.

    https://schema.org/Organization
    """

    jsonld_type: ClassVar[str] = "Organization"
    accepted_payment_method: Annotated[
        str | LoanOrCredit | PaymentMethod | list[str | LoanOrCredit | PaymentMethod] | None,
        prop("acceptedPaymentMethod"),
    ] = None
    actionable_feedback_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("actionableFeedbackPolicy")
    ] = None
    address: Annotated[str | PostalAddress | list[str | PostalAddress] | None, prop("address")] = (
        None
    )
    agent_interaction_statistic: Annotated[
        InteractionCounter | list[InteractionCounter] | None, prop("agentInteractionStatistic")
    ] = None
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    alumni: Annotated[Person | list[Person] | None, prop("alumni")] = None
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    award: Annotated[str | list[str] | None, prop("award")] = None
    awards: Annotated[str | list[str] | None, prop("awards", superseded_by=("award",))] = None
    brand: Annotated[Brand | Organization | list[Brand | Organization] | None, prop("brand")] = None
    company_registration: Annotated[
        Certification | list[Certification] | None, prop("companyRegistration")
    ] = None
    contact_point: Annotated[ContactPoint | list[ContactPoint] | None, prop("contactPoint")] = None
    contact_points: Annotated[
        ContactPoint | list[ContactPoint] | None,
        prop("contactPoints", superseded_by=("contactPoint",)),
    ] = None
    corrections_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("correctionsPolicy")
    ] = None
    department: Annotated[Organization | list[Organization] | None, prop("department")] = None
    dissolution_date: Annotated[_dt.date | list[_dt.date] | None, prop("dissolutionDate")] = None
    diversity_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("diversityPolicy")
    ] = None
    diversity_staffing_report: Annotated[
        str | Article | list[str | Article] | None, prop("diversityStaffingReport")
    ] = None
    duns: Annotated[str | list[str] | None, prop("duns")] = None
    email: Annotated[str | list[str] | None, prop("email")] = None
    employee: Annotated[Person | list[Person] | None, prop("employee")] = None
    employees: Annotated[
        Person | list[Person] | None, prop("employees", superseded_by=("employee",))
    ] = None
    ethics_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("ethicsPolicy")
    ] = None
    event: Annotated[Event | list[Event] | None, prop("event")] = None
    events: Annotated[Event | list[Event] | None, prop("events", superseded_by=("event",))] = None
    fax_number: Annotated[str | list[str] | None, prop("faxNumber")] = None
    founder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("founder")
    ] = None
    founders: Annotated[
        Person | list[Person] | None, prop("founders", superseded_by=("founder",))
    ] = None
    founding_date: Annotated[_dt.date | list[_dt.date] | None, prop("foundingDate")] = None
    founding_location: Annotated[Place | list[Place] | None, prop("foundingLocation")] = None
    funder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("funder")
    ] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    global_location_number: Annotated[str | list[str] | None, prop("globalLocationNumber")] = None
    has_certification: Annotated[
        Certification | list[Certification] | None, prop("hasCertification")
    ] = None
    has_gs1_digital_link: Annotated[str | list[str] | None, prop("hasGS1DigitalLink")] = None
    has_member_program: Annotated[
        MemberProgram | list[MemberProgram] | None, prop("hasMemberProgram")
    ] = None
    has_merchant_return_policy: Annotated[
        MerchantReturnPolicy | list[MerchantReturnPolicy] | None, prop("hasMerchantReturnPolicy")
    ] = None
    has_offer_catalog: Annotated[
        OfferCatalog | list[OfferCatalog] | None, prop("hasOfferCatalog")
    ] = None
    has_pos: Annotated[Place | list[Place] | None, prop("hasPOS")] = None
    has_product_return_policy: Annotated[
        ProductReturnPolicy | list[ProductReturnPolicy] | None,
        prop("hasProductReturnPolicy", superseded_by=("hasMerchantReturnPolicy",)),
    ] = None
    has_shipping_service: Annotated[
        ShippingService | list[ShippingService] | None, prop("hasShippingService")
    ] = None
    interaction_statistic: Annotated[
        InteractionCounter | list[InteractionCounter] | None, prop("interactionStatistic")
    ] = None
    isic_v4: Annotated[str | list[str] | None, prop("isicV4")] = None
    iso6523_code: Annotated[str | list[str] | None, prop("iso6523Code")] = None
    keywords: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("keywords")] = None
    knows_about: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("knowsAbout"),
    ] = None
    knows_language: Annotated[
        str | Language | list[str | Language] | None, prop("knowsLanguage")
    ] = None
    legal_address: Annotated[PostalAddress | list[PostalAddress] | None, prop("legalAddress")] = (
        None
    )
    legal_name: Annotated[str | list[str] | None, prop("legalName")] = None
    legal_representative: Annotated[Person | list[Person] | None, prop("legalRepresentative")] = (
        None
    )
    lei_code: Annotated[str | list[str] | None, prop("leiCode")] = None
    location: Annotated[
        str
        | Place
        | PostalAddress
        | VirtualLocation
        | list[str | Place | PostalAddress | VirtualLocation]
        | None,
        prop("location"),
    ] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    makes_offer: Annotated[Offer | list[Offer] | None, prop("makesOffer")] = None
    member: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("member")
    ] = None
    member_of: Annotated[
        MemberProgramTier
        | Organization
        | ProgramMembership
        | list[MemberProgramTier | Organization | ProgramMembership]
        | None,
        prop("memberOf"),
    ] = None
    members: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("members", superseded_by=("member",)),
    ] = None
    naics: Annotated[str | list[str] | None, prop("naics")] = None
    nonprofit_status: Annotated[
        NLNonprofitType
        | NonprofitType
        | UKNonprofitType
        | USNonprofitType
        | list[NLNonprofitType | NonprofitType | UKNonprofitType | USNonprofitType]
        | None,
        prop("nonprofitStatus"),
    ] = None
    number_of_employees: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfEmployees")
    ] = None
    ownership_funding_info: Annotated[
        str | AboutPage | CreativeWork | list[str | AboutPage | CreativeWork] | None,
        prop("ownershipFundingInfo"),
    ] = None
    owns: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("owns")
    ] = None
    parent_organization: Annotated[
        Organization | list[Organization] | None, prop("parentOrganization")
    ] = None
    publishing_principles: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("publishingPrinciples")
    ] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    reviews: Annotated[Review | list[Review] | None, prop("reviews", superseded_by=("review",))] = (
        None
    )
    seeks: Annotated[Demand | list[Demand] | None, prop("seeks")] = None
    service_area: Annotated[
        AdministrativeArea | GeoShape | Place | list[AdministrativeArea | GeoShape | Place] | None,
        prop("serviceArea", superseded_by=("areaServed",)),
    ] = None
    skills: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("skills")] = None
    slogan: Annotated[str | list[str] | None, prop("slogan")] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None
    sub_organization: Annotated[
        Organization | list[Organization] | None, prop("subOrganization")
    ] = None
    tax_id: Annotated[str | list[str] | None, prop("taxID")] = None
    telephone: Annotated[str | list[str] | None, prop("telephone")] = None
    unnamed_sources_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("unnamedSourcesPolicy")
    ] = None
    vat_id: Annotated[str | list[str] | None, prop("vatID")] = None


class Person(Thing):
    """A person (alive, dead, undead, or fictional).

    https://schema.org/Person
    """

    jsonld_type: ClassVar[str] = "Person"
    additional_name: Annotated[str | list[str] | None, prop("additionalName")] = None
    address: Annotated[str | PostalAddress | list[str | PostalAddress] | None, prop("address")] = (
        None
    )
    affiliation: Annotated[Organization | list[Organization] | None, prop("affiliation")] = None
    agent_interaction_statistic: Annotated[
        InteractionCounter | list[InteractionCounter] | None, prop("agentInteractionStatistic")
    ] = None
    alumni_of: Annotated[
        EducationalOrganization
        | Organization
        | list[EducationalOrganization | Organization]
        | None,
        prop("alumniOf"),
    ] = None
    award: Annotated[str | list[str] | None, prop("award")] = None
    awards: Annotated[str | list[str] | None, prop("awards", superseded_by=("award",))] = None
    birth_date: Annotated[_dt.date | list[_dt.date] | None, prop("birthDate")] = None
    birth_place: Annotated[Place | list[Place] | None, prop("birthPlace")] = None
    brand: Annotated[Brand | Organization | list[Brand | Organization] | None, prop("brand")] = None
    call_sign: Annotated[str | list[str] | None, prop("callSign")] = None
    children: Annotated[Person | list[Person] | None, prop("children")] = None
    colleague: Annotated[str | Person | list[str | Person] | None, prop("colleague")] = None
    colleagues: Annotated[
        Person | list[Person] | None, prop("colleagues", superseded_by=("colleague",))
    ] = None
    contact_point: Annotated[ContactPoint | list[ContactPoint] | None, prop("contactPoint")] = None
    contact_points: Annotated[
        ContactPoint | list[ContactPoint] | None,
        prop("contactPoints", superseded_by=("contactPoint",)),
    ] = None
    death_date: Annotated[_dt.date | list[_dt.date] | None, prop("deathDate")] = None
    death_place: Annotated[Place | list[Place] | None, prop("deathPlace")] = None
    duns: Annotated[str | list[str] | None, prop("duns")] = None
    email: Annotated[str | list[str] | None, prop("email")] = None
    family_name: Annotated[str | list[str] | None, prop("familyName")] = None
    fax_number: Annotated[str | list[str] | None, prop("faxNumber")] = None
    follows: Annotated[Person | list[Person] | None, prop("follows")] = None
    funder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("funder")
    ] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    gender: Annotated[str | GenderType | list[str | GenderType] | None, prop("gender")] = None
    given_name: Annotated[str | list[str] | None, prop("givenName")] = None
    global_location_number: Annotated[str | list[str] | None, prop("globalLocationNumber")] = None
    has_certification: Annotated[
        Certification | list[Certification] | None, prop("hasCertification")
    ] = None
    has_occupation: Annotated[Occupation | list[Occupation] | None, prop("hasOccupation")] = None
    has_offer_catalog: Annotated[
        OfferCatalog | list[OfferCatalog] | None, prop("hasOfferCatalog")
    ] = None
    has_pos: Annotated[Place | list[Place] | None, prop("hasPOS")] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    home_location: Annotated[
        ContactPoint | Place | list[ContactPoint | Place] | None, prop("homeLocation")
    ] = None
    honorific_prefix: Annotated[str | list[str] | None, prop("honorificPrefix")] = None
    honorific_suffix: Annotated[str | list[str] | None, prop("honorificSuffix")] = None
    interaction_statistic: Annotated[
        InteractionCounter | list[InteractionCounter] | None, prop("interactionStatistic")
    ] = None
    isic_v4: Annotated[str | list[str] | None, prop("isicV4")] = None
    job_title: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("jobTitle")] = (
        None
    )
    knows: Annotated[Person | list[Person] | None, prop("knows")] = None
    knows_about: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("knowsAbout"),
    ] = None
    knows_language: Annotated[
        str | Language | list[str | Language] | None, prop("knowsLanguage")
    ] = None
    makes_offer: Annotated[Offer | list[Offer] | None, prop("makesOffer")] = None
    member_of: Annotated[
        MemberProgramTier
        | Organization
        | ProgramMembership
        | list[MemberProgramTier | Organization | ProgramMembership]
        | None,
        prop("memberOf"),
    ] = None
    naics: Annotated[str | list[str] | None, prop("naics")] = None
    nationality: Annotated[Country | list[Country] | None, prop("nationality")] = None
    net_worth: Annotated[
        MonetaryAmount | PriceSpecification | list[MonetaryAmount | PriceSpecification] | None,
        prop("netWorth"),
    ] = None
    owns: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("owns")
    ] = None
    parent: Annotated[Person | list[Person] | None, prop("parent")] = None
    parents: Annotated[Person | list[Person] | None, prop("parents", superseded_by=("parent",))] = (
        None
    )
    performer_in: Annotated[Event | list[Event] | None, prop("performerIn")] = None
    publishing_principles: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("publishingPrinciples")
    ] = None
    related_to: Annotated[Person | list[Person] | None, prop("relatedTo")] = None
    seeks: Annotated[Demand | list[Demand] | None, prop("seeks")] = None
    sibling: Annotated[Person | list[Person] | None, prop("sibling")] = None
    siblings: Annotated[
        Person | list[Person] | None, prop("siblings", superseded_by=("sibling",))
    ] = None
    skills: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("skills")] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None
    spouse: Annotated[Person | list[Person] | None, prop("spouse")] = None
    tax_id: Annotated[str | list[str] | None, prop("taxID")] = None
    telephone: Annotated[str | list[str] | None, prop("telephone")] = None
    vat_id: Annotated[str | list[str] | None, prop("vatID")] = None
    weight: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("weight")
    ] = None
    work_location: Annotated[
        ContactPoint | Place | list[ContactPoint | Place] | None, prop("workLocation")
    ] = None
    works_for: Annotated[Organization | list[Organization] | None, prop("worksFor")] = None


class Place(Thing):
    """Entities that have a somewhat fixed, physical extension.

    https://schema.org/Place
    """

    jsonld_type: ClassVar[str] = "Place"
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    address: Annotated[str | PostalAddress | list[str | PostalAddress] | None, prop("address")] = (
        None
    )
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    amenity_feature: Annotated[
        LocationFeatureSpecification | list[LocationFeatureSpecification] | None,
        prop("amenityFeature"),
    ] = None
    branch_code: Annotated[str | list[str] | None, prop("branchCode")] = None
    contained_in: Annotated[
        Place | list[Place] | None, prop("containedIn", superseded_by=("containedInPlace",))
    ] = None
    contained_in_place: Annotated[Place | list[Place] | None, prop("containedInPlace")] = None
    contains_place: Annotated[Place | list[Place] | None, prop("containsPlace")] = None
    event: Annotated[Event | list[Event] | None, prop("event")] = None
    events: Annotated[Event | list[Event] | None, prop("events", superseded_by=("event",))] = None
    fax_number: Annotated[str | list[str] | None, prop("faxNumber")] = None
    geo: Annotated[
        GeoCoordinates | GeoShape | list[GeoCoordinates | GeoShape] | None, prop("geo")
    ] = None
    geo_contains: Annotated[Place | list[Place] | None, prop("geoContains")] = None
    geo_covered_by: Annotated[Place | list[Place] | None, prop("geoCoveredBy")] = None
    geo_covers: Annotated[Place | list[Place] | None, prop("geoCovers")] = None
    geo_crosses: Annotated[Place | list[Place] | None, prop("geoCrosses")] = None
    geo_disjoint: Annotated[Place | list[Place] | None, prop("geoDisjoint")] = None
    geo_equals: Annotated[Place | list[Place] | None, prop("geoEquals")] = None
    geo_intersects: Annotated[Place | list[Place] | None, prop("geoIntersects")] = None
    geo_overlaps: Annotated[Place | list[Place] | None, prop("geoOverlaps")] = None
    geo_touches: Annotated[Place | list[Place] | None, prop("geoTouches")] = None
    geo_within: Annotated[Place | list[Place] | None, prop("geoWithin")] = None
    global_location_number: Annotated[str | list[str] | None, prop("globalLocationNumber")] = None
    has_certification: Annotated[
        Certification | list[Certification] | None, prop("hasCertification")
    ] = None
    has_drive_through_service: Annotated[
        bool | list[bool] | None, prop("hasDriveThroughService")
    ] = None
    has_gs1_digital_link: Annotated[str | list[str] | None, prop("hasGS1DigitalLink")] = None
    has_map: Annotated[str | Map | list[str | Map] | None, prop("hasMap")] = None
    is_accessible_for_free: Annotated[bool | list[bool] | None, prop("isAccessibleForFree")] = None
    isic_v4: Annotated[str | list[str] | None, prop("isicV4")] = None
    keywords: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("keywords")] = None
    latitude: Annotated[str | int | float | list[str | int | float] | None, prop("latitude")] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    longitude: Annotated[str | int | float | list[str | int | float] | None, prop("longitude")] = (
        None
    )
    map: Annotated[str | list[str] | None, prop("map", superseded_by=("hasMap",))] = None
    maps: Annotated[str | list[str] | None, prop("maps", superseded_by=("hasMap",))] = None
    maximum_attendee_capacity: Annotated[
        int | list[int] | None, prop("maximumAttendeeCapacity")
    ] = None
    opening_hours_specification: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None,
        prop("openingHoursSpecification"),
    ] = None
    photo: Annotated[
        ImageObject | Photograph | list[ImageObject | Photograph] | None, prop("photo")
    ] = None
    photos: Annotated[
        ImageObject | Photograph | list[ImageObject | Photograph] | None,
        prop("photos", superseded_by=("photo",)),
    ] = None
    public_access: Annotated[bool | list[bool] | None, prop("publicAccess")] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    reviews: Annotated[Review | list[Review] | None, prop("reviews", superseded_by=("review",))] = (
        None
    )
    slogan: Annotated[str | list[str] | None, prop("slogan")] = None
    smoking_allowed: Annotated[bool | list[bool] | None, prop("smokingAllowed")] = None
    special_opening_hours_specification: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None,
        prop("specialOpeningHoursSpecification"),
    ] = None
    telephone: Annotated[str | list[str] | None, prop("telephone")] = None
    tour_booking_page: Annotated[str | list[str] | None, prop("tourBookingPage")] = None


class Product(Thing):
    """Any offered product or service.

    https://schema.org/Product
    """

    jsonld_type: ClassVar[str] = "Product"
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    award: Annotated[str | list[str] | None, prop("award")] = None
    awards: Annotated[str | list[str] | None, prop("awards", superseded_by=("award",))] = None
    brand: Annotated[Brand | Organization | list[Brand | Organization] | None, prop("brand")] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    color: Annotated[str | list[str] | None, prop("color")] = None
    country_of_assembly: Annotated[str | list[str] | None, prop("countryOfAssembly")] = None
    country_of_last_processing: Annotated[
        str | list[str] | None, prop("countryOfLastProcessing")
    ] = None
    country_of_origin: Annotated[Country | list[Country] | None, prop("countryOfOrigin")] = None
    depth: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("depth")
    ] = None
    funding: Annotated[Grant | list[Grant] | None, prop("funding")] = None
    gtin12: Annotated[str | list[str] | None, prop("gtin12")] = None
    gtin13: Annotated[str | list[str] | None, prop("gtin13")] = None
    gtin14: Annotated[str | list[str] | None, prop("gtin14")] = None
    gtin8: Annotated[str | list[str] | None, prop("gtin8")] = None
    has_certification: Annotated[
        Certification | list[Certification] | None, prop("hasCertification")
    ] = None
    has_energy_consumption_details: Annotated[
        EnergyConsumptionDetails | list[EnergyConsumptionDetails] | None,
        prop("hasEnergyConsumptionDetails"),
    ] = None
    has_gs1_digital_link: Annotated[str | list[str] | None, prop("hasGS1DigitalLink")] = None
    has_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("hasMeasurement")
    ] = None
    has_merchant_return_policy: Annotated[
        MerchantReturnPolicy | list[MerchantReturnPolicy] | None, prop("hasMerchantReturnPolicy")
    ] = None
    has_product_return_policy: Annotated[
        ProductReturnPolicy | list[ProductReturnPolicy] | None,
        prop("hasProductReturnPolicy", superseded_by=("hasMerchantReturnPolicy",)),
    ] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    in_product_group_with_id: Annotated[str | list[str] | None, prop("inProductGroupWithID")] = None
    is_accessory_or_spare_part_for: Annotated[
        Product | list[Product] | None, prop("isAccessoryOrSparePartFor")
    ] = None
    is_consumable_for: Annotated[Product | list[Product] | None, prop("isConsumableFor")] = None
    is_family_friendly: Annotated[bool | list[bool] | None, prop("isFamilyFriendly")] = None
    is_related_to: Annotated[
        Product | Service | list[Product | Service] | None, prop("isRelatedTo")
    ] = None
    is_similar_to: Annotated[
        Product | Service | list[Product | Service] | None, prop("isSimilarTo")
    ] = None
    is_variant_of: Annotated[
        ProductGroup | ProductModel | list[ProductGroup | ProductModel] | None, prop("isVariantOf")
    ] = None
    item_condition: Annotated[
        OfferItemCondition | list[OfferItemCondition] | None, prop("itemCondition")
    ] = None
    keywords: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("keywords")] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    manufacturer: Annotated[Organization | list[Organization] | None, prop("manufacturer")] = None
    material: Annotated[str | Product | list[str | Product] | None, prop("material")] = None
    model: Annotated[str | ProductModel | list[str | ProductModel] | None, prop("model")] = None
    mpn: Annotated[str | list[str] | None, prop("mpn")] = None
    negative_notes: Annotated[
        str | ItemList | ListItem | list[str | ItemList | ListItem] | None, prop("negativeNotes")
    ] = None
    nsn: Annotated[str | list[str] | None, prop("nsn")] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    pattern: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("pattern")] = None
    positive_notes: Annotated[
        str | ItemList | ListItem | list[str | ItemList | ListItem] | None, prop("positiveNotes")
    ] = None
    product_id: Annotated[str | list[str] | None, prop("productID")] = None
    production_date: Annotated[_dt.date | list[_dt.date] | None, prop("productionDate")] = None
    purchase_date: Annotated[_dt.date | list[_dt.date] | None, prop("purchaseDate")] = None
    release_date: Annotated[_dt.date | list[_dt.date] | None, prop("releaseDate")] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    reviews: Annotated[Review | list[Review] | None, prop("reviews", superseded_by=("review",))] = (
        None
    )
    size: Annotated[
        str
        | DefinedTerm
        | QuantitativeValue
        | SizeSpecification
        | list[str | DefinedTerm | QuantitativeValue | SizeSpecification]
        | None,
        prop("size"),
    ] = None
    sku: Annotated[str | list[str] | None, prop("sku")] = None
    slogan: Annotated[str | list[str] | None, prop("slogan")] = None
    weight: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("weight")
    ] = None
    width: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("width")
    ] = None


class Accommodation(Place):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room.

    https://schema.org/Accommodation
    """

    jsonld_type: ClassVar[str] = "Accommodation"
    accommodation_category: Annotated[str | list[str] | None, prop("accommodationCategory")] = None
    accommodation_floor_plan: Annotated[
        FloorPlan | list[FloorPlan] | None, prop("accommodationFloorPlan")
    ] = None
    bed: Annotated[
        str | BedDetails | BedType | list[str | BedDetails | BedType] | None, prop("bed")
    ] = None
    floor_level: Annotated[str | list[str] | None, prop("floorLevel")] = None
    floor_size: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("floorSize")] = (
        None
    )
    lease_length: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("leaseLength")
    ] = None
    number_of_bathrooms_total: Annotated[int | list[int] | None, prop("numberOfBathroomsTotal")] = (
        None
    )
    number_of_bedrooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfBedrooms"),
    ] = None
    number_of_full_bathrooms: Annotated[
        int | float | list[int | float] | None, prop("numberOfFullBathrooms")
    ] = None
    number_of_partial_bathrooms: Annotated[
        int | float | list[int | float] | None, prop("numberOfPartialBathrooms")
    ] = None
    number_of_rooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfRooms"),
    ] = None
    occupancy: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("occupancy")] = (
        None
    )
    permitted_usage: Annotated[str | list[str] | None, prop("permittedUsage")] = None
    pets_allowed: Annotated[str | bool | list[str | bool] | None, prop("petsAllowed")] = None
    year_built: Annotated[int | float | list[int | float] | None, prop("yearBuilt")] = None


class AchieveAction(Action):
    """The act of accomplishing something via previous efforts.

    https://schema.org/AchieveAction
    """

    jsonld_type: ClassVar[str] = "AchieveAction"


class ActionAccessSpecification(Intangible):
    """A set of requirements that must be fulfilled in order to perform an Action.

    https://schema.org/ActionAccessSpecification
    """

    jsonld_type: ClassVar[str] = "ActionAccessSpecification"
    availability_ends: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityEnds"),
    ] = None
    availability_starts: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityStarts"),
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    eligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("eligibleRegion")
    ] = None
    expects_acceptance_of: Annotated[Offer | list[Offer] | None, prop("expectsAcceptanceOf")] = None
    ineligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("ineligibleRegion")
    ] = None
    requires_subscription: Annotated[
        bool | MediaSubscription | list[bool | MediaSubscription] | None,
        prop("requiresSubscription"),
    ] = None


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government.

    https://schema.org/AdministrativeArea
    """

    jsonld_type: ClassVar[str] = "AdministrativeArea"


class Airline(Organization):
    """An organization that provides flights for passengers.

    https://schema.org/Airline
    """

    jsonld_type: ClassVar[str] = "Airline"
    boarding_policy: Annotated[
        BoardingPolicyType | list[BoardingPolicyType] | None, prop("boardingPolicy")
    ] = None
    iata_code: Annotated[str | list[str] | None, prop("iataCode")] = None


class AlignmentObject(Intangible):
    """An intangible item that describes an alignment between a learning resource and a node in an educational framework.

    https://schema.org/AlignmentObject
    """

    jsonld_type: ClassVar[str] = "AlignmentObject"
    alignment_type: Annotated[str | list[str] | None, prop("alignmentType")] = None
    educational_framework: Annotated[str | list[str] | None, prop("educationalFramework")] = None
    target_description: Annotated[str | list[str] | None, prop("targetDescription")] = None
    target_name: Annotated[str | list[str] | None, prop("targetName")] = None
    target_url: Annotated[str | list[str] | None, prop("targetUrl")] = None


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system.

    https://schema.org/AnatomicalStructure
    """

    jsonld_type: ClassVar[str] = "AnatomicalStructure"
    associated_pathophysiology: Annotated[
        str | list[str] | None, prop("associatedPathophysiology")
    ] = None
    body_location: Annotated[str | list[str] | None, prop("bodyLocation")] = None
    connected_to: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("connectedTo")
    ] = None
    diagram: Annotated[ImageObject | list[ImageObject] | None, prop("diagram")] = None
    part_of_system: Annotated[
        AnatomicalSystem | list[AnatomicalSystem] | None, prop("partOfSystem")
    ] = None
    related_condition: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("relatedCondition")
    ] = None
    related_therapy: Annotated[
        MedicalTherapy | list[MedicalTherapy] | None, prop("relatedTherapy")
    ] = None
    sub_structure: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("subStructure")
    ] = None


class AnatomicalSystem(MedicalEntity):
    """An anatomical system is a group of anatomical structures that work together to perform a certain task.

    https://schema.org/AnatomicalSystem
    """

    jsonld_type: ClassVar[str] = "AnatomicalSystem"
    associated_pathophysiology: Annotated[
        str | list[str] | None, prop("associatedPathophysiology")
    ] = None
    comprised_of: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | list[AnatomicalStructure | AnatomicalSystem]
        | None,
        prop("comprisedOf"),
    ] = None
    related_condition: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("relatedCondition")
    ] = None
    related_structure: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("relatedStructure")
    ] = None
    related_therapy: Annotated[
        MedicalTherapy | list[MedicalTherapy] | None, prop("relatedTherapy")
    ] = None


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.

    https://schema.org/ArchiveComponent
    """

    jsonld_type: ClassVar[str] = "ArchiveComponent"
    holding_archive: Annotated[
        ArchiveOrganization | list[ArchiveOrganization] | None, prop("holdingArchive")
    ] = None
    item_location: Annotated[
        str | Place | PostalAddress | list[str | Place | PostalAddress] | None, prop("itemLocation")
    ] = None


class Article(CreativeWork):
    """An article, such as a news article or piece of investigative report.

    https://schema.org/Article
    """

    jsonld_type: ClassVar[str] = "Article"
    article_body: Annotated[str | list[str] | None, prop("articleBody")] = None
    article_section: Annotated[str | list[str] | None, prop("articleSection")] = None
    backstory: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("backstory")
    ] = None
    page_end: Annotated[str | int | list[str | int] | None, prop("pageEnd")] = None
    page_start: Annotated[str | int | list[str | int] | None, prop("pageStart")] = None
    pagination: Annotated[str | list[str] | None, prop("pagination")] = None
    speakable: Annotated[
        str | SpeakableSpecification | list[str | SpeakableSpecification] | None, prop("speakable")
    ] = None


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    https://schema.org/AssessAction
    """

    jsonld_type: ClassVar[str] = "AssessAction"


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.

    https://schema.org/Atlas
    """

    jsonld_type: ClassVar[str] = "Atlas"


class Audience(Intangible):
    """Intended audience for an item, i.e. the group for whom the item was created.

    https://schema.org/Audience
    """

    jsonld_type: ClassVar[str] = "Audience"
    audience_type: Annotated[str | list[str] | None, prop("audienceType")] = None
    geographic_area: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("geographicArea")
    ] = None


class BedDetails(Intangible):
    """An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room.

    https://schema.org/BedDetails
    """

    jsonld_type: ClassVar[str] = "BedDetails"
    number_of_beds: Annotated[int | float | list[int | float] | None, prop("numberOfBeds")] = None
    type_of_bed: Annotated[str | BedType | list[str | BedType] | None, prop("typeOfBed")] = None


class Blog(CreativeWork):
    """A blog, sometimes known as a "weblog".

    https://schema.org/Blog
    """

    jsonld_type: ClassVar[str] = "Blog"
    blog_post: Annotated[BlogPosting | list[BlogPosting] | None, prop("blogPost")] = None
    blog_posts: Annotated[
        BlogPosting | list[BlogPosting] | None, prop("blogPosts", superseded_by=("blogPost",))
    ] = None
    issn: Annotated[str | list[str] | None, prop("issn")] = None


class Book(CreativeWork):
    """A book.

    https://schema.org/Book
    """

    jsonld_type: ClassVar[str] = "Book"
    abridged: Annotated[bool | list[bool] | None, prop("abridged")] = None
    book_edition: Annotated[str | list[str] | None, prop("bookEdition")] = None
    book_format: Annotated[BookFormatType | list[BookFormatType] | None, prop("bookFormat")] = None
    illustrator: Annotated[Person | list[Person] | None, prop("illustrator")] = None
    isbn: Annotated[str | list[str] | None, prop("isbn")] = None
    number_of_pages: Annotated[int | list[int] | None, prop("numberOfPages")] = None


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    https://schema.org/Brand
    """

    jsonld_type: ClassVar[str] = "Brand"
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    slogan: Annotated[str | list[str] | None, prop("slogan")] = None


class BroadcastChannel(Intangible):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    https://schema.org/BroadcastChannel
    """

    jsonld_type: ClassVar[str] = "BroadcastChannel"
    broadcast_channel_id: Annotated[str | list[str] | None, prop("broadcastChannelId")] = None
    broadcast_frequency: Annotated[
        str | BroadcastFrequencySpecification | list[str | BroadcastFrequencySpecification] | None,
        prop("broadcastFrequency"),
    ] = None
    broadcast_service_tier: Annotated[str | list[str] | None, prop("broadcastServiceTier")] = None
    genre: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("genre")] = None
    in_broadcast_lineup: Annotated[
        CableOrSatelliteService | list[CableOrSatelliteService] | None, prop("inBroadcastLineup")
    ] = None
    provides_broadcast_service: Annotated[
        BroadcastService | list[BroadcastService] | None, prop("providesBroadcastService")
    ] = None


class BroadcastFrequencySpecification(Intangible):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    https://schema.org/BroadcastFrequencySpecification
    """

    jsonld_type: ClassVar[str] = "BroadcastFrequencySpecification"
    broadcast_frequency_value: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("broadcastFrequencyValue"),
    ] = None
    broadcast_signal_modulation: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("broadcastSignalModulation"),
    ] = None
    broadcast_sub_channel: Annotated[str | list[str] | None, prop("broadcastSubChannel")] = None


class BusinessEvent(Event):
    """Event type: Business event.

    https://schema.org/BusinessEvent
    """

    jsonld_type: ClassVar[str] = "BusinessEvent"


class Certification(CreativeWork):
    """A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization.

    https://schema.org/Certification
    """

    jsonld_type: ClassVar[str] = "Certification"
    audit_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("auditDate")
    ] = None
    certification_identification: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("certificationIdentification")
    ] = None
    certification_rating: Annotated[Rating | list[Rating] | None, prop("certificationRating")] = (
        None
    )
    certification_status: Annotated[
        CertificationStatusEnumeration | list[CertificationStatusEnumeration] | None,
        prop("certificationStatus"),
    ] = None
    has_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("hasMeasurement")
    ] = None
    issued_by: Annotated[Organization | list[Organization] | None, prop("issuedBy")] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_in: Annotated[AdministrativeArea | list[AdministrativeArea] | None, prop("validIn")] = (
        None
    )


class Chapter(CreativeWork):
    """One of the sections into which a book is divided.

    https://schema.org/Chapter
    """

    jsonld_type: ClassVar[str] = "Chapter"
    page_end: Annotated[str | int | list[str | int] | None, prop("pageEnd")] = None
    page_start: Annotated[str | int | list[str | int] | None, prop("pageStart")] = None
    pagination: Annotated[str | list[str] | None, prop("pagination")] = None


class ChildrensEvent(Event):
    """Event type: Children's event.

    https://schema.org/ChildrensEvent
    """

    jsonld_type: ClassVar[str] = "ChildrensEvent"


class CivicStructure(Place):
    """A public structure, such as a town hall or concert hall.

    https://schema.org/CivicStructure
    """

    jsonld_type: ClassVar[str] = "CivicStructure"
    opening_hours: Annotated[str | list[str] | None, prop("openingHours")] = None


class Claim(CreativeWork):
    """A Claim in Schema.org represents a specific, factually-oriented claim that could be the itemReviewed in a ClaimReview.

    https://schema.org/Claim
    """

    jsonld_type: ClassVar[str] = "Claim"
    appearance: Annotated[CreativeWork | list[CreativeWork] | None, prop("appearance")] = None
    claim_interpreter: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("claimInterpreter")
    ] = None
    first_appearance: Annotated[
        CreativeWork | list[CreativeWork] | None, prop("firstAppearance")
    ] = None


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    https://schema.org/Clip
    """

    jsonld_type: ClassVar[str] = "Clip"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    clip_number: Annotated[str | int | list[str | int] | None, prop("clipNumber")] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    end_offset: Annotated[int | float | list[int | float] | None, prop("endOffset")] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    part_of_episode: Annotated[Episode | list[Episode] | None, prop("partOfEpisode")] = None
    part_of_season: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None, prop("partOfSeason")
    ] = None
    part_of_series: Annotated[
        CreativeWorkSeries | list[CreativeWorkSeries] | None, prop("partOfSeries")
    ] = None
    start_offset: Annotated[int | float | list[int | float] | None, prop("startOffset")] = None


class Code(CreativeWork):
    """Computer programming source code.

    https://schema.org/Code

    Deprecated: superseded by SoftwareSourceCode.
    """

    jsonld_type: ClassVar[str] = "Code"


class Collection(CreativeWork):
    """A collection of items, e.g. creative works or products.

    https://schema.org/Collection
    """

    jsonld_type: ClassVar[str] = "Collection"
    collection_size: Annotated[int | list[int] | None, prop("collectionSize")] = None


class ComedyEvent(Event):
    """Event type: Comedy event.

    https://schema.org/ComedyEvent
    """

    jsonld_type: ClassVar[str] = "ComedyEvent"


class ComicStory(CreativeWork):
    """The term "story" is any indivisible, re-printable unit of a comic, including the interior stories, covers, and backmatter.

    https://schema.org/ComicStory
    """

    jsonld_type: ClassVar[str] = "ComicStory"
    artist: Annotated[Person | list[Person] | None, prop("artist")] = None
    colorist: Annotated[Person | list[Person] | None, prop("colorist")] = None
    inker: Annotated[Person | list[Person] | None, prop("inker")] = None
    letterer: Annotated[Person | list[Person] | None, prop("letterer")] = None
    penciler: Annotated[Person | list[Person] | None, prop("penciler")] = None


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post.

    https://schema.org/Comment
    """

    jsonld_type: ClassVar[str] = "Comment"
    downvote_count: Annotated[int | list[int] | None, prop("downvoteCount")] = None
    parent_item: Annotated[
        Comment | CreativeWork | list[Comment | CreativeWork] | None, prop("parentItem")
    ] = None
    shared_content: Annotated[CreativeWork | list[CreativeWork] | None, prop("sharedContent")] = (
        None
    )
    upvote_count: Annotated[int | list[int] | None, prop("upvoteCount")] = None


class ComputerLanguage(Intangible):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations.

    https://schema.org/ComputerLanguage
    """

    jsonld_type: ClassVar[str] = "ComputerLanguage"


class Consortium(Organization):
    """A Consortium is a membership Organization whose members are typically Organizations.

    https://schema.org/Consortium
    """

    jsonld_type: ClassVar[str] = "Consortium"


class ConstraintNode(Intangible):
    """The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract...

    https://schema.org/ConstraintNode
    """

    jsonld_type: ClassVar[str] = "ConstraintNode"
    constraint_property: Annotated[str | list[str] | None, prop("constraintProperty")] = None
    num_constraints: Annotated[int | list[int] | None, prop("numConstraints")] = None


class ConsumeAction(Action):
    """The act of ingesting information/resources/food.

    https://schema.org/ConsumeAction
    """

    jsonld_type: ClassVar[str] = "ConsumeAction"
    action_accessibility_requirement: Annotated[
        ActionAccessSpecification | list[ActionAccessSpecification] | None,
        prop("actionAccessibilityRequirement"),
    ] = None
    expects_acceptance_of: Annotated[Offer | list[Offer] | None, prop("expectsAcceptanceOf")] = None


class ControlAction(Action):
    """An agent controls a device or application.

    https://schema.org/ControlAction
    """

    jsonld_type: ClassVar[str] = "ControlAction"


class Conversation(CreativeWork):
    """One or more messages between organizations or people on a particular topic.

    https://schema.org/Conversation
    """

    jsonld_type: ClassVar[str] = "Conversation"


class Cooperative(Organization):
    """An organization that is a joint project of multiple organizations or persons.

    https://schema.org/Cooperative
    """

    jsonld_type: ClassVar[str] = "Cooperative"


class Corporation(Organization):
    """Organization: A business corporation.

    https://schema.org/Corporation
    """

    jsonld_type: ClassVar[str] = "Corporation"
    ticker_symbol: Annotated[str | list[str] | None, prop("tickerSymbol")] = None


class Course(CreativeWork):
    """A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study.

    https://schema.org/Course
    """

    jsonld_type: ClassVar[str] = "Course"
    available_language: Annotated[
        str | Language | list[str | Language] | None, prop("availableLanguage")
    ] = None
    course_code: Annotated[str | list[str] | None, prop("courseCode")] = None
    course_prerequisites: Annotated[
        str | AlignmentObject | Course | list[str | AlignmentObject | Course] | None,
        prop("coursePrerequisites"),
    ] = None
    educational_credential_awarded: Annotated[
        str | list[str] | None, prop("educationalCredentialAwarded")
    ] = None
    financial_aid_eligible: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("financialAidEligible")
    ] = None
    has_course_instance: Annotated[
        CourseInstance | list[CourseInstance] | None, prop("hasCourseInstance")
    ] = None
    number_of_credits: Annotated[
        int | StructuredValue | list[int | StructuredValue] | None, prop("numberOfCredits")
    ] = None
    occupational_credential_awarded: Annotated[
        str | list[str] | None, prop("occupationalCredentialAwarded")
    ] = None
    syllabus_sections: Annotated[Syllabus | list[Syllabus] | None, prop("syllabusSections")] = None
    total_historical_enrollment: Annotated[
        int | list[int] | None, prop("totalHistoricalEnrollment")
    ] = None


class CourseInstance(Event):
    """An instance of a Course which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.

    https://schema.org/CourseInstance
    """

    jsonld_type: ClassVar[str] = "CourseInstance"
    course_mode: Annotated[str | list[str] | None, prop("courseMode")] = None
    course_schedule: Annotated[Schedule | list[Schedule] | None, prop("courseSchedule")] = None
    course_workload: Annotated[str | list[str] | None, prop("courseWorkload")] = None
    instructor: Annotated[Person | list[Person] | None, prop("instructor")] = None


class CreateAction(Action):
    """The act of deliberately creating/producing/generating/building a result out of the agent.

    https://schema.org/CreateAction
    """

    jsonld_type: ClassVar[str] = "CreateAction"


class CreativeWorkSeason(CreativeWork):
    """A media season, e.g. TV, radio, video game etc.

    https://schema.org/CreativeWorkSeason
    """

    jsonld_type: ClassVar[str] = "CreativeWorkSeason"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    episode: Annotated[Episode | list[Episode] | None, prop("episode")] = None
    episodes: Annotated[
        Episode | list[Episode] | None, prop("episodes", superseded_by=("episode",))
    ] = None
    number_of_episodes: Annotated[int | list[int] | None, prop("numberOfEpisodes")] = None
    part_of_series: Annotated[
        CreativeWorkSeries | list[CreativeWorkSeries] | None, prop("partOfSeries")
    ] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    season_number: Annotated[str | int | list[str | int] | None, prop("seasonNumber")] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class DanceEvent(Event):
    """Event type: A social dance.

    https://schema.org/DanceEvent
    """

    jsonld_type: ClassVar[str] = "DanceEvent"


class DataCatalog(CreativeWork):
    """A collection of datasets.

    https://schema.org/DataCatalog
    """

    jsonld_type: ClassVar[str] = "DataCatalog"
    dataset: Annotated[Dataset | list[Dataset] | None, prop("dataset")] = None
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None


class DataFeedItem(Intangible):
    """A single item within a larger data feed.

    https://schema.org/DataFeedItem
    """

    jsonld_type: ClassVar[str] = "DataFeedItem"
    date_created: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateCreated")
    ] = None
    date_deleted: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateDeleted")
    ] = None
    date_modified: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateModified")
    ] = None
    item: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("item")
    ] = None


class Dataset(CreativeWork):
    """A body of structured information describing some topic(s) of interest.

    https://schema.org/Dataset
    """

    jsonld_type: ClassVar[str] = "Dataset"
    catalog: Annotated[
        DataCatalog | list[DataCatalog] | None,
        prop("catalog", superseded_by=("includedInDataCatalog",)),
    ] = None
    dataset_time_interval: Annotated[
        _dt.datetime | list[_dt.datetime] | None,
        prop("datasetTimeInterval", superseded_by=("temporalCoverage",)),
    ] = None
    distribution: Annotated[DataDownload | list[DataDownload] | None, prop("distribution")] = None
    included_data_catalog: Annotated[
        DataCatalog | list[DataCatalog] | None,
        prop("includedDataCatalog", superseded_by=("includedInDataCatalog",)),
    ] = None
    included_in_data_catalog: Annotated[
        DataCatalog | list[DataCatalog] | None, prop("includedInDataCatalog")
    ] = None
    issn: Annotated[str | list[str] | None, prop("issn")] = None
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None
    variable_measured: Annotated[
        str
        | PropertyValue
        | StatisticalVariable
        | list[str | PropertyValue | StatisticalVariable]
        | None,
        prop("variableMeasured"),
    ] = None


class DefinedTerm(Intangible):
    """A word, name, acronym, phrase, etc. with a formal definition.

    https://schema.org/DefinedTerm
    """

    jsonld_type: ClassVar[str] = "DefinedTerm"
    about: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("about")
    ] = None
    in_defined_term_set: Annotated[
        str | DefinedTermSet | list[str | DefinedTermSet] | None, prop("inDefinedTermSet")
    ] = None
    term_code: Annotated[str | list[str] | None, prop("termCode")] = None


class DefinedTermSet(CreativeWork):
    """A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration.

    https://schema.org/DefinedTermSet
    """

    jsonld_type: ClassVar[str] = "DefinedTermSet"
    has_defined_term: Annotated[DefinedTerm | list[DefinedTerm] | None, prop("hasDefinedTerm")] = (
        None
    )


class DeliveryEvent(Event):
    """An event involving the delivery of an item.

    https://schema.org/DeliveryEvent
    """

    jsonld_type: ClassVar[str] = "DeliveryEvent"
    access_code: Annotated[str | list[str] | None, prop("accessCode")] = None
    available_from: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("availableFrom")] = (
        None
    )
    available_through: Annotated[
        _dt.datetime | list[_dt.datetime] | None, prop("availableThrough")
    ] = None
    has_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("hasDeliveryMethod")
    ] = None


class Demand(Intangible):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services.

    https://schema.org/Demand
    """

    jsonld_type: ClassVar[str] = "Demand"
    accepted_payment_method: Annotated[
        str | LoanOrCredit | PaymentMethod | list[str | LoanOrCredit | PaymentMethod] | None,
        prop("acceptedPaymentMethod"),
    ] = None
    advance_booking_requirement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("advanceBookingRequirement")
    ] = None
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    availability: Annotated[
        ItemAvailability | list[ItemAvailability] | None, prop("availability")
    ] = None
    availability_ends: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityEnds"),
    ] = None
    availability_starts: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityStarts"),
    ] = None
    available_at_or_from: Annotated[Place | list[Place] | None, prop("availableAtOrFrom")] = None
    available_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("availableDeliveryMethod")
    ] = None
    business_function: Annotated[
        BusinessFunction | list[BusinessFunction] | None, prop("businessFunction")
    ] = None
    delivery_lead_time: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("deliveryLeadTime")
    ] = None
    eligible_customer_type: Annotated[
        BusinessEntityType | list[BusinessEntityType] | None, prop("eligibleCustomerType")
    ] = None
    eligible_duration: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("eligibleDuration")
    ] = None
    eligible_quantity: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("eligibleQuantity")
    ] = None
    eligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("eligibleRegion")
    ] = None
    eligible_transaction_volume: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("eligibleTransactionVolume")
    ] = None
    gtin12: Annotated[str | list[str] | None, prop("gtin12")] = None
    gtin13: Annotated[str | list[str] | None, prop("gtin13")] = None
    gtin14: Annotated[str | list[str] | None, prop("gtin14")] = None
    gtin8: Annotated[str | list[str] | None, prop("gtin8")] = None
    includes_object: Annotated[
        TypeAndQuantityNode | list[TypeAndQuantityNode] | None, prop("includesObject")
    ] = None
    ineligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("ineligibleRegion")
    ] = None
    inventory_level: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("inventoryLevel")
    ] = None
    item_condition: Annotated[
        OfferItemCondition | list[OfferItemCondition] | None, prop("itemCondition")
    ] = None
    item_offered: Annotated[
        AggregateOffer
        | CreativeWork
        | Event
        | MenuItem
        | Product
        | Service
        | Trip
        | list[AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip]
        | None,
        prop("itemOffered"),
    ] = None
    mpn: Annotated[str | list[str] | None, prop("mpn")] = None
    price_specification: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("priceSpecification")
    ] = None
    seller: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("seller")
    ] = None
    serial_number: Annotated[str | list[str] | None, prop("serialNumber")] = None
    sku: Annotated[str | list[str] | None, prop("sku")] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None
    warranty: Annotated[WarrantyPromise | list[WarrantyPromise] | None, prop("warranty")] = None


class DigitalDocument(CreativeWork):
    """An electronic file or document.

    https://schema.org/DigitalDocument
    """

    jsonld_type: ClassVar[str] = "DigitalDocument"
    has_digital_document_permission: Annotated[
        DigitalDocumentPermission | list[DigitalDocumentPermission] | None,
        prop("hasDigitalDocumentPermission"),
    ] = None


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    https://schema.org/DigitalDocumentPermission
    """

    jsonld_type: ClassVar[str] = "DigitalDocumentPermission"
    grantee: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("grantee"),
    ] = None
    permission_type: Annotated[
        DigitalDocumentPermissionType | list[DigitalDocumentPermissionType] | None,
        prop("permissionType"),
    ] = None


class Drawing(CreativeWork):
    """A picture or diagram made with a pencil, pen, or crayon rather than paint.

    https://schema.org/Drawing
    """

    jsonld_type: ClassVar[str] = "Drawing"


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins.

    https://schema.org/DrugClass
    """

    jsonld_type: ClassVar[str] = "DrugClass"
    drug: Annotated[Drug | list[Drug] | None, prop("drug")] = None


class DrugCost(MedicalEntity):
    """The cost per unit of a medical drug.

    https://schema.org/DrugCost
    """

    jsonld_type: ClassVar[str] = "DrugCost"
    applicable_location: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("applicableLocation")
    ] = None
    cost_category: Annotated[
        DrugCostCategory | list[DrugCostCategory] | None, prop("costCategory")
    ] = None
    cost_currency: Annotated[str | list[str] | None, prop("costCurrency")] = None
    cost_origin: Annotated[str | list[str] | None, prop("costOrigin")] = None
    cost_per_unit: Annotated[
        str
        | int
        | float
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[
            str
            | int
            | float
            | DriveWheelConfigurationValue
            | QualitativeValue
            | SteeringPositionValue
        ]
        | None,
        prop("costPerUnit"),
    ] = None
    drug_unit: Annotated[str | list[str] | None, prop("drugUnit")] = None


class EducationEvent(Event):
    """Event type: Education event.

    https://schema.org/EducationEvent
    """

    jsonld_type: ClassVar[str] = "EducationEvent"
    assesses: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("assesses")] = None
    teaches: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("teaches")] = None


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate.

    https://schema.org/EducationalOccupationalProgram
    """

    jsonld_type: ClassVar[str] = "EducationalOccupationalProgram"
    application_deadline: Annotated[
        str | _dt.date | list[str | _dt.date] | None, prop("applicationDeadline")
    ] = None
    application_start_date: Annotated[
        _dt.date | list[_dt.date] | None, prop("applicationStartDate")
    ] = None
    day_of_week: Annotated[DayOfWeek | list[DayOfWeek] | None, prop("dayOfWeek")] = None
    educational_credential_awarded: Annotated[
        str | list[str] | None, prop("educationalCredentialAwarded")
    ] = None
    educational_program_mode: Annotated[str | list[str] | None, prop("educationalProgramMode")] = (
        None
    )
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    financial_aid_eligible: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("financialAidEligible")
    ] = None
    has_course: Annotated[Course | list[Course] | None, prop("hasCourse")] = None
    maximum_enrollment: Annotated[int | list[int] | None, prop("maximumEnrollment")] = None
    number_of_credits: Annotated[
        int | StructuredValue | list[int | StructuredValue] | None, prop("numberOfCredits")
    ] = None
    occupational_credential_awarded: Annotated[
        str | list[str] | None, prop("occupationalCredentialAwarded")
    ] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    program_prerequisites: Annotated[
        str | AlignmentObject | Course | list[str | AlignmentObject | Course] | None,
        prop("programPrerequisites"),
    ] = None
    program_type: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("programType")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    salary_upon_completion: Annotated[
        MonetaryAmountDistribution | list[MonetaryAmountDistribution] | None,
        prop("salaryUponCompletion"),
    ] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None
    term_duration: Annotated[str | list[str] | None, prop("termDuration")] = None
    terms_per_year: Annotated[int | float | list[int | float] | None, prop("termsPerYear")] = None
    time_of_day: Annotated[str | list[str] | None, prop("timeOfDay")] = None
    time_to_complete: Annotated[str | list[str] | None, prop("timeToComplete")] = None
    training_salary: Annotated[
        MonetaryAmountDistribution | list[MonetaryAmountDistribution] | None, prop("trainingSalary")
    ] = None
    typical_credits_per_term: Annotated[
        int | StructuredValue | list[int | StructuredValue] | None, prop("typicalCreditsPerTerm")
    ] = None


class EnergyConsumptionDetails(Intangible):
    """EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy.

    https://schema.org/EnergyConsumptionDetails
    """

    jsonld_type: ClassVar[str] = "EnergyConsumptionDetails"
    energy_efficiency_scale_max: Annotated[
        EUEnergyEfficiencyEnumeration | list[EUEnergyEfficiencyEnumeration] | None,
        prop("energyEfficiencyScaleMax"),
    ] = None
    energy_efficiency_scale_min: Annotated[
        EUEnergyEfficiencyEnumeration | list[EUEnergyEfficiencyEnumeration] | None,
        prop("energyEfficiencyScaleMin"),
    ] = None
    has_energy_efficiency_category: Annotated[
        EUEnergyEfficiencyEnumeration
        | EnergyEfficiencyEnumeration
        | EnergyStarEnergyEfficiencyEnumeration
        | list[
            EUEnergyEfficiencyEnumeration
            | EnergyEfficiencyEnumeration
            | EnergyStarEnergyEfficiencyEnumeration
        ]
        | None,
        prop("hasEnergyEfficiencyCategory"),
    ] = None


class EntryPoint(Intangible):
    """An entry point, within some Web-based protocol.

    https://schema.org/EntryPoint
    """

    jsonld_type: ClassVar[str] = "EntryPoint"
    action_application: Annotated[
        SoftwareApplication | list[SoftwareApplication] | None, prop("actionApplication")
    ] = None
    action_platform: Annotated[
        str | DigitalPlatformEnumeration | list[str | DigitalPlatformEnumeration] | None,
        prop("actionPlatform"),
    ] = None
    application: Annotated[
        SoftwareApplication | list[SoftwareApplication] | None,
        prop("application", superseded_by=("actionApplication",)),
    ] = None
    content_type: Annotated[str | list[str] | None, prop("contentType")] = None
    encoding_type: Annotated[str | list[str] | None, prop("encodingType")] = None
    http_method: Annotated[str | list[str] | None, prop("httpMethod")] = None
    url_template: Annotated[str | list[str] | None, prop("urlTemplate")] = None


class Enumeration(Intangible):
    """Lists or enumerations, for example, a list of cuisines or music genres, etc.

    https://schema.org/Enumeration
    """

    jsonld_type: ClassVar[str] = "Enumeration"


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    https://schema.org/Episode
    """

    jsonld_type: ClassVar[str] = "Episode"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    episode_number: Annotated[str | int | list[str | int] | None, prop("episodeNumber")] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    part_of_season: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None, prop("partOfSeason")
    ] = None
    part_of_series: Annotated[
        CreativeWorkSeries | list[CreativeWorkSeries] | None, prop("partOfSeries")
    ] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class ExhibitionEvent(Event):
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...

    https://schema.org/ExhibitionEvent
    """

    jsonld_type: ClassVar[str] = "ExhibitionEvent"


class Festival(Event):
    """Event type: Festival.

    https://schema.org/Festival
    """

    jsonld_type: ClassVar[str] = "Festival"


class FinancialIncentive(Intangible):
    """Represents financial incentives for goods/services offered by an organization (or individual).

    https://schema.org/FinancialIncentive
    """

    jsonld_type: ClassVar[str] = "FinancialIncentive"
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    eligible_with_supplier: Annotated[
        Organization | list[Organization] | None, prop("eligibleWithSupplier")
    ] = None
    incentive_amount: Annotated[
        LoanOrCredit
        | QuantitativeValue
        | UnitPriceSpecification
        | list[LoanOrCredit | QuantitativeValue | UnitPriceSpecification]
        | None,
        prop("incentiveAmount"),
    ] = None
    incentive_status: Annotated[
        IncentiveStatus | list[IncentiveStatus] | None, prop("incentiveStatus")
    ] = None
    incentive_type: Annotated[IncentiveType | list[IncentiveType] | None, prop("incentiveType")] = (
        None
    )
    incentivized_item: Annotated[
        DefinedTerm | Product | list[DefinedTerm | Product] | None, prop("incentivizedItem")
    ] = None
    income_limit: Annotated[
        str | MonetaryAmount | list[str | MonetaryAmount] | None, prop("incomeLimit")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    publisher: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("publisher")
    ] = None
    purchase_price_limit: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("purchasePriceLimit")
    ] = None
    purchase_type: Annotated[PurchaseType | list[PurchaseType] | None, prop("purchaseType")] = None
    qualified_expense: Annotated[
        IncentiveQualifiedExpenseType | list[IncentiveQualifiedExpenseType] | None,
        prop("qualifiedExpense"),
    ] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None


class FindAction(Action):
    """The act of finding an object.\\n\\nRelated actions:\\n\\n* SearchAction: FindAction is generally lead by a SearchAction, but not necessarily.

    https://schema.org/FindAction
    """

    jsonld_type: ClassVar[str] = "FindAction"


class FloorPlan(Intangible):
    """A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale.

    https://schema.org/FloorPlan
    """

    jsonld_type: ClassVar[str] = "FloorPlan"
    amenity_feature: Annotated[
        LocationFeatureSpecification | list[LocationFeatureSpecification] | None,
        prop("amenityFeature"),
    ] = None
    floor_size: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("floorSize")] = (
        None
    )
    is_plan_for_apartment: Annotated[
        Accommodation | list[Accommodation] | None, prop("isPlanForApartment")
    ] = None
    layout_image: Annotated[
        str | ImageObject | list[str | ImageObject] | None, prop("layoutImage")
    ] = None
    number_of_accommodation_units: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfAccommodationUnits")
    ] = None
    number_of_available_accommodation_units: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None,
        prop("numberOfAvailableAccommodationUnits"),
    ] = None
    number_of_bathrooms_total: Annotated[int | list[int] | None, prop("numberOfBathroomsTotal")] = (
        None
    )
    number_of_bedrooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfBedrooms"),
    ] = None
    number_of_full_bathrooms: Annotated[
        int | float | list[int | float] | None, prop("numberOfFullBathrooms")
    ] = None
    number_of_partial_bathrooms: Annotated[
        int | float | list[int | float] | None, prop("numberOfPartialBathrooms")
    ] = None
    number_of_rooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfRooms"),
    ] = None
    pets_allowed: Annotated[str | bool | list[str | bool] | None, prop("petsAllowed")] = None


class FoodEvent(Event):
    """Event type: Food event.

    https://schema.org/FoodEvent
    """

    jsonld_type: ClassVar[str] = "FoodEvent"


class FundingScheme(Organization):
    """A FundingScheme combines organizational, project and policy aspects of grant-based funding that sets guidelines, principles and mechanisms to support other kinds of projects and activities.

    https://schema.org/FundingScheme
    """

    jsonld_type: ClassVar[str] = "FundingScheme"


class Game(CreativeWork):
    """The Game type represents things which are games.

    https://schema.org/Game
    """

    jsonld_type: ClassVar[str] = "Game"
    character_attribute: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None,
        prop("characterAttribute"),
    ] = None
    game_item: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("gameItem")
    ] = None
    game_location: Annotated[
        str | Place | PostalAddress | list[str | Place | PostalAddress] | None, prop("gameLocation")
    ] = None
    number_of_players: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfPlayers")
    ] = None
    quest: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("quest")
    ] = None


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    https://schema.org/GameServer
    """

    jsonld_type: ClassVar[str] = "GameServer"
    game: Annotated[VideoGame | list[VideoGame] | None, prop("game")] = None
    players_online: Annotated[int | list[int] | None, prop("playersOnline")] = None
    server_status: Annotated[
        GameServerStatus | list[GameServerStatus] | None, prop("serverStatus")
    ] = None


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    https://schema.org/GovernmentOrganization
    """

    jsonld_type: ClassVar[str] = "GovernmentOrganization"


class Grant(Intangible):
    """A grant, typically financial or otherwise quantifiable, of resources.

    https://schema.org/Grant
    """

    jsonld_type: ClassVar[str] = "Grant"
    funded_item: Annotated[
        CreativeWork
        | Event
        | MedicalEntity
        | Organization
        | Person
        | PhysicalExam
        | Product
        | list[
            CreativeWork | Event | MedicalEntity | Organization | Person | PhysicalExam | Product
        ]
        | None,
        prop("fundedItem"),
    ] = None
    funder: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("funder")
    ] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None


class Guide(CreativeWork):
    """Guide is a page or article that recommends specific products or services, or aspects of a thing for a user to consider.

    https://schema.org/Guide
    """

    jsonld_type: ClassVar[str] = "Guide"
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    review_aspect: Annotated[
        str | StructuredValue | list[str | StructuredValue] | None, prop("reviewAspect")
    ] = None


class Hackathon(Event):
    """A hackathon event.

    https://schema.org/Hackathon
    """

    jsonld_type: ClassVar[str] = "Hackathon"


class HealthTopicContent(CreativeWork):
    """HealthTopicContent is WebContent that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments.

    https://schema.org/HealthTopicContent
    """

    jsonld_type: ClassVar[str] = "HealthTopicContent"
    has_health_aspect: Annotated[
        HealthAspectEnumeration | list[HealthAspectEnumeration] | None, prop("hasHealthAspect")
    ] = None


class HowTo(CreativeWork):
    """Instructions that explain how to achieve a result by performing a sequence of steps.

    https://schema.org/HowTo
    """

    jsonld_type: ClassVar[str] = "HowTo"
    estimated_cost: Annotated[
        str | MonetaryAmount | list[str | MonetaryAmount] | None, prop("estimatedCost")
    ] = None
    perform_time: Annotated[str | list[str] | None, prop("performTime")] = None
    prep_time: Annotated[str | list[str] | None, prop("prepTime")] = None
    step: Annotated[
        str
        | CreativeWork
        | HowToSection
        | HowToStep
        | list[str | CreativeWork | HowToSection | HowToStep]
        | None,
        prop("step"),
    ] = None
    steps: Annotated[
        str | CreativeWork | ItemList | list[str | CreativeWork | ItemList] | None,
        prop("steps", superseded_by=("step",)),
    ] = None
    supply: Annotated[str | HowToSupply | list[str | HowToSupply] | None, prop("supply")] = None
    tool: Annotated[str | HowToTool | list[str | HowToTool] | None, prop("tool")] = None
    total_time: Annotated[str | list[str] | None, prop("totalTime")] = None
    yield_: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("yield")
    ] = None


class IndividualProduct(Product):
    """A single, identifiable product instance (e.g. a laptop with a particular serial number).

    https://schema.org/IndividualProduct
    """

    jsonld_type: ClassVar[str] = "IndividualProduct"
    serial_number: Annotated[str | list[str] | None, prop("serialNumber")] = None


class InteractAction(Action):
    """The act of interacting with another person or organization.

    https://schema.org/InteractAction
    """

    jsonld_type: ClassVar[str] = "InteractAction"


class Invoice(Intangible):
    """A statement of the money due for goods or services; a bill.

    https://schema.org/Invoice
    """

    jsonld_type: ClassVar[str] = "Invoice"
    account_id: Annotated[str | list[str] | None, prop("accountId")] = None
    billing_period: Annotated[str | list[str] | None, prop("billingPeriod")] = None
    broker: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("broker")
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    confirmation_number: Annotated[str | list[str] | None, prop("confirmationNumber")] = None
    customer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("customer")
    ] = None
    minimum_payment_due: Annotated[
        MonetaryAmount | PriceSpecification | list[MonetaryAmount | PriceSpecification] | None,
        prop("minimumPaymentDue"),
    ] = None
    payment_due: Annotated[
        _dt.datetime | list[_dt.datetime] | None,
        prop("paymentDue", superseded_by=("paymentDueDate",)),
    ] = None
    payment_due_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("paymentDueDate")
    ] = None
    payment_method: Annotated[
        str | PaymentMethod | list[str | PaymentMethod] | None, prop("paymentMethod")
    ] = None
    payment_method_id: Annotated[str | list[str] | None, prop("paymentMethodId")] = None
    payment_status: Annotated[
        str | PaymentStatusType | list[str | PaymentStatusType] | None, prop("paymentStatus")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    references_order: Annotated[Order | list[Order] | None, prop("referencesOrder")] = None
    scheduled_payment_date: Annotated[
        _dt.date | list[_dt.date] | None, prop("scheduledPaymentDate")
    ] = None
    total_payment_due: Annotated[
        MonetaryAmount | PriceSpecification | list[MonetaryAmount | PriceSpecification] | None,
        prop("totalPaymentDue"),
    ] = None


class ItemList(Intangible):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs.

    https://schema.org/ItemList
    """

    jsonld_type: ClassVar[str] = "ItemList"
    item_list_element: Annotated[
        str
        | ListItem
        | SchemaEnumeration
        | Thing
        | list[str | ListItem | SchemaEnumeration | Thing]
        | None,
        prop("itemListElement"),
    ] = None
    item_list_order: Annotated[
        str | ItemListOrderType | list[str | ItemListOrderType] | None, prop("itemListOrder")
    ] = None
    number_of_items: Annotated[int | list[int] | None, prop("numberOfItems")] = None


class JobPosting(Intangible):
    """A listing that describes a job opening in a certain organization.

    https://schema.org/JobPosting
    """

    jsonld_type: ClassVar[str] = "JobPosting"
    application_contact: Annotated[
        ContactPoint | list[ContactPoint] | None, prop("applicationContact")
    ] = None
    base_salary: Annotated[
        int
        | float
        | MonetaryAmount
        | PriceSpecification
        | list[int | float | MonetaryAmount | PriceSpecification]
        | None,
        prop("baseSalary"),
    ] = None
    benefits: Annotated[
        str | list[str] | None, prop("benefits", superseded_by=("jobBenefits",))
    ] = None
    date_posted: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("datePosted")
    ] = None
    eligibility_to_work_requirement: Annotated[
        str | list[str] | None, prop("eligibilityToWorkRequirement")
    ] = None
    employer_overview: Annotated[str | list[str] | None, prop("employerOverview")] = None
    employment_type: Annotated[str | list[str] | None, prop("employmentType")] = None
    employment_unit: Annotated[Organization | list[Organization] | None, prop("employmentUnit")] = (
        None
    )
    estimated_salary: Annotated[
        int
        | float
        | MonetaryAmount
        | MonetaryAmountDistribution
        | list[int | float | MonetaryAmount | MonetaryAmountDistribution]
        | None,
        prop("estimatedSalary"),
    ] = None
    experience_requirements: Annotated[str | list[str] | None, prop("experienceRequirements")] = (
        None
    )
    hiring_organization: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("hiringOrganization")
    ] = None
    incentive_compensation: Annotated[str | list[str] | None, prop("incentiveCompensation")] = None
    incentives: Annotated[
        str | list[str] | None, prop("incentives", superseded_by=("incentiveCompensation",))
    ] = None
    industry: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("industry")] = None
    job_benefits: Annotated[str | list[str] | None, prop("jobBenefits")] = None
    job_immediate_start: Annotated[bool | list[bool] | None, prop("jobImmediateStart")] = None
    job_location: Annotated[Place | list[Place] | None, prop("jobLocation")] = None
    job_location_type: Annotated[str | list[str] | None, prop("jobLocationType")] = None
    job_start_date: Annotated[
        str | _dt.date | list[str | _dt.date] | None, prop("jobStartDate")
    ] = None
    physical_requirement: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("physicalRequirement")
    ] = None
    relevant_occupation: Annotated[
        Occupation | list[Occupation] | None, prop("relevantOccupation")
    ] = None
    responsibilities: Annotated[str | list[str] | None, prop("responsibilities")] = None
    salary_currency: Annotated[str | list[str] | None, prop("salaryCurrency")] = None
    security_clearance_requirement: Annotated[
        str | list[str] | None, prop("securityClearanceRequirement")
    ] = None
    sensory_requirement: Annotated[
        str | DefinedTerm | list[str | DefinedTerm] | None, prop("sensoryRequirement")
    ] = None
    skills: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("skills")] = None
    special_commitments: Annotated[str | list[str] | None, prop("specialCommitments")] = None
    title: Annotated[str | list[str] | None, prop("title")] = None
    total_job_openings: Annotated[int | list[int] | None, prop("totalJobOpenings")] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None
    work_hours: Annotated[str | list[str] | None, prop("workHours")] = None


class Landform(Place):
    """A landform or physical feature.

    https://schema.org/Landform
    """

    jsonld_type: ClassVar[str] = "Landform"


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    https://schema.org/LandmarksOrHistoricalBuildings
    """

    jsonld_type: ClassVar[str] = "LandmarksOrHistoricalBuildings"


class Language(Intangible):
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in BCP 47 can be used via the alternateName property.

    https://schema.org/Language
    """

    jsonld_type: ClassVar[str] = "Language"


class Legislation(CreativeWork):
    """A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).

    https://schema.org/Legislation
    """

    jsonld_type: ClassVar[str] = "Legislation"
    jurisdiction: Annotated[
        str | AdministrativeArea | list[str | AdministrativeArea] | None, prop("jurisdiction")
    ] = None
    legislation_amends: Annotated[
        Legislation | list[Legislation] | None, prop("legislationAmends")
    ] = None
    legislation_applies: Annotated[
        Legislation | list[Legislation] | None, prop("legislationApplies")
    ] = None
    legislation_changes: Annotated[
        Legislation | list[Legislation] | None, prop("legislationChanges")
    ] = None
    legislation_commences: Annotated[
        Legislation | list[Legislation] | None, prop("legislationCommences")
    ] = None
    legislation_consolidates: Annotated[
        Legislation | list[Legislation] | None, prop("legislationConsolidates")
    ] = None
    legislation_corrects: Annotated[
        Legislation | list[Legislation] | None, prop("legislationCorrects")
    ] = None
    legislation_countersigned_by: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("legislationCountersignedBy"),
    ] = None
    legislation_date: Annotated[_dt.date | list[_dt.date] | None, prop("legislationDate")] = None
    legislation_date_of_applicability: Annotated[
        _dt.date | list[_dt.date] | None, prop("legislationDateOfApplicability")
    ] = None
    legislation_date_version: Annotated[
        _dt.date | list[_dt.date] | None, prop("legislationDateVersion")
    ] = None
    legislation_ensures_implementation_of: Annotated[
        Legislation | list[Legislation] | None, prop("legislationEnsuresImplementationOf")
    ] = None
    legislation_identifier: Annotated[str | list[str] | None, prop("legislationIdentifier")] = None
    legislation_jurisdiction: Annotated[
        str | AdministrativeArea | list[str | AdministrativeArea] | None,
        prop("legislationJurisdiction"),
    ] = None
    legislation_legal_force: Annotated[
        LegalForceStatus | list[LegalForceStatus] | None, prop("legislationLegalForce")
    ] = None
    legislation_passed_by: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("legislationPassedBy")
    ] = None
    legislation_repeals: Annotated[
        Legislation | list[Legislation] | None, prop("legislationRepeals")
    ] = None
    legislation_responsible: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("legislationResponsible")
    ] = None
    legislation_transposes: Annotated[
        Legislation | list[Legislation] | None, prop("legislationTransposes")
    ] = None
    legislation_type: Annotated[
        str | CategoryCode | list[str | CategoryCode] | None, prop("legislationType")
    ] = None


class LibrarySystem(Organization):
    """A LibrarySystem is a collaborative system amongst several libraries.

    https://schema.org/LibrarySystem
    """

    jsonld_type: ClassVar[str] = "LibrarySystem"


class LifestyleModification(MedicalEntity):
    """A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.

    https://schema.org/LifestyleModification
    """

    jsonld_type: ClassVar[str] = "LifestyleModification"


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    https://schema.org/ListItem
    """

    jsonld_type: ClassVar[str] = "ListItem"
    item: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("item")
    ] = None
    next_item: Annotated[ListItem | list[ListItem] | None, prop("nextItem")] = None
    position: Annotated[str | int | list[str | int] | None, prop("position")] = None
    previous_item: Annotated[ListItem | list[ListItem] | None, prop("previousItem")] = None


class LiteraryEvent(Event):
    """Event type: Literary event.

    https://schema.org/LiteraryEvent
    """

    jsonld_type: ClassVar[str] = "LiteraryEvent"


class LocalBusiness(Organization, Place):
    """A particular physical business or branch of an organization.

    https://schema.org/LocalBusiness
    """

    jsonld_type: ClassVar[str] = "LocalBusiness"
    branch_of: Annotated[
        Organization | list[Organization] | None,
        prop("branchOf", superseded_by=("parentOrganization",)),
    ] = None
    currencies_accepted: Annotated[str | list[str] | None, prop("currenciesAccepted")] = None
    floor_level: Annotated[str | list[str] | None, prop("floorLevel")] = None
    opening_hours: Annotated[str | list[str] | None, prop("openingHours")] = None
    payment_accepted: Annotated[str | list[str] | None, prop("paymentAccepted")] = None
    price_range: Annotated[str | list[str] | None, prop("priceRange")] = None


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed.

    https://schema.org/Manuscript
    """

    jsonld_type: ClassVar[str] = "Manuscript"


class Map(CreativeWork):
    """A map.

    https://schema.org/Map
    """

    jsonld_type: ClassVar[str] = "Map"
    map_type: Annotated[MapCategoryType | list[MapCategoryType] | None, prop("mapType")] = None


class MediaObject(CreativeWork):
    """A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload.

    https://schema.org/MediaObject
    """

    jsonld_type: ClassVar[str] = "MediaObject"
    associated_article: Annotated[
        NewsArticle | list[NewsArticle] | None, prop("associatedArticle")
    ] = None
    bitrate: Annotated[str | list[str] | None, prop("bitrate")] = None
    content_size: Annotated[str | list[str] | None, prop("contentSize")] = None
    content_url: Annotated[str | list[str] | None, prop("contentUrl")] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    embed_url: Annotated[str | list[str] | None, prop("embedUrl")] = None
    encodes_creative_work: Annotated[
        CreativeWork | list[CreativeWork] | None, prop("encodesCreativeWork")
    ] = None
    end_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("endTime")
    ] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    ineligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("ineligibleRegion")
    ] = None
    player_type: Annotated[str | list[str] | None, prop("playerType")] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    regions_allowed: Annotated[Place | list[Place] | None, prop("regionsAllowed")] = None
    requires_subscription: Annotated[
        bool | MediaSubscription | list[bool | MediaSubscription] | None,
        prop("requiresSubscription"),
    ] = None
    sha256: Annotated[str | list[str] | None, prop("sha256")] = None
    start_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("startTime")
    ] = None
    upload_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("uploadDate")
    ] = None
    width: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("width")
    ] = None


class MediaReviewItem(CreativeWork):
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation in a MediaReview.

    https://schema.org/MediaReviewItem
    """

    jsonld_type: ClassVar[str] = "MediaReviewItem"
    media_item_appearance: Annotated[
        MediaObject | list[MediaObject] | None, prop("mediaItemAppearance")
    ] = None


class MediaSubscription(Intangible):
    """A subscription which allows a user to access media including audio, video, books, etc.

    https://schema.org/MediaSubscription
    """

    jsonld_type: ClassVar[str] = "MediaSubscription"
    authenticator: Annotated[Organization | list[Organization] | None, prop("authenticator")] = None
    expects_acceptance_of: Annotated[Offer | list[Offer] | None, prop("expectsAcceptanceOf")] = None


class MedicalCause(MedicalEntity):
    """The causative agent(s) that are responsible for the pathophysiologic process that eventually results in a medical condition, symptom or sign.

    https://schema.org/MedicalCause
    """

    jsonld_type: ClassVar[str] = "MedicalCause"
    cause_of: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None, prop("causeOf")
    ] = None


class MedicalCondition(MedicalEntity):
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally.

    https://schema.org/MedicalCondition
    """

    jsonld_type: ClassVar[str] = "MedicalCondition"
    associated_anatomy: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | SuperficialAnatomy
        | list[AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy]
        | None,
        prop("associatedAnatomy"),
    ] = None
    cause: Annotated[MedicalCause | list[MedicalCause] | None, prop("cause")] = None
    differential_diagnosis: Annotated[
        DDxElement | list[DDxElement] | None, prop("differentialDiagnosis")
    ] = None
    drug: Annotated[Drug | list[Drug] | None, prop("drug")] = None
    epidemiology: Annotated[str | list[str] | None, prop("epidemiology")] = None
    expected_prognosis: Annotated[str | list[str] | None, prop("expectedPrognosis")] = None
    natural_progression: Annotated[str | list[str] | None, prop("naturalProgression")] = None
    pathophysiology: Annotated[str | list[str] | None, prop("pathophysiology")] = None
    possible_complication: Annotated[str | list[str] | None, prop("possibleComplication")] = None
    possible_treatment: Annotated[
        Drug
        | DrugClass
        | LifestyleModification
        | MedicalTherapy
        | list[Drug | DrugClass | LifestyleModification | MedicalTherapy]
        | None,
        prop("possibleTreatment"),
    ] = None
    primary_prevention: Annotated[
        MedicalTherapy | list[MedicalTherapy] | None, prop("primaryPrevention")
    ] = None
    risk_factor: Annotated[
        MedicalRiskFactor | list[MedicalRiskFactor] | None, prop("riskFactor")
    ] = None
    secondary_prevention: Annotated[
        Drug
        | DrugClass
        | LifestyleModification
        | MedicalTherapy
        | list[Drug | DrugClass | LifestyleModification | MedicalTherapy]
        | None,
        prop("secondaryPrevention"),
    ] = None
    sign_or_symptom: Annotated[
        MedicalSignOrSymptom | list[MedicalSignOrSymptom] | None, prop("signOrSymptom")
    ] = None
    stage: Annotated[MedicalConditionStage | list[MedicalConditionStage] | None, prop("stage")] = (
        None
    )
    status: Annotated[
        str
        | EventStatusType
        | MedicalStudyStatus
        | list[str | EventStatusType | MedicalStudyStatus]
        | None,
        prop("status"),
    ] = None
    typical_test: Annotated[MedicalTest | list[MedicalTest] | None, prop("typicalTest")] = None


class MedicalContraindication(MedicalEntity):
    """A condition or factor that serves as a reason to withhold a certain medical therapy.

    https://schema.org/MedicalContraindication
    """

    jsonld_type: ClassVar[str] = "MedicalContraindication"


class MedicalDevice(MedicalEntity):
    """Any object used in a medical capacity, such as to diagnose or treat a patient.

    https://schema.org/MedicalDevice
    """

    jsonld_type: ClassVar[str] = "MedicalDevice"
    adverse_outcome: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("adverseOutcome"),
    ] = None
    contraindication: Annotated[
        str | MedicalContraindication | list[str | MedicalContraindication] | None,
        prop("contraindication"),
    ] = None
    post_op: Annotated[str | list[str] | None, prop("postOp")] = None
    pre_op: Annotated[str | list[str] | None, prop("preOp")] = None
    procedure: Annotated[str | list[str] | None, prop("procedure")] = None
    serious_adverse_outcome: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("seriousAdverseOutcome"),
    ] = None


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition.

    https://schema.org/MedicalGuideline
    """

    jsonld_type: ClassVar[str] = "MedicalGuideline"
    evidence_level: Annotated[
        MedicalEvidenceLevel | list[MedicalEvidenceLevel] | None, prop("evidenceLevel")
    ] = None
    evidence_origin: Annotated[str | list[str] | None, prop("evidenceOrigin")] = None
    guideline_date: Annotated[_dt.date | list[_dt.date] | None, prop("guidelineDate")] = None
    guideline_subject: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("guidelineSubject"),
    ] = None


class MedicalIndication(MedicalEntity):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.

    https://schema.org/MedicalIndication
    """

    jsonld_type: ClassVar[str] = "MedicalIndication"


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.

    https://schema.org/MedicalIntangible
    """

    jsonld_type: ClassVar[str] = "MedicalIntangible"


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic.

    https://schema.org/MedicalOrganization
    """

    jsonld_type: ClassVar[str] = "MedicalOrganization"
    medical_specialty: Annotated[
        MedicalSpecialty | list[MedicalSpecialty] | None, prop("medicalSpecialty")
    ] = None


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.

    https://schema.org/MedicalProcedure
    """

    jsonld_type: ClassVar[str] = "MedicalProcedure"
    body_location: Annotated[str | list[str] | None, prop("bodyLocation")] = None
    followup: Annotated[str | list[str] | None, prop("followup")] = None
    how_performed: Annotated[str | list[str] | None, prop("howPerformed")] = None
    preparation: Annotated[
        str | MedicalEntity | PhysicalExam | list[str | MedicalEntity | PhysicalExam] | None,
        prop("preparation"),
    ] = None
    procedure_type: Annotated[
        MedicalProcedureType | list[MedicalProcedureType] | None, prop("procedureType")
    ] = None
    status: Annotated[
        str
        | EventStatusType
        | MedicalStudyStatus
        | list[str | EventStatusType | MedicalStudyStatus]
        | None,
        prop("status"),
    ] = None


class MedicalRiskEstimator(MedicalEntity):
    """Any rule set or interactive tool for estimating the risk of developing a complication or condition.

    https://schema.org/MedicalRiskEstimator
    """

    jsonld_type: ClassVar[str] = "MedicalRiskEstimator"
    estimates_risk_of: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("estimatesRiskOf"),
    ] = None
    included_risk_factor: Annotated[
        MedicalRiskFactor | list[MedicalRiskFactor] | None, prop("includedRiskFactor")
    ] = None


class MedicalRiskFactor(MedicalEntity):
    """A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.

    https://schema.org/MedicalRiskFactor
    """

    jsonld_type: ClassVar[str] = "MedicalRiskFactor"
    increases_risk_of: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("increasesRiskOf"),
    ] = None


class MedicalStudy(MedicalEntity):
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not.

    https://schema.org/MedicalStudy
    """

    jsonld_type: ClassVar[str] = "MedicalStudy"
    health_condition: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("healthCondition")
    ] = None
    sponsor: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("sponsor")
    ] = None
    status: Annotated[
        str
        | EventStatusType
        | MedicalStudyStatus
        | list[str | EventStatusType | MedicalStudyStatus]
        | None,
        prop("status"),
    ] = None
    study_location: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("studyLocation")
    ] = None
    study_subject: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("studySubject"),
    ] = None


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes.

    https://schema.org/MedicalTest
    """

    jsonld_type: ClassVar[str] = "MedicalTest"
    affected_by: Annotated[Drug | list[Drug] | None, prop("affectedBy")] = None
    normal_range: Annotated[
        str
        | MedicalEnumeration
        | SchemaEnumeration
        | list[str | MedicalEnumeration | SchemaEnumeration]
        | None,
        prop("normalRange"),
    ] = None
    sign_detected: Annotated[MedicalSign | list[MedicalSign] | None, prop("signDetected")] = None
    used_to_diagnose: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("usedToDiagnose")
    ] = None
    uses_device: Annotated[MedicalDevice | list[MedicalDevice] | None, prop("usesDevice")] = None


class MemberProgram(Intangible):
    """A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points.

    https://schema.org/MemberProgram
    """

    jsonld_type: ClassVar[str] = "MemberProgram"
    has_tiers: Annotated[MemberProgramTier | list[MemberProgramTier] | None, prop("hasTiers")] = (
        None
    )
    hosting_organization: Annotated[
        Organization | list[Organization] | None, prop("hostingOrganization")
    ] = None


class MemberProgramTier(Intangible):
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".

    https://schema.org/MemberProgramTier
    """

    jsonld_type: ClassVar[str] = "MemberProgramTier"
    has_tier_benefit: Annotated[
        TierBenefitEnumeration | list[TierBenefitEnumeration] | None, prop("hasTierBenefit")
    ] = None
    has_tier_requirement: Annotated[
        str
        | CreditCard
        | MonetaryAmount
        | UnitPriceSpecification
        | list[str | CreditCard | MonetaryAmount | UnitPriceSpecification]
        | None,
        prop("hasTierRequirement"),
    ] = None
    is_tier_of: Annotated[MemberProgram | list[MemberProgram] | None, prop("isTierOf")] = None
    membership_points_earned: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("membershipPointsEarned"),
    ] = None


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment.

    https://schema.org/Menu
    """

    jsonld_type: ClassVar[str] = "Menu"
    has_menu_item: Annotated[MenuItem | list[MenuItem] | None, prop("hasMenuItem")] = None
    has_menu_section: Annotated[MenuSection | list[MenuSection] | None, prop("hasMenuSection")] = (
        None
    )


class MenuItem(Intangible):
    """A food or drink item listed in a menu or menu section.

    https://schema.org/MenuItem
    """

    jsonld_type: ClassVar[str] = "MenuItem"
    menu_add_on: Annotated[
        MenuItem | MenuSection | list[MenuItem | MenuSection] | None, prop("menuAddOn")
    ] = None
    nutrition: Annotated[
        NutritionInformation | list[NutritionInformation] | None, prop("nutrition")
    ] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    suitable_for_diet: Annotated[
        Diet | RestrictedDiet | list[Diet | RestrictedDiet] | None, prop("suitableForDiet")
    ] = None


class MenuSection(CreativeWork):
    """A sub-grouping of food or drink items in a menu.

    https://schema.org/MenuSection
    """

    jsonld_type: ClassVar[str] = "MenuSection"
    has_menu_item: Annotated[MenuItem | list[MenuItem] | None, prop("hasMenuItem")] = None
    has_menu_section: Annotated[MenuSection | list[MenuSection] | None, prop("hasMenuSection")] = (
        None
    )


class MerchantReturnPolicy(Intangible):
    """A MerchantReturnPolicy provides information about product return policies associated with an Organization, Product, or Offer.

    https://schema.org/MerchantReturnPolicy
    """

    jsonld_type: ClassVar[str] = "MerchantReturnPolicy"
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    applicable_country: Annotated[
        str | Country | list[str | Country] | None, prop("applicableCountry")
    ] = None
    customer_remorse_return_fees: Annotated[
        ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None,
        prop("customerRemorseReturnFees"),
    ] = None
    customer_remorse_return_label_source: Annotated[
        ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None,
        prop("customerRemorseReturnLabelSource"),
    ] = None
    customer_remorse_return_shipping_fees_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None,
        prop("customerRemorseReturnShippingFeesAmount"),
    ] = None
    in_store_returns_offered: Annotated[bool | list[bool] | None, prop("inStoreReturnsOffered")] = (
        None
    )
    item_condition: Annotated[
        OfferItemCondition | list[OfferItemCondition] | None, prop("itemCondition")
    ] = None
    item_defect_return_fees: Annotated[
        ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None, prop("itemDefectReturnFees")
    ] = None
    item_defect_return_label_source: Annotated[
        ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None,
        prop("itemDefectReturnLabelSource"),
    ] = None
    item_defect_return_shipping_fees_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("itemDefectReturnShippingFeesAmount")
    ] = None
    merchant_return_days: Annotated[
        int | _dt.date | _dt.datetime | list[int | _dt.date | _dt.datetime] | None,
        prop("merchantReturnDays"),
    ] = None
    merchant_return_link: Annotated[str | list[str] | None, prop("merchantReturnLink")] = None
    refund_type: Annotated[
        RefundTypeEnumeration | list[RefundTypeEnumeration] | None, prop("refundType")
    ] = None
    restocking_fee: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None,
        prop("restockingFee"),
    ] = None
    return_fees: Annotated[
        ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None, prop("returnFees")
    ] = None
    return_label_source: Annotated[
        ReturnLabelSourceEnumeration | list[ReturnLabelSourceEnumeration] | None,
        prop("returnLabelSource"),
    ] = None
    return_method: Annotated[
        ReturnMethodEnumeration | list[ReturnMethodEnumeration] | None, prop("returnMethod")
    ] = None
    return_policy_category: Annotated[
        MerchantReturnEnumeration | list[MerchantReturnEnumeration] | None,
        prop("returnPolicyCategory"),
    ] = None
    return_policy_country: Annotated[
        str | Country | list[str | Country] | None, prop("returnPolicyCountry")
    ] = None
    return_policy_seasonal_override: Annotated[
        MerchantReturnPolicySeasonalOverride | list[MerchantReturnPolicySeasonalOverride] | None,
        prop("returnPolicySeasonalOverride"),
    ] = None
    return_shipping_fees_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("returnShippingFeesAmount")
    ] = None
    valid_for_member_tier: Annotated[
        MemberProgramTier | list[MemberProgramTier] | None, prop("validForMemberTier")
    ] = None


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    https://schema.org/MerchantReturnPolicySeasonalOverride
    """

    jsonld_type: ClassVar[str] = "MerchantReturnPolicySeasonalOverride"
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    merchant_return_days: Annotated[
        int | _dt.date | _dt.datetime | list[int | _dt.date | _dt.datetime] | None,
        prop("merchantReturnDays"),
    ] = None
    refund_type: Annotated[
        RefundTypeEnumeration | list[RefundTypeEnumeration] | None, prop("refundType")
    ] = None
    restocking_fee: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None,
        prop("restockingFee"),
    ] = None
    return_fees: Annotated[
        ReturnFeesEnumeration | list[ReturnFeesEnumeration] | None, prop("returnFees")
    ] = None
    return_method: Annotated[
        ReturnMethodEnumeration | list[ReturnMethodEnumeration] | None, prop("returnMethod")
    ] = None
    return_policy_category: Annotated[
        MerchantReturnEnumeration | list[MerchantReturnEnumeration] | None,
        prop("returnPolicyCategory"),
    ] = None
    return_shipping_fees_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("returnShippingFeesAmount")
    ] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    https://schema.org/Message
    """

    jsonld_type: ClassVar[str] = "Message"
    bcc_recipient: Annotated[
        ContactPoint | Organization | Person | list[ContactPoint | Organization | Person] | None,
        prop("bccRecipient"),
    ] = None
    cc_recipient: Annotated[
        ContactPoint | Organization | Person | list[ContactPoint | Organization | Person] | None,
        prop("ccRecipient"),
    ] = None
    date_read: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateRead")
    ] = None
    date_received: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("dateReceived")] = None
    date_sent: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("dateSent")] = None
    message_attachment: Annotated[
        CreativeWork | list[CreativeWork] | None, prop("messageAttachment")
    ] = None
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None
    sender: Annotated[
        Audience | Organization | Person | list[Audience | Organization | Person] | None,
        prop("sender"),
    ] = None
    to_recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("toRecipient"),
    ] = None


class MoveAction(Action):
    """The act of an agent relocating to a place.\\n\\nRelated actions:\\n\\n* TransferAction: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.

    https://schema.org/MoveAction
    """

    jsonld_type: ClassVar[str] = "MoveAction"
    from_location: Annotated[Place | list[Place] | None, prop("fromLocation")] = None
    to_location: Annotated[Place | list[Place] | None, prop("toLocation")] = None


class Movie(CreativeWork):
    """A movie.

    https://schema.org/Movie
    """

    jsonld_type: ClassVar[str] = "Movie"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    subtitle_language: Annotated[
        str | Language | list[str | Language] | None, prop("subtitleLanguage")
    ] = None
    title_eidr: Annotated[str | list[str] | None, prop("titleEIDR")] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class MusicComposition(CreativeWork):
    """A musical composition.

    https://schema.org/MusicComposition
    """

    jsonld_type: ClassVar[str] = "MusicComposition"
    composer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("composer")
    ] = None
    first_performance: Annotated[Event | list[Event] | None, prop("firstPerformance")] = None
    included_composition: Annotated[
        MusicComposition | list[MusicComposition] | None, prop("includedComposition")
    ] = None
    iswc_code: Annotated[str | list[str] | None, prop("iswcCode")] = None
    lyricist: Annotated[Person | list[Person] | None, prop("lyricist")] = None
    lyrics: Annotated[CreativeWork | list[CreativeWork] | None, prop("lyrics")] = None
    music_arrangement: Annotated[
        MusicComposition | list[MusicComposition] | None, prop("musicArrangement")
    ] = None
    music_composition_form: Annotated[str | list[str] | None, prop("musicCompositionForm")] = None
    musical_key: Annotated[str | list[str] | None, prop("musicalKey")] = None
    recorded_as: Annotated[MusicRecording | list[MusicRecording] | None, prop("recordedAs")] = None


class MusicEvent(Event):
    """Event type: Music event.

    https://schema.org/MusicEvent
    """

    jsonld_type: ClassVar[str] = "MusicEvent"


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form.

    https://schema.org/MusicPlaylist
    """

    jsonld_type: ClassVar[str] = "MusicPlaylist"
    num_tracks: Annotated[int | list[int] | None, prop("numTracks")] = None
    track: Annotated[
        ItemList | MusicRecording | list[ItemList | MusicRecording] | None, prop("track")
    ] = None
    tracks: Annotated[
        MusicRecording | list[MusicRecording] | None, prop("tracks", superseded_by=("track",))
    ] = None


class MusicRecording(CreativeWork):
    """A music recording (track), usually a single song.

    https://schema.org/MusicRecording
    """

    jsonld_type: ClassVar[str] = "MusicRecording"
    by_artist: Annotated[
        MusicGroup | Person | list[MusicGroup | Person] | None, prop("byArtist")
    ] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    in_album: Annotated[MusicAlbum | list[MusicAlbum] | None, prop("inAlbum")] = None
    in_playlist: Annotated[MusicPlaylist | list[MusicPlaylist] | None, prop("inPlaylist")] = None
    isrc_code: Annotated[str | list[str] | None, prop("isrcCode")] = None
    recording_of: Annotated[
        MusicComposition | list[MusicComposition] | None, prop("recordingOf")
    ] = None


class NGO(Organization):
    """Organization: Non-governmental Organization.

    https://schema.org/NGO
    """

    jsonld_type: ClassVar[str] = "NGO"


class NewsMediaOrganization(Organization):
    """A News/Media organization such as a newspaper or TV station.

    https://schema.org/NewsMediaOrganization
    """

    jsonld_type: ClassVar[str] = "NewsMediaOrganization"
    masthead: Annotated[str | CreativeWork | list[str | CreativeWork] | None, prop("masthead")] = (
        None
    )
    mission_coverage_priorities_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None,
        prop("missionCoveragePrioritiesPolicy"),
    ] = None
    no_bylines_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("noBylinesPolicy")
    ] = None
    verification_fact_checking_policy: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("verificationFactCheckingPolicy")
    ] = None


class Occupation(Intangible):
    """A profession, may involve prolonged training and/or a formal qualification.

    https://schema.org/Occupation
    """

    jsonld_type: ClassVar[str] = "Occupation"
    estimated_salary: Annotated[
        int
        | float
        | MonetaryAmount
        | MonetaryAmountDistribution
        | list[int | float | MonetaryAmount | MonetaryAmountDistribution]
        | None,
        prop("estimatedSalary"),
    ] = None
    experience_requirements: Annotated[str | list[str] | None, prop("experienceRequirements")] = (
        None
    )
    occupation_location: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("occupationLocation")
    ] = None
    responsibilities: Annotated[str | list[str] | None, prop("responsibilities")] = None
    skills: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("skills")] = None


class Offer(Intangible):
    """An offer to transfer some rights to an item or to provide a service, for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.\\n\\nNote...

    https://schema.org/Offer
    """

    jsonld_type: ClassVar[str] = "Offer"
    accepted_payment_method: Annotated[
        str | LoanOrCredit | PaymentMethod | list[str | LoanOrCredit | PaymentMethod] | None,
        prop("acceptedPaymentMethod"),
    ] = None
    add_on: Annotated[Offer | list[Offer] | None, prop("addOn")] = None
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    advance_booking_requirement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("advanceBookingRequirement")
    ] = None
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    availability: Annotated[
        ItemAvailability | list[ItemAvailability] | None, prop("availability")
    ] = None
    availability_ends: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityEnds"),
    ] = None
    availability_starts: Annotated[
        _dt.date | _dt.datetime | _dt.time | list[_dt.date | _dt.datetime | _dt.time] | None,
        prop("availabilityStarts"),
    ] = None
    available_at_or_from: Annotated[Place | list[Place] | None, prop("availableAtOrFrom")] = None
    available_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("availableDeliveryMethod")
    ] = None
    business_function: Annotated[
        BusinessFunction | list[BusinessFunction] | None, prop("businessFunction")
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    checkout_page_url_template: Annotated[
        str | list[str] | None, prop("checkoutPageURLTemplate")
    ] = None
    delivery_lead_time: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("deliveryLeadTime")
    ] = None
    eligible_customer_type: Annotated[
        BusinessEntityType | list[BusinessEntityType] | None, prop("eligibleCustomerType")
    ] = None
    eligible_duration: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("eligibleDuration")
    ] = None
    eligible_quantity: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("eligibleQuantity")
    ] = None
    eligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("eligibleRegion")
    ] = None
    eligible_transaction_volume: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("eligibleTransactionVolume")
    ] = None
    gtin12: Annotated[str | list[str] | None, prop("gtin12")] = None
    gtin13: Annotated[str | list[str] | None, prop("gtin13")] = None
    gtin14: Annotated[str | list[str] | None, prop("gtin14")] = None
    gtin8: Annotated[str | list[str] | None, prop("gtin8")] = None
    has_gs1_digital_link: Annotated[str | list[str] | None, prop("hasGS1DigitalLink")] = None
    has_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("hasMeasurement")
    ] = None
    has_merchant_return_policy: Annotated[
        MerchantReturnPolicy | list[MerchantReturnPolicy] | None, prop("hasMerchantReturnPolicy")
    ] = None
    includes_object: Annotated[
        TypeAndQuantityNode | list[TypeAndQuantityNode] | None, prop("includesObject")
    ] = None
    ineligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("ineligibleRegion")
    ] = None
    inventory_level: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("inventoryLevel")
    ] = None
    is_family_friendly: Annotated[bool | list[bool] | None, prop("isFamilyFriendly")] = None
    item_condition: Annotated[
        OfferItemCondition | list[OfferItemCondition] | None, prop("itemCondition")
    ] = None
    item_offered: Annotated[
        AggregateOffer
        | CreativeWork
        | Event
        | MenuItem
        | Product
        | Service
        | Trip
        | list[AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip]
        | None,
        prop("itemOffered"),
    ] = None
    lease_length: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("leaseLength")
    ] = None
    mpn: Annotated[str | list[str] | None, prop("mpn")] = None
    offered_by: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("offeredBy")
    ] = None
    price: Annotated[str | int | float | list[str | int | float] | None, prop("price")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    price_specification: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("priceSpecification")
    ] = None
    price_valid_until: Annotated[_dt.date | list[_dt.date] | None, prop("priceValidUntil")] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    reviews: Annotated[Review | list[Review] | None, prop("reviews", superseded_by=("review",))] = (
        None
    )
    seller: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("seller")
    ] = None
    serial_number: Annotated[str | list[str] | None, prop("serialNumber")] = None
    shipping_details: Annotated[
        OfferShippingDetails | list[OfferShippingDetails] | None, prop("shippingDetails")
    ] = None
    sku: Annotated[str | list[str] | None, prop("sku")] = None
    valid_for_member_tier: Annotated[
        MemberProgramTier | list[MemberProgramTier] | None, prop("validForMemberTier")
    ] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None
    warranty: Annotated[WarrantyPromise | list[WarrantyPromise] | None, prop("warranty")] = None


class OnlineBusiness(Organization):
    """A particular online business, either standalone or the online part of a broader organization.

    https://schema.org/OnlineBusiness
    """

    jsonld_type: ClassVar[str] = "OnlineBusiness"


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

    https://schema.org/Order
    """

    jsonld_type: ClassVar[str] = "Order"
    accepted_offer: Annotated[Offer | list[Offer] | None, prop("acceptedOffer")] = None
    billing_address: Annotated[
        PostalAddress | list[PostalAddress] | None, prop("billingAddress")
    ] = None
    broker: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("broker")
    ] = None
    confirmation_number: Annotated[str | list[str] | None, prop("confirmationNumber")] = None
    customer: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("customer")
    ] = None
    discount: Annotated[str | int | float | list[str | int | float] | None, prop("discount")] = None
    discount_code: Annotated[str | list[str] | None, prop("discountCode")] = None
    discount_currency: Annotated[str | list[str] | None, prop("discountCurrency")] = None
    is_gift: Annotated[bool | list[bool] | None, prop("isGift")] = None
    merchant: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("merchant", superseded_by=("seller",)),
    ] = None
    order_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("orderDate")
    ] = None
    order_delivery: Annotated[
        ParcelDelivery | list[ParcelDelivery] | None, prop("orderDelivery")
    ] = None
    order_number: Annotated[str | list[str] | None, prop("orderNumber")] = None
    order_status: Annotated[OrderStatus | list[OrderStatus] | None, prop("orderStatus")] = None
    ordered_item: Annotated[
        OrderItem | Product | Service | list[OrderItem | Product | Service] | None,
        prop("orderedItem"),
    ] = None
    part_of_invoice: Annotated[Invoice | list[Invoice] | None, prop("partOfInvoice")] = None
    payment_due: Annotated[
        _dt.datetime | list[_dt.datetime] | None,
        prop("paymentDue", superseded_by=("paymentDueDate",)),
    ] = None
    payment_due_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("paymentDueDate")
    ] = None
    payment_method: Annotated[
        str | PaymentMethod | list[str | PaymentMethod] | None, prop("paymentMethod")
    ] = None
    payment_method_id: Annotated[str | list[str] | None, prop("paymentMethodId")] = None
    payment_url: Annotated[str | list[str] | None, prop("paymentUrl")] = None
    seller: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("seller")
    ] = None


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects.

    https://schema.org/OrganizeAction
    """

    jsonld_type: ClassVar[str] = "OrganizeAction"


class Painting(CreativeWork):
    """A painting.

    https://schema.org/Painting
    """

    jsonld_type: ClassVar[str] = "Painting"


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    https://schema.org/ParcelDelivery
    """

    jsonld_type: ClassVar[str] = "ParcelDelivery"
    carrier: Annotated[
        Organization | list[Organization] | None, prop("carrier", superseded_by=("provider",))
    ] = None
    delivery_address: Annotated[
        PostalAddress | list[PostalAddress] | None, prop("deliveryAddress")
    ] = None
    delivery_status: Annotated[
        DeliveryEvent | list[DeliveryEvent] | None, prop("deliveryStatus")
    ] = None
    expected_arrival_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("expectedArrivalFrom")
    ] = None
    expected_arrival_until: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("expectedArrivalUntil")
    ] = None
    has_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("hasDeliveryMethod")
    ] = None
    item_shipped: Annotated[Product | list[Product] | None, prop("itemShipped")] = None
    origin_address: Annotated[PostalAddress | list[PostalAddress] | None, prop("originAddress")] = (
        None
    )
    part_of_order: Annotated[Order | list[Order] | None, prop("partOfOrder")] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    tracking_number: Annotated[str | list[str] | None, prop("trackingNumber")] = None
    tracking_url: Annotated[str | list[str] | None, prop("trackingUrl")] = None


class PaymentMethod(Intangible):
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase.

    https://schema.org/PaymentMethod
    """

    jsonld_type: ClassVar[str] = "PaymentMethod"
    payment_method_type: Annotated[
        PaymentMethodType | list[PaymentMethodType] | None, prop("paymentMethodType")
    ] = None


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus.

    https://schema.org/PerformingGroup
    """

    jsonld_type: ClassVar[str] = "PerformingGroup"


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    https://schema.org/Permit
    """

    jsonld_type: ClassVar[str] = "Permit"
    issued_by: Annotated[Organization | list[Organization] | None, prop("issuedBy")] = None
    issued_through: Annotated[Service | list[Service] | None, prop("issuedThrough")] = None
    permit_audience: Annotated[Audience | list[Audience] | None, prop("permitAudience")] = None
    valid_for: Annotated[str | list[str] | None, prop("validFor")] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_in: Annotated[AdministrativeArea | list[AdministrativeArea] | None, prop("validIn")] = (
        None
    )
    valid_until: Annotated[_dt.date | list[_dt.date] | None, prop("validUntil")] = None


class Photograph(CreativeWork):
    """A photograph.

    https://schema.org/Photograph
    """

    jsonld_type: ClassVar[str] = "Photograph"


class Play(CreativeWork):
    """A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading.

    https://schema.org/Play
    """

    jsonld_type: ClassVar[str] = "Play"


class PlayAction(Action):
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation, competition or exercise.\\n\\nRelated actions:\\n\\n* ListenAction: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for...

    https://schema.org/PlayAction
    """

    jsonld_type: ClassVar[str] = "PlayAction"
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    event: Annotated[Event | list[Event] | None, prop("event")] = None


class PoliticalParty(Organization):
    """Organization: Political Party.

    https://schema.org/PoliticalParty
    """

    jsonld_type: ClassVar[str] = "PoliticalParty"


class Poster(CreativeWork):
    """A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.

    https://schema.org/Poster
    """

    jsonld_type: ClassVar[str] = "Poster"


class ProductGroup(Product):
    """A ProductGroup represents a group of Products that vary only in certain well-described ways, such as by size, color, material etc. While a ProductGroup itself is not directly offered for sale, the various varying products that it represe...

    https://schema.org/ProductGroup
    """

    jsonld_type: ClassVar[str] = "ProductGroup"
    has_variant: Annotated[Product | list[Product] | None, prop("hasVariant")] = None
    product_group_id: Annotated[str | list[str] | None, prop("productGroupID")] = None
    varies_by: Annotated[
        str | DefinedTerm | PropertyValue | list[str | DefinedTerm | PropertyValue] | None,
        prop("variesBy"),
    ] = None


class ProductModel(Product):
    """A datasheet or vendor specification of a product (in the sense of a prototypical description).

    https://schema.org/ProductModel
    """

    jsonld_type: ClassVar[str] = "ProductModel"
    predecessor_of: Annotated[ProductModel | list[ProductModel] | None, prop("predecessorOf")] = (
        None
    )
    successor_of: Annotated[ProductModel | list[ProductModel] | None, prop("successorOf")] = None


class ProductReturnPolicy(Intangible):
    """A ProductReturnPolicy provides information about product return policies associated with an Organization or Product.

    https://schema.org/ProductReturnPolicy

    Deprecated: superseded by MerchantReturnPolicy.
    """

    jsonld_type: ClassVar[str] = "ProductReturnPolicy"
    product_return_days: Annotated[
        int | list[int] | None, prop("productReturnDays", superseded_by=("merchantReturnDays",))
    ] = None
    product_return_link: Annotated[
        str | list[str] | None, prop("productReturnLink", superseded_by=("merchantReturnLink",))
    ] = None


class ProgramMembership(Intangible):
    """Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

    https://schema.org/ProgramMembership
    """

    jsonld_type: ClassVar[str] = "ProgramMembership"
    hosting_organization: Annotated[
        Organization | list[Organization] | None, prop("hostingOrganization")
    ] = None
    member: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("member")
    ] = None
    members: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("members", superseded_by=("member",)),
    ] = None
    membership_number: Annotated[str | list[str] | None, prop("membershipNumber")] = None
    membership_points_earned: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("membershipPointsEarned"),
    ] = None
    program: Annotated[MemberProgram | list[MemberProgram] | None, prop("program")] = None
    program_name: Annotated[str | list[str] | None, prop("programName")] = None


class Project(Organization):
    """An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.

    https://schema.org/Project
    """

    jsonld_type: ClassVar[str] = "Project"


class PropertyValueSpecification(Intangible):
    """A Property value specification.

    https://schema.org/PropertyValueSpecification
    """

    jsonld_type: ClassVar[str] = "PropertyValueSpecification"
    default_value: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("defaultValue"),
    ] = None
    max_value: Annotated[int | float | list[int | float] | None, prop("maxValue")] = None
    min_value: Annotated[int | float | list[int | float] | None, prop("minValue")] = None
    multiple_values: Annotated[bool | list[bool] | None, prop("multipleValues")] = None
    readonly_value: Annotated[bool | list[bool] | None, prop("readonlyValue")] = None
    step_value: Annotated[int | float | list[int | float] | None, prop("stepValue")] = None
    value_max_length: Annotated[int | float | list[int | float] | None, prop("valueMaxLength")] = (
        None
    )
    value_min_length: Annotated[int | float | list[int | float] | None, prop("valueMinLength")] = (
        None
    )
    value_name: Annotated[str | list[str] | None, prop("valueName")] = None
    value_pattern: Annotated[str | list[str] | None, prop("valuePattern")] = None
    value_required: Annotated[bool | list[bool] | None, prop("valueRequired")] = None


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.

    https://schema.org/PublicationEvent
    """

    jsonld_type: ClassVar[str] = "PublicationEvent"
    free: Annotated[
        bool | list[bool] | None, prop("free", superseded_by=("isAccessibleForFree",))
    ] = None
    published_by: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("publishedBy")
    ] = None
    published_on: Annotated[
        BroadcastService | list[BroadcastService] | None, prop("publishedOn")
    ] = None


class PublicationIssue(CreativeWork):
    """A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.\\n\\nSee also blog post.

    https://schema.org/PublicationIssue
    """

    jsonld_type: ClassVar[str] = "PublicationIssue"
    issue_number: Annotated[str | int | list[str | int] | None, prop("issueNumber")] = None
    page_end: Annotated[str | int | list[str | int] | None, prop("pageEnd")] = None
    page_start: Annotated[str | int | list[str | int] | None, prop("pageStart")] = None
    pagination: Annotated[str | list[str] | None, prop("pagination")] = None


class PublicationVolume(CreativeWork):
    """A part of a successively published publication such as a periodical or multi-volume work, often numbered.

    https://schema.org/PublicationVolume
    """

    jsonld_type: ClassVar[str] = "PublicationVolume"
    page_end: Annotated[str | int | list[str | int] | None, prop("pageEnd")] = None
    page_start: Annotated[str | int | list[str | int] | None, prop("pageStart")] = None
    pagination: Annotated[str | list[str] | None, prop("pagination")] = None
    volume_number: Annotated[str | int | list[str | int] | None, prop("volumeNumber")] = None


class Rating(Intangible):
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

    https://schema.org/Rating
    """

    jsonld_type: ClassVar[str] = "Rating"
    author: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("author")
    ] = None
    best_rating: Annotated[
        str | int | float | list[str | int | float] | None, prop("bestRating")
    ] = None
    rating_explanation: Annotated[str | list[str] | None, prop("ratingExplanation")] = None
    rating_value: Annotated[
        str | int | float | list[str | int | float] | None, prop("ratingValue")
    ] = None
    review_aspect: Annotated[
        str | StructuredValue | list[str | StructuredValue] | None, prop("reviewAspect")
    ] = None
    worst_rating: Annotated[
        str | int | float | list[str | int | float] | None, prop("worstRating")
    ] = None


class Reservation(Intangible):
    """Describes a reservation for travel, dining or an event.

    https://schema.org/Reservation
    """

    jsonld_type: ClassVar[str] = "Reservation"
    booking_agent: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("bookingAgent", superseded_by=("broker",)),
    ] = None
    booking_time: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("bookingTime")] = None
    broker: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("broker")
    ] = None
    modified_time: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("modifiedTime")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    program_membership_used: Annotated[
        ProgramMembership | list[ProgramMembership] | None, prop("programMembershipUsed")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    reservation_for: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("reservationFor")
    ] = None
    reservation_id: Annotated[str | list[str] | None, prop("reservationId")] = None
    reservation_status: Annotated[
        ReservationStatusType | list[ReservationStatusType] | None, prop("reservationStatus")
    ] = None
    reserved_ticket: Annotated[Ticket | list[Ticket] | None, prop("reservedTicket")] = None
    total_price: Annotated[
        str
        | int
        | float
        | PriceSpecification
        | list[str | int | float | PriceSpecification]
        | None,
        prop("totalPrice"),
    ] = None
    under_name: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("underName")
    ] = None


class Residence(Place):
    """The place where a person lives.

    https://schema.org/Residence
    """

    jsonld_type: ClassVar[str] = "Residence"
    accommodation_floor_plan: Annotated[
        FloorPlan | list[FloorPlan] | None, prop("accommodationFloorPlan")
    ] = None
    floor_level: Annotated[str | list[str] | None, prop("floorLevel")] = None


class Review(CreativeWork):
    """A review of an item - for example, of a restaurant, movie, or store.

    https://schema.org/Review
    """

    jsonld_type: ClassVar[str] = "Review"
    associated_claim_review: Annotated[
        Review | list[Review] | None, prop("associatedClaimReview")
    ] = None
    associated_media_review: Annotated[
        Review | list[Review] | None, prop("associatedMediaReview")
    ] = None
    associated_review: Annotated[Review | list[Review] | None, prop("associatedReview")] = None
    item_reviewed: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("itemReviewed")
    ] = None
    negative_notes: Annotated[
        str | ItemList | ListItem | list[str | ItemList | ListItem] | None, prop("negativeNotes")
    ] = None
    positive_notes: Annotated[
        str | ItemList | ListItem | list[str | ItemList | ListItem] | None, prop("positiveNotes")
    ] = None
    review_aspect: Annotated[
        str | StructuredValue | list[str | StructuredValue] | None, prop("reviewAspect")
    ] = None
    review_body: Annotated[str | list[str] | None, prop("reviewBody")] = None
    review_rating: Annotated[Rating | list[Rating] | None, prop("reviewRating")] = None


class Role(Intangible):
    """Represents additional information about a relationship or property.

    https://schema.org/Role
    """

    jsonld_type: ClassVar[str] = "Role"
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    named_position: Annotated[
        str | list[str] | None, prop("namedPosition", superseded_by=("roleName",))
    ] = None
    role_name: Annotated[str | list[str] | None, prop("roleName")] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None


class SaleEvent(Event):
    """Event type: Sales event.

    https://schema.org/SaleEvent
    """

    jsonld_type: ClassVar[str] = "SaleEvent"


class Schedule(Intangible):
    """A schedule defines a repeating time period used to describe a regularly occurring Event.

    https://schema.org/Schedule
    """

    jsonld_type: ClassVar[str] = "Schedule"
    by_day: Annotated[str | DayOfWeek | list[str | DayOfWeek] | None, prop("byDay")] = None
    by_month: Annotated[int | list[int] | None, prop("byMonth")] = None
    by_month_day: Annotated[int | list[int] | None, prop("byMonthDay")] = None
    by_month_week: Annotated[int | list[int] | None, prop("byMonthWeek")] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    end_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("endTime")
    ] = None
    except_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("exceptDate")
    ] = None
    repeat_count: Annotated[int | list[int] | None, prop("repeatCount")] = None
    repeat_frequency: Annotated[str | list[str] | None, prop("repeatFrequency")] = None
    schedule_timezone: Annotated[str | list[str] | None, prop("scheduleTimezone")] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None
    start_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("startTime")
    ] = None


class ScreeningEvent(Event):
    """A screening of a movie or other video.

    https://schema.org/ScreeningEvent
    """

    jsonld_type: ClassVar[str] = "ScreeningEvent"
    subtitle_language: Annotated[
        str | Language | list[str | Language] | None, prop("subtitleLanguage")
    ] = None
    video_format: Annotated[str | list[str] | None, prop("videoFormat")] = None
    work_presented: Annotated[Movie | list[Movie] | None, prop("workPresented")] = None


class Sculpture(CreativeWork):
    """A piece of sculpture.

    https://schema.org/Sculpture
    """

    jsonld_type: ClassVar[str] = "Sculpture"


class SearchAction(Action):
    """The act of searching for an object.\\n\\nRelated actions:\\n\\n* FindAction: SearchAction generally leads to a FindAction, but not necessarily.

    https://schema.org/SearchAction
    """

    jsonld_type: ClassVar[str] = "SearchAction"
    query: Annotated[str | list[str] | None, prop("query")] = None


class Season(CreativeWork):
    """A media season, e.g. TV, radio, video game etc.

    https://schema.org/Season

    Deprecated: superseded by CreativeWorkSeason.
    """

    jsonld_type: ClassVar[str] = "Season"


class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    https://schema.org/Seat
    """

    jsonld_type: ClassVar[str] = "Seat"
    seat_number: Annotated[str | list[str] | None, prop("seatNumber")] = None
    seat_row: Annotated[str | list[str] | None, prop("seatRow")] = None
    seat_section: Annotated[str | list[str] | None, prop("seatSection")] = None
    seating_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("seatingType"),
    ] = None


class Series(Intangible):
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind.

    https://schema.org/Series
    """

    jsonld_type: ClassVar[str] = "Series"


class Service(Intangible):
    """A service provided by an organization, e.g. delivery service, print services, etc.

    https://schema.org/Service
    """

    jsonld_type: ClassVar[str] = "Service"
    aggregate_rating: Annotated[
        AggregateRating | list[AggregateRating] | None, prop("aggregateRating")
    ] = None
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    available_channel: Annotated[
        ServiceChannel | list[ServiceChannel] | None, prop("availableChannel")
    ] = None
    award: Annotated[str | list[str] | None, prop("award")] = None
    brand: Annotated[Brand | Organization | list[Brand | Organization] | None, prop("brand")] = None
    broker: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("broker")
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    has_certification: Annotated[
        Certification | list[Certification] | None, prop("hasCertification")
    ] = None
    has_offer_catalog: Annotated[
        OfferCatalog | list[OfferCatalog] | None, prop("hasOfferCatalog")
    ] = None
    hours_available: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None, prop("hoursAvailable")
    ] = None
    is_related_to: Annotated[
        Product | Service | list[Product | Service] | None, prop("isRelatedTo")
    ] = None
    is_similar_to: Annotated[
        Product | Service | list[Product | Service] | None, prop("isSimilarTo")
    ] = None
    logo: Annotated[str | ImageObject | list[str | ImageObject] | None, prop("logo")] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    produces: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None,
        prop("produces", superseded_by=("serviceOutput",)),
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    provider_mobility: Annotated[str | list[str] | None, prop("providerMobility")] = None
    review: Annotated[Review | list[Review] | None, prop("review")] = None
    service_area: Annotated[
        AdministrativeArea | GeoShape | Place | list[AdministrativeArea | GeoShape | Place] | None,
        prop("serviceArea", superseded_by=("areaServed",)),
    ] = None
    service_audience: Annotated[
        Audience | list[Audience] | None, prop("serviceAudience", superseded_by=("audience",))
    ] = None
    service_output: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("serviceOutput")
    ] = None
    service_type: Annotated[
        str | GovernmentBenefitsType | list[str | GovernmentBenefitsType] | None,
        prop("serviceType"),
    ] = None
    slogan: Annotated[str | list[str] | None, prop("slogan")] = None
    terms_of_service: Annotated[str | list[str] | None, prop("termsOfService")] = None


class ServiceChannel(Intangible):
    """A means for accessing a service, e.g. a government office location, web site, or phone number.

    https://schema.org/ServiceChannel
    """

    jsonld_type: ClassVar[str] = "ServiceChannel"
    available_language: Annotated[
        str | Language | list[str | Language] | None, prop("availableLanguage")
    ] = None
    processing_time: Annotated[str | list[str] | None, prop("processingTime")] = None
    provides_service: Annotated[Service | list[Service] | None, prop("providesService")] = None
    service_location: Annotated[Place | list[Place] | None, prop("serviceLocation")] = None
    service_phone: Annotated[ContactPoint | list[ContactPoint] | None, prop("servicePhone")] = None
    service_postal_address: Annotated[
        PostalAddress | list[PostalAddress] | None, prop("servicePostalAddress")
    ] = None
    service_sms_number: Annotated[
        ContactPoint | list[ContactPoint] | None, prop("serviceSmsNumber")
    ] = None
    service_url: Annotated[str | list[str] | None, prop("serviceUrl")] = None


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music.

    https://schema.org/SheetMusic
    """

    jsonld_type: ClassVar[str] = "SheetMusic"


class ShortStory(CreativeWork):
    """Short story or tale.

    https://schema.org/ShortStory
    """

    jsonld_type: ClassVar[str] = "ShortStory"


class SocialEvent(Event):
    """Event type: Social event.

    https://schema.org/SocialEvent
    """

    jsonld_type: ClassVar[str] = "SocialEvent"


class SoftwareApplication(CreativeWork):
    """A software application.

    https://schema.org/SoftwareApplication
    """

    jsonld_type: ClassVar[str] = "SoftwareApplication"
    application_category: Annotated[str | list[str] | None, prop("applicationCategory")] = None
    application_sub_category: Annotated[str | list[str] | None, prop("applicationSubCategory")] = (
        None
    )
    application_suite: Annotated[str | list[str] | None, prop("applicationSuite")] = None
    available_on_device: Annotated[str | list[str] | None, prop("availableOnDevice")] = None
    countries_not_supported: Annotated[str | list[str] | None, prop("countriesNotSupported")] = None
    countries_supported: Annotated[str | list[str] | None, prop("countriesSupported")] = None
    device: Annotated[
        str | list[str] | None, prop("device", superseded_by=("availableOnDevice",))
    ] = None
    download_url: Annotated[str | list[str] | None, prop("downloadUrl")] = None
    feature_list: Annotated[str | list[str] | None, prop("featureList")] = None
    file_size: Annotated[str | list[str] | None, prop("fileSize")] = None
    install_url: Annotated[str | list[str] | None, prop("installUrl")] = None
    memory_requirements: Annotated[str | list[str] | None, prop("memoryRequirements")] = None
    operating_system: Annotated[str | list[str] | None, prop("operatingSystem")] = None
    permissions: Annotated[str | list[str] | None, prop("permissions")] = None
    processor_requirements: Annotated[str | list[str] | None, prop("processorRequirements")] = None
    release_notes: Annotated[str | list[str] | None, prop("releaseNotes")] = None
    requirements: Annotated[
        str | list[str] | None, prop("requirements", superseded_by=("softwareRequirements",))
    ] = None
    runtime_platform: Annotated[str | list[str] | None, prop("runtimePlatform")] = None
    screenshot: Annotated[
        str | ImageObject | list[str | ImageObject] | None, prop("screenshot")
    ] = None
    software_add_on: Annotated[
        SoftwareApplication | list[SoftwareApplication] | None, prop("softwareAddOn")
    ] = None
    software_help: Annotated[CreativeWork | list[CreativeWork] | None, prop("softwareHelp")] = None
    software_requirements: Annotated[
        str | SoftwareApplication | list[str | SoftwareApplication] | None,
        prop("softwareRequirements"),
    ] = None
    software_version: Annotated[str | list[str] | None, prop("softwareVersion")] = None
    storage_requirements: Annotated[str | list[str] | None, prop("storageRequirements")] = None
    supporting_data: Annotated[DataFeed | list[DataFeed] | None, prop("supportingData")] = None


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code.

    https://schema.org/SoftwareSourceCode
    """

    jsonld_type: ClassVar[str] = "SoftwareSourceCode"
    code_repository: Annotated[str | list[str] | None, prop("codeRepository")] = None
    code_sample_type: Annotated[str | list[str] | None, prop("codeSampleType")] = None
    programming_language: Annotated[
        str | ComputerLanguage | list[str | ComputerLanguage] | None, prop("programmingLanguage")
    ] = None
    runtime: Annotated[
        str | list[str] | None, prop("runtime", superseded_by=("runtimePlatform",))
    ] = None
    runtime_platform: Annotated[str | list[str] | None, prop("runtimePlatform")] = None
    sample_type: Annotated[
        str | list[str] | None, prop("sampleType", superseded_by=("codeSampleType",))
    ] = None
    target_product: Annotated[
        SoftwareApplication | list[SoftwareApplication] | None, prop("targetProduct")
    ] = None


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind.

    https://schema.org/SomeProducts
    """

    jsonld_type: ClassVar[str] = "SomeProducts"
    inventory_level: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("inventoryLevel")
    ] = None


class SpeakableSpecification(Intangible):
    """A SpeakableSpecification indicates (typically via xpath or cssSelector) sections of a document that are highlighted as particularly speakable.

    https://schema.org/SpeakableSpecification
    """

    jsonld_type: ClassVar[str] = "SpeakableSpecification"


class SpecialAnnouncement(CreativeWork):
    """A SpecialAnnouncement combines a simple date-stamped textual information update with contextualized Web links and other structured data.

    https://schema.org/SpecialAnnouncement
    """

    jsonld_type: ClassVar[str] = "SpecialAnnouncement"
    announcement_location: Annotated[
        CivicStructure | LocalBusiness | list[CivicStructure | LocalBusiness] | None,
        prop("announcementLocation"),
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    date_posted: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("datePosted")
    ] = None
    disease_prevention_info: Annotated[str | list[str] | None, prop("diseasePreventionInfo")] = None
    disease_spread_statistics: Annotated[
        str | Dataset | Observation | list[str | Dataset | Observation] | None,
        prop("diseaseSpreadStatistics"),
    ] = None
    getting_tested_info: Annotated[str | list[str] | None, prop("gettingTestedInfo")] = None
    government_benefits_info: Annotated[
        GovernmentService | list[GovernmentService] | None, prop("governmentBenefitsInfo")
    ] = None
    news_updates_and_guidelines: Annotated[
        str | list[str] | None, prop("newsUpdatesAndGuidelines")
    ] = None
    public_transport_closures_info: Annotated[
        str | list[str] | None, prop("publicTransportClosuresInfo")
    ] = None
    quarantine_guidelines: Annotated[str | list[str] | None, prop("quarantineGuidelines")] = None
    school_closures_info: Annotated[str | list[str] | None, prop("schoolClosuresInfo")] = None
    travel_bans: Annotated[str | list[str] | None, prop("travelBans")] = None


class SportsEvent(Event):
    """Event type: Sports event.

    https://schema.org/SportsEvent
    """

    jsonld_type: ClassVar[str] = "SportsEvent"
    away_team: Annotated[
        Person | SportsTeam | list[Person | SportsTeam] | None, prop("awayTeam")
    ] = None
    competitor: Annotated[
        Person | SportsTeam | list[Person | SportsTeam] | None, prop("competitor")
    ] = None
    home_team: Annotated[
        Person | SportsTeam | list[Person | SportsTeam] | None, prop("homeTeam")
    ] = None
    referee: Annotated[Person | list[Person] | None, prop("referee")] = None
    sport: Annotated[str | list[str] | None, prop("sport")] = None


class SportsOrganization(Organization):
    """Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.

    https://schema.org/SportsOrganization
    """

    jsonld_type: ClassVar[str] = "SportsOrganization"
    sport: Annotated[str | list[str] | None, prop("sport")] = None


class Statement(CreativeWork):
    """A statement about something, for example a fun or interesting fact.

    https://schema.org/Statement
    """

    jsonld_type: ClassVar[str] = "Statement"


class StatisticalPopulation(Intangible):
    """A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints.

    https://schema.org/StatisticalPopulation
    """

    jsonld_type: ClassVar[str] = "StatisticalPopulation"


class StructuredValue(Intangible):
    """Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.

    https://schema.org/StructuredValue
    """

    jsonld_type: ClassVar[str] = "StructuredValue"


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.

    https://schema.org/Substance
    """

    jsonld_type: ClassVar[str] = "Substance"
    active_ingredient: Annotated[str | list[str] | None, prop("activeIngredient")] = None
    maximum_intake: Annotated[
        MaximumDoseSchedule | list[MaximumDoseSchedule] | None, prop("maximumIntake")
    ] = None


class SuperficialAnatomy(MedicalEntity):
    """Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures.

    https://schema.org/SuperficialAnatomy
    """

    jsonld_type: ClassVar[str] = "SuperficialAnatomy"
    associated_pathophysiology: Annotated[
        str | list[str] | None, prop("associatedPathophysiology")
    ] = None
    related_anatomy: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | list[AnatomicalStructure | AnatomicalSystem]
        | None,
        prop("relatedAnatomy"),
    ] = None
    related_condition: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("relatedCondition")
    ] = None
    related_therapy: Annotated[
        MedicalTherapy | list[MedicalTherapy] | None, prop("relatedTherapy")
    ] = None
    significance: Annotated[str | list[str] | None, prop("significance")] = None


class Syllabus(CreativeWork):
    """A syllabus that describes the material covered in a course, often with several such sections per Course so that a distinct timeRequired can be provided for that section of the Course.

    https://schema.org/Syllabus
    """

    jsonld_type: ClassVar[str] = "Syllabus"


class TheaterEvent(Event):
    """Event type: Theater performance.

    https://schema.org/TheaterEvent
    """

    jsonld_type: ClassVar[str] = "TheaterEvent"


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.

    https://schema.org/Thesis
    """

    jsonld_type: ClassVar[str] = "Thesis"
    in_support_of: Annotated[str | list[str] | None, prop("inSupportOf")] = None


class Ticket(Intangible):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    https://schema.org/Ticket
    """

    jsonld_type: ClassVar[str] = "Ticket"
    date_issued: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("dateIssued")
    ] = None
    issued_by: Annotated[Organization | list[Organization] | None, prop("issuedBy")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    ticket_number: Annotated[str | list[str] | None, prop("ticketNumber")] = None
    ticket_token: Annotated[str | list[str] | None, prop("ticketToken")] = None
    ticketed_seat: Annotated[Seat | list[Seat] | None, prop("ticketedSeat")] = None
    total_price: Annotated[
        str
        | int
        | float
        | PriceSpecification
        | list[str | int | float | PriceSpecification]
        | None,
        prop("totalPrice"),
    ] = None
    under_name: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("underName")
    ] = None


class TouristAttraction(Place):
    """A tourist attraction.

    https://schema.org/TouristAttraction
    """

    jsonld_type: ClassVar[str] = "TouristAttraction"
    available_language: Annotated[
        str | Language | list[str | Language] | None, prop("availableLanguage")
    ] = None
    tourist_type: Annotated[str | Audience | list[str | Audience] | None, prop("touristType")] = (
        None
    )


class TradeAction(Action):
    """The act of participating in an exchange of goods and services for monetary compensation.

    https://schema.org/TradeAction
    """

    jsonld_type: ClassVar[str] = "TradeAction"
    price: Annotated[str | int | float | list[str | int | float] | None, prop("price")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    price_specification: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("priceSpecification")
    ] = None


class TransferAction(Action):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

    https://schema.org/TransferAction
    """

    jsonld_type: ClassVar[str] = "TransferAction"
    from_location: Annotated[Place | list[Place] | None, prop("fromLocation")] = None
    to_location: Annotated[Place | list[Place] | None, prop("toLocation")] = None


class Trip(Intangible):
    """A trip or journey.

    https://schema.org/Trip
    """

    jsonld_type: ClassVar[str] = "Trip"
    arrival_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("arrivalTime")
    ] = None
    departure_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("departureTime")
    ] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    trip_origin: Annotated[Place | list[Place] | None, prop("tripOrigin")] = None


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    https://schema.org/UpdateAction
    """

    jsonld_type: ClassVar[str] = "UpdateAction"
    collection: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None,
        prop("collection", superseded_by=("targetCollection",)),
    ] = None
    target_collection: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("targetCollection")
    ] = None


class UserInteraction(Event):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserInteraction

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserInteraction"


class Vehicle(Product):
    """A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.

    https://schema.org/Vehicle
    """

    jsonld_type: ClassVar[str] = "Vehicle"
    acceleration_time: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("accelerationTime")
    ] = None
    body_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("bodyType"),
    ] = None
    call_sign: Annotated[str | list[str] | None, prop("callSign")] = None
    cargo_volume: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("cargoVolume")
    ] = None
    date_vehicle_first_registered: Annotated[
        _dt.date | list[_dt.date] | None, prop("dateVehicleFirstRegistered")
    ] = None
    drive_wheel_configuration: Annotated[
        str | DriveWheelConfigurationValue | list[str | DriveWheelConfigurationValue] | None,
        prop("driveWheelConfiguration"),
    ] = None
    emissions_co2: Annotated[int | float | list[int | float] | None, prop("emissionsCO2")] = None
    fuel_capacity: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("fuelCapacity")
    ] = None
    fuel_consumption: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("fuelConsumption")
    ] = None
    fuel_efficiency: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("fuelEfficiency")
    ] = None
    fuel_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("fuelType"),
    ] = None
    known_vehicle_damages: Annotated[str | list[str] | None, prop("knownVehicleDamages")] = None
    meets_emission_standard: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("meetsEmissionStandard"),
    ] = None
    mileage_from_odometer: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("mileageFromOdometer")
    ] = None
    model_date: Annotated[_dt.date | list[_dt.date] | None, prop("modelDate")] = None
    number_of_airbags: Annotated[
        str | int | float | list[str | int | float] | None, prop("numberOfAirbags")
    ] = None
    number_of_axles: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfAxles"),
    ] = None
    number_of_doors: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfDoors"),
    ] = None
    number_of_forward_gears: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfForwardGears"),
    ] = None
    number_of_previous_owners: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfPreviousOwners"),
    ] = None
    payload: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("payload")] = None
    seating_capacity: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("seatingCapacity"),
    ] = None
    speed: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("speed")] = None
    steering_position: Annotated[
        SteeringPositionValue | list[SteeringPositionValue] | None, prop("steeringPosition")
    ] = None
    tongue_weight: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("tongueWeight")
    ] = None
    trailer_weight: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("trailerWeight")
    ] = None
    vehicle_configuration: Annotated[str | list[str] | None, prop("vehicleConfiguration")] = None
    vehicle_engine: Annotated[
        EngineSpecification | list[EngineSpecification] | None, prop("vehicleEngine")
    ] = None
    vehicle_identification_number: Annotated[
        str | list[str] | None, prop("vehicleIdentificationNumber")
    ] = None
    vehicle_interior_color: Annotated[str | list[str] | None, prop("vehicleInteriorColor")] = None
    vehicle_interior_type: Annotated[str | list[str] | None, prop("vehicleInteriorType")] = None
    vehicle_model_date: Annotated[_dt.date | list[_dt.date] | None, prop("vehicleModelDate")] = None
    vehicle_seating_capacity: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("vehicleSeatingCapacity"),
    ] = None
    vehicle_special_usage: Annotated[
        str | CarUsageType | list[str | CarUsageType] | None, prop("vehicleSpecialUsage")
    ] = None
    vehicle_transmission: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("vehicleTransmission"),
    ] = None
    weight_total: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("weightTotal")
    ] = None
    wheelbase: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("wheelbase")] = (
        None
    )


class VirtualLocation(Intangible):
    """An online or virtual location for attending events.

    https://schema.org/VirtualLocation
    """

    jsonld_type: ClassVar[str] = "VirtualLocation"


class VisualArtsEvent(Event):
    """Event type: Visual arts event.

    https://schema.org/VisualArtsEvent
    """

    jsonld_type: ClassVar[str] = "VisualArtsEvent"


class VisualArtwork(CreativeWork):
    """A work of art that is primarily visual in character.

    https://schema.org/VisualArtwork
    """

    jsonld_type: ClassVar[str] = "VisualArtwork"
    art_edition: Annotated[str | int | list[str | int] | None, prop("artEdition")] = None
    art_medium: Annotated[str | list[str] | None, prop("artMedium")] = None
    artform: Annotated[str | list[str] | None, prop("artform")] = None
    artist: Annotated[Person | list[Person] | None, prop("artist")] = None
    artwork_surface: Annotated[str | list[str] | None, prop("artworkSurface")] = None
    colorist: Annotated[Person | list[Person] | None, prop("colorist")] = None
    depth: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("depth")
    ] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    inker: Annotated[Person | list[Person] | None, prop("inker")] = None
    letterer: Annotated[Person | list[Person] | None, prop("letterer")] = None
    penciler: Annotated[Person | list[Person] | None, prop("penciler")] = None
    surface: Annotated[
        str | list[str] | None, prop("surface", superseded_by=("artworkSurface",))
    ] = None
    weight: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("weight")
    ] = None
    width: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("width")
    ] = None


class WebPage(CreativeWork):
    """A web page.

    https://schema.org/WebPage
    """

    jsonld_type: ClassVar[str] = "WebPage"
    breadcrumb: Annotated[
        str | BreadcrumbList | list[str | BreadcrumbList] | None, prop("breadcrumb")
    ] = None
    last_reviewed: Annotated[_dt.date | list[_dt.date] | None, prop("lastReviewed")] = None
    main_content_of_page: Annotated[
        WebPageElement | list[WebPageElement] | None, prop("mainContentOfPage")
    ] = None
    primary_image_of_page: Annotated[
        ImageObject | list[ImageObject] | None, prop("primaryImageOfPage")
    ] = None
    related_link: Annotated[str | list[str] | None, prop("relatedLink")] = None
    reviewed_by: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("reviewedBy")
    ] = None
    significant_link: Annotated[str | list[str] | None, prop("significantLink")] = None
    significant_links: Annotated[
        str | list[str] | None, prop("significantLinks", superseded_by=("significantLink",))
    ] = None
    speakable: Annotated[
        str | SpeakableSpecification | list[str | SpeakableSpecification] | None, prop("speakable")
    ] = None
    specialty: Annotated[
        MedicalSpecialty | Specialty | list[MedicalSpecialty | Specialty] | None, prop("specialty")
    ] = None


class WebPageElement(CreativeWork):
    """A web page element, like a table or an image.

    https://schema.org/WebPageElement
    """

    jsonld_type: ClassVar[str] = "WebPageElement"


class WebSite(CreativeWork):
    """A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.

    https://schema.org/WebSite
    """

    jsonld_type: ClassVar[str] = "WebSite"
    issn: Annotated[str | list[str] | None, prop("issn")] = None


class WorkersUnion(Organization):
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.

    https://schema.org/WorkersUnion
    """

    jsonld_type: ClassVar[str] = "WorkersUnion"


class Model3D(MediaObject):
    """A 3D model represents some kind of 3D content, which may have encodings in one or more MediaObjects.

    https://schema.org/3DModel
    """

    jsonld_type: ClassVar[str] = "3DModel"
    is_resizable: Annotated[bool | list[bool] | None, prop("isResizable")] = None


class AboutPage(WebPage):
    """Web page type: About page.

    https://schema.org/AboutPage
    """

    jsonld_type: ClassVar[str] = "AboutPage"


class ActivateAction(ControlAction):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

    https://schema.org/ActivateAction
    """

    jsonld_type: ClassVar[str] = "ActivateAction"


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    https://schema.org/AddAction
    """

    jsonld_type: ClassVar[str] = "AddAction"


class AdvertiserContentArticle(Article):
    """An Article that an external entity has paid to place or to produce to its specifications.

    https://schema.org/AdvertiserContentArticle
    """

    jsonld_type: ClassVar[str] = "AdvertiserContentArticle"


class AggregateOffer(Offer):
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.\\n\\nNote: AggregateOffers are normally expected to associate multiple offer...

    https://schema.org/AggregateOffer
    """

    jsonld_type: ClassVar[str] = "AggregateOffer"
    high_price: Annotated[str | int | float | list[str | int | float] | None, prop("highPrice")] = (
        None
    )
    low_price: Annotated[str | int | float | list[str | int | float] | None, prop("lowPrice")] = (
        None
    )
    offer_count: Annotated[int | list[int] | None, prop("offerCount")] = None
    offers: Annotated[Demand | Offer | list[Demand | Offer] | None, prop("offers")] = None


class AggregateRating(Rating):
    """The average rating based on multiple ratings or reviews.

    https://schema.org/AggregateRating
    """

    jsonld_type: ClassVar[str] = "AggregateRating"
    item_reviewed: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("itemReviewed")
    ] = None
    rating_count: Annotated[int | list[int] | None, prop("ratingCount")] = None
    review_count: Annotated[int | list[int] | None, prop("reviewCount")] = None


class Airport(CivicStructure):
    """An airport.

    https://schema.org/Airport
    """

    jsonld_type: ClassVar[str] = "Airport"
    iata_code: Annotated[str | list[str] | None, prop("iataCode")] = None
    icao_code: Annotated[str | list[str] | None, prop("icaoCode")] = None


class AllocateAction(OrganizeAction):
    """The act of organizing tasks/objects/events by associating resources to it.

    https://schema.org/AllocateAction
    """

    jsonld_type: ClassVar[str] = "AllocateAction"


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    https://schema.org/AnimalShelter
    """

    jsonld_type: ClassVar[str] = "AnimalShelter"


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    https://schema.org/Answer
    """

    jsonld_type: ClassVar[str] = "Answer"


class Apartment(Accommodation):
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see http://en.wikipedia...

    https://schema.org/Apartment
    """

    jsonld_type: ClassVar[str] = "Apartment"


class ApartmentComplex(Residence):
    """Residence type: Apartment complex.

    https://schema.org/ApartmentComplex
    """

    jsonld_type: ClassVar[str] = "ApartmentComplex"
    number_of_accommodation_units: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfAccommodationUnits")
    ] = None
    number_of_available_accommodation_units: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None,
        prop("numberOfAvailableAccommodationUnits"),
    ] = None
    number_of_bedrooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfBedrooms"),
    ] = None
    pets_allowed: Annotated[str | bool | list[str | bool] | None, prop("petsAllowed")] = None


class ApplyAction(OrganizeAction):
    """The act of registering to an organization/service without the guarantee to receive it.\\n\\nRelated actions:\\n\\n* RegisterAction: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.

    https://schema.org/ApplyAction
    """

    jsonld_type: ClassVar[str] = "ApplyAction"


class ApprovedIndication(MedicalIndication):
    """An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.

    https://schema.org/ApprovedIndication
    """

    jsonld_type: ClassVar[str] = "ApprovedIndication"


class Aquarium(CivicStructure):
    """Aquarium.

    https://schema.org/Aquarium
    """

    jsonld_type: ClassVar[str] = "Aquarium"


class ArchiveOrganization(LocalBusiness):
    """An organization with archival holdings.

    https://schema.org/ArchiveOrganization
    """

    jsonld_type: ClassVar[str] = "ArchiveOrganization"
    archive_held: Annotated[
        ArchiveComponent | list[ArchiveComponent] | None, prop("archiveHeld")
    ] = None


class ArriveAction(MoveAction):
    """The act of arriving at a place.

    https://schema.org/ArriveAction
    """

    jsonld_type: ClassVar[str] = "ArriveAction"


class AudioObject(MediaObject):
    """An audio file.

    https://schema.org/AudioObject
    """

    jsonld_type: ClassVar[str] = "AudioObject"
    caption: Annotated[str | MediaObject | list[str | MediaObject] | None, prop("caption")] = None
    embedded_text_caption: Annotated[str | list[str] | None, prop("embeddedTextCaption")] = None
    transcript: Annotated[str | list[str] | None, prop("transcript")] = None


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    https://schema.org/AutomotiveBusiness
    """

    jsonld_type: ClassVar[str] = "AutomotiveBusiness"


class Beach(CivicStructure):
    """Beach.

    https://schema.org/Beach
    """

    jsonld_type: ClassVar[str] = "Beach"


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\\n\\nRelated actions:\\n\\n* FollowAction: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.

    https://schema.org/BefriendAction
    """

    jsonld_type: ClassVar[str] = "BefriendAction"


class BloodTest(MedicalTest):
    """A medical test performed on a sample of a patient's blood.

    https://schema.org/BloodTest
    """

    jsonld_type: ClassVar[str] = "BloodTest"


class BoatReservation(Reservation):
    """A reservation for boat travel.

    https://schema.org/BoatReservation
    """

    jsonld_type: ClassVar[str] = "BoatReservation"


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels.

    https://schema.org/BoatTerminal
    """

    jsonld_type: ClassVar[str] = "BoatTerminal"


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    https://schema.org/BoatTrip
    """

    jsonld_type: ClassVar[str] = "BoatTrip"
    arrival_boat_terminal: Annotated[
        BoatTerminal | list[BoatTerminal] | None, prop("arrivalBoatTerminal")
    ] = None
    departure_boat_terminal: Annotated[
        BoatTerminal | list[BoatTerminal] | None, prop("departureBoatTerminal")
    ] = None


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    https://schema.org/BodyOfWater
    """

    jsonld_type: ClassVar[str] = "BodyOfWater"


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    https://schema.org/Bone
    """

    jsonld_type: ClassVar[str] = "Bone"


class BookmarkAction(OrganizeAction):
    """An agent bookmarks/flags/labels/tags/marks an object.

    https://schema.org/BookmarkAction
    """

    jsonld_type: ClassVar[str] = "BookmarkAction"


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date.

    https://schema.org/BorrowAction
    """

    jsonld_type: ClassVar[str] = "BorrowAction"
    lender: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("lender")
    ] = None


class BrainStructure(AnatomicalStructure):
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.

    https://schema.org/BrainStructure
    """

    jsonld_type: ClassVar[str] = "BrainStructure"


class BreadcrumbList(ItemList):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.\\n\\nThe position property is used to reconstruct the order...

    https://schema.org/BreadcrumbList
    """

    jsonld_type: ClassVar[str] = "BreadcrumbList"


class Bridge(CivicStructure):
    """A bridge.

    https://schema.org/Bridge
    """

    jsonld_type: ClassVar[str] = "Bridge"


class BroadcastEvent(PublicationEvent):
    """An over the air or online broadcast event.

    https://schema.org/BroadcastEvent
    """

    jsonld_type: ClassVar[str] = "BroadcastEvent"
    broadcast_of_event: Annotated[Event | list[Event] | None, prop("broadcastOfEvent")] = None
    is_live_broadcast: Annotated[bool | list[bool] | None, prop("isLiveBroadcast")] = None
    subtitle_language: Annotated[
        str | Language | list[str | Language] | None, prop("subtitleLanguage")
    ] = None
    video_format: Annotated[str | list[str] | None, prop("videoFormat")] = None


class BroadcastService(Service):
    """A delivery service through which content is provided via broadcast over the air or online.

    https://schema.org/BroadcastService
    """

    jsonld_type: ClassVar[str] = "BroadcastService"
    area: Annotated[Place | list[Place] | None, prop("area", superseded_by=("serviceArea",))] = None
    broadcast_affiliate_of: Annotated[
        Organization | list[Organization] | None, prop("broadcastAffiliateOf")
    ] = None
    broadcast_display_name: Annotated[str | list[str] | None, prop("broadcastDisplayName")] = None
    broadcast_frequency: Annotated[
        str | BroadcastFrequencySpecification | list[str | BroadcastFrequencySpecification] | None,
        prop("broadcastFrequency"),
    ] = None
    broadcast_timezone: Annotated[str | list[str] | None, prop("broadcastTimezone")] = None
    broadcaster: Annotated[Organization | list[Organization] | None, prop("broadcaster")] = None
    call_sign: Annotated[str | list[str] | None, prop("callSign")] = None
    has_broadcast_channel: Annotated[
        BroadcastChannel | list[BroadcastChannel] | None, prop("hasBroadcastChannel")
    ] = None
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    parent_service: Annotated[
        BroadcastService | list[BroadcastService] | None, prop("parentService")
    ] = None
    video_format: Annotated[str | list[str] | None, prop("videoFormat")] = None


class BusOrCoach(Vehicle):
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers.

    https://schema.org/BusOrCoach
    """

    jsonld_type: ClassVar[str] = "BusOrCoach"
    acriss_code: Annotated[str | list[str] | None, prop("acrissCode")] = None
    roof_load: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("roofLoad")] = (
        None
    )


class BusReservation(Reservation):
    """A reservation for bus travel.

    https://schema.org/BusReservation
    """

    jsonld_type: ClassVar[str] = "BusReservation"


class BusStation(CivicStructure):
    """A bus station.

    https://schema.org/BusStation
    """

    jsonld_type: ClassVar[str] = "BusStation"


class BusStop(CivicStructure):
    """A bus stop.

    https://schema.org/BusStop
    """

    jsonld_type: ClassVar[str] = "BusStop"


class BusTrip(Trip):
    """A trip on a commercial bus line.

    https://schema.org/BusTrip
    """

    jsonld_type: ClassVar[str] = "BusTrip"
    arrival_bus_stop: Annotated[
        BusStation | BusStop | list[BusStation | BusStop] | None, prop("arrivalBusStop")
    ] = None
    bus_name: Annotated[str | list[str] | None, prop("busName")] = None
    bus_number: Annotated[str | list[str] | None, prop("busNumber")] = None
    departure_bus_stop: Annotated[
        BusStation | BusStop | list[BusStation | BusStop] | None, prop("departureBusStop")
    ] = None


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

    https://schema.org/BusinessAudience
    """

    jsonld_type: ClassVar[str] = "BusinessAudience"
    number_of_employees: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfEmployees")
    ] = None
    yearly_revenue: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("yearlyRevenue")
    ] = None
    years_in_operation: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("yearsInOperation")
    ] = None


class BusinessEntityType(Enumeration):
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\\n\\nCommonly used values:\\...

    https://schema.org/BusinessEntityType
    """

    jsonld_type: ClassVar[str] = "BusinessEntityType"


class BusinessFunction(Enumeration):
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer.

    https://schema.org/BusinessFunction
    """

    jsonld_type: ClassVar[str] = "BusinessFunction"


class BuyAction(TradeAction):
    """The act of giving money to a seller in exchange for goods or services rendered.

    https://schema.org/BuyAction
    """

    jsonld_type: ClassVar[str] = "BuyAction"
    seller: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("seller")
    ] = None
    vendor: Annotated[
        Organization | Person | list[Organization | Person] | None,
        prop("vendor", superseded_by=("seller",)),
    ] = None
    warranty_promise: Annotated[
        WarrantyPromise | list[WarrantyPromise] | None,
        prop("warrantyPromise", superseded_by=("warranty",)),
    ] = None


class CDCPMDRecord(StructuredValue):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format used for hospital data reporting.

    https://schema.org/CDCPMDRecord
    """

    jsonld_type: ClassVar[str] = "CDCPMDRecord"
    cvd_collection_date: Annotated[
        str | _dt.datetime | list[str | _dt.datetime] | None, prop("cvdCollectionDate")
    ] = None
    cvd_facility_county: Annotated[str | list[str] | None, prop("cvdFacilityCounty")] = None
    cvd_facility_id: Annotated[str | list[str] | None, prop("cvdFacilityId")] = None
    cvd_num_beds: Annotated[int | float | list[int | float] | None, prop("cvdNumBeds")] = None
    cvd_num_beds_occ: Annotated[int | float | list[int | float] | None, prop("cvdNumBedsOcc")] = (
        None
    )
    cvd_num_c19_died: Annotated[int | float | list[int | float] | None, prop("cvdNumC19Died")] = (
        None
    )
    cvd_num_c19_ho_pats: Annotated[
        int | float | list[int | float] | None, prop("cvdNumC19HOPats")
    ] = None
    cvd_num_c19_hosp_pats: Annotated[
        int | float | list[int | float] | None, prop("cvdNumC19HospPats")
    ] = None
    cvd_num_c19_mech_vent_pats: Annotated[
        int | float | list[int | float] | None, prop("cvdNumC19MechVentPats")
    ] = None
    cvd_num_c19_of_mech_vent_pats: Annotated[
        int | float | list[int | float] | None, prop("cvdNumC19OFMechVentPats")
    ] = None
    cvd_num_c19_overflow_pats: Annotated[
        int | float | list[int | float] | None, prop("cvdNumC19OverflowPats")
    ] = None
    cvd_num_icu_beds: Annotated[int | float | list[int | float] | None, prop("cvdNumICUBeds")] = (
        None
    )
    cvd_num_icu_beds_occ: Annotated[
        int | float | list[int | float] | None, prop("cvdNumICUBedsOcc")
    ] = None
    cvd_num_tot_beds: Annotated[int | float | list[int | float] | None, prop("cvdNumTotBeds")] = (
        None
    )
    cvd_num_vent: Annotated[int | float | list[int | float] | None, prop("cvdNumVent")] = None
    cvd_num_vent_use: Annotated[int | float | list[int | float] | None, prop("cvdNumVentUse")] = (
        None
    )
    date_posted: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("datePosted")
    ] = None


class CableOrSatelliteService(Service):
    """A service which provides access to media programming like TV or radio.

    https://schema.org/CableOrSatelliteService
    """

    jsonld_type: ClassVar[str] = "CableOrSatelliteService"


class CampingPitch(Accommodation):
    """A CampingPitch is an individual place for overnight stay in the outdoors, typically being part of a larger camping site, or Campground.\\n\\n In British English a campsite, or campground, is an area, usually divided into a number of pitche...

    https://schema.org/CampingPitch
    """

    jsonld_type: ClassVar[str] = "CampingPitch"


class Car(Vehicle):
    """A car is a wheeled, self-powered motor vehicle used for transportation.

    https://schema.org/Car
    """

    jsonld_type: ClassVar[str] = "Car"
    acriss_code: Annotated[str | list[str] | None, prop("acrissCode")] = None
    roof_load: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("roofLoad")] = (
        None
    )


class CategoryCode(DefinedTerm):
    """A Category Code.

    https://schema.org/CategoryCode
    """

    jsonld_type: ClassVar[str] = "CategoryCode"
    code_value: Annotated[str | list[str] | None, prop("codeValue")] = None
    in_code_set: Annotated[
        str | CategoryCodeSet | list[str | CategoryCodeSet] | None, prop("inCodeSet")
    ] = None


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    https://schema.org/CategoryCodeSet
    """

    jsonld_type: ClassVar[str] = "CategoryCodeSet"
    has_category_code: Annotated[
        CategoryCode | list[CategoryCode] | None, prop("hasCategoryCode")
    ] = None


class Cemetery(CivicStructure):
    """A graveyard.

    https://schema.org/Cemetery
    """

    jsonld_type: ClassVar[str] = "Cemetery"


class CheckAction(FindAction):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

    https://schema.org/CheckAction
    """

    jsonld_type: ClassVar[str] = "CheckAction"


class CheckoutPage(WebPage):
    """Web page type: Checkout page.

    https://schema.org/CheckoutPage
    """

    jsonld_type: ClassVar[str] = "CheckoutPage"


class ChildCare(LocalBusiness):
    """A Childcare center.

    https://schema.org/ChildCare
    """

    jsonld_type: ClassVar[str] = "ChildCare"


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    https://schema.org/ChooseAction
    """

    jsonld_type: ClassVar[str] = "ChooseAction"
    action_option: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("actionOption"),
    ] = None
    option: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("option", superseded_by=("actionOption",)),
    ] = None


class City(AdministrativeArea):
    """A city or town.

    https://schema.org/City
    """

    jsonld_type: ClassVar[str] = "City"


class ClaimReview(Review):
    """A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

    https://schema.org/ClaimReview
    """

    jsonld_type: ClassVar[str] = "ClaimReview"
    claim_reviewed: Annotated[str | list[str] | None, prop("claimReviewed")] = None


class CollectionPage(WebPage):
    """Web page type: Collection page.

    https://schema.org/CollectionPage
    """

    jsonld_type: ClassVar[str] = "CollectionPage"


class ComicIssue(PublicationIssue):
    """Individual comic issues are serially published as part of a larger series.

    https://schema.org/ComicIssue
    """

    jsonld_type: ClassVar[str] = "ComicIssue"
    artist: Annotated[Person | list[Person] | None, prop("artist")] = None
    colorist: Annotated[Person | list[Person] | None, prop("colorist")] = None
    inker: Annotated[Person | list[Person] | None, prop("inker")] = None
    letterer: Annotated[Person | list[Person] | None, prop("letterer")] = None
    penciler: Annotated[Person | list[Person] | None, prop("penciler")] = None
    variant_cover: Annotated[str | list[str] | None, prop("variantCover")] = None


class CommunicateAction(InteractAction):
    """The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.

    https://schema.org/CommunicateAction
    """

    jsonld_type: ClassVar[str] = "CommunicateAction"
    about: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("about")
    ] = None
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    language: Annotated[
        Language | list[Language] | None, prop("language", superseded_by=("inLanguage",))
    ] = None
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class ContactPage(WebPage):
    """Web page type: Contact page.

    https://schema.org/ContactPage
    """

    jsonld_type: ClassVar[str] = "ContactPage"


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department.

    https://schema.org/ContactPoint
    """

    jsonld_type: ClassVar[str] = "ContactPoint"
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    available_language: Annotated[
        str | Language | list[str | Language] | None, prop("availableLanguage")
    ] = None
    contact_option: Annotated[
        ContactPointOption | list[ContactPointOption] | None, prop("contactOption")
    ] = None
    contact_type: Annotated[str | list[str] | None, prop("contactType")] = None
    email: Annotated[str | list[str] | None, prop("email")] = None
    fax_number: Annotated[str | list[str] | None, prop("faxNumber")] = None
    hours_available: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None, prop("hoursAvailable")
    ] = None
    product_supported: Annotated[
        str | Product | list[str | Product] | None, prop("productSupported")
    ] = None
    service_area: Annotated[
        AdministrativeArea | GeoShape | Place | list[AdministrativeArea | GeoShape | Place] | None,
        prop("serviceArea", superseded_by=("areaServed",)),
    ] = None
    telephone: Annotated[str | list[str] | None, prop("telephone")] = None


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    https://schema.org/Continent
    """

    jsonld_type: ClassVar[str] = "Continent"


class CookAction(CreateAction):
    """The act of producing/preparing food.

    https://schema.org/CookAction
    """

    jsonld_type: ClassVar[str] = "CookAction"
    food_establishment: Annotated[
        FoodEstablishment | Place | list[FoodEstablishment | Place] | None,
        prop("foodEstablishment"),
    ] = None
    food_event: Annotated[FoodEvent | list[FoodEvent] | None, prop("foodEvent")] = None
    recipe: Annotated[Recipe | list[Recipe] | None, prop("recipe")] = None


class CorrectionComment(Comment):
    """A comment that corrects CreativeWork.

    https://schema.org/CorrectionComment
    """

    jsonld_type: ClassVar[str] = "CorrectionComment"


class Country(AdministrativeArea):
    """A country.

    https://schema.org/Country
    """

    jsonld_type: ClassVar[str] = "Country"


class CoverArt(VisualArtwork):
    """The artwork on the outer surface of a CreativeWork.

    https://schema.org/CoverArt
    """

    jsonld_type: ClassVar[str] = "CoverArt"


class CreativeWorkSeries(CreativeWork, Series):
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.

    https://schema.org/CreativeWorkSeries
    """

    jsonld_type: ClassVar[str] = "CreativeWorkSeries"
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    issn: Annotated[str | list[str] | None, prop("issn")] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None


class Crematorium(CivicStructure):
    """A crematorium.

    https://schema.org/Crematorium
    """

    jsonld_type: ClassVar[str] = "Crematorium"


class CriticReview(Review):
    """A CriticReview is a more specialized form of Review written or published by a source that is recognized for its reviewing activities.

    https://schema.org/CriticReview
    """

    jsonld_type: ClassVar[str] = "CriticReview"


class DDxElement(MedicalIntangible):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

    https://schema.org/DDxElement
    """

    jsonld_type: ClassVar[str] = "DDxElement"
    diagnosis: Annotated[MedicalCondition | list[MedicalCondition] | None, prop("diagnosis")] = None
    distinguishing_sign: Annotated[
        MedicalSignOrSymptom | list[MedicalSignOrSymptom] | None, prop("distinguishingSign")
    ] = None


class DanceGroup(PerformingGroup):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    https://schema.org/DanceGroup
    """

    jsonld_type: ClassVar[str] = "DanceGroup"


class DataDownload(MediaObject):
    """All or part of a Dataset in downloadable form.

    https://schema.org/DataDownload
    """

    jsonld_type: ClassVar[str] = "DataDownload"
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None


class DataFeed(Dataset):
    """A single feed providing structured information about one or more entities or topics.

    https://schema.org/DataFeed
    """

    jsonld_type: ClassVar[str] = "DataFeed"
    data_feed_element: Annotated[
        str
        | DataFeedItem
        | SchemaEnumeration
        | Thing
        | list[str | DataFeedItem | SchemaEnumeration | Thing]
        | None,
        prop("dataFeedElement"),
    ] = None


class DatedMoneySpecification(StructuredValue):
    """A DatedMoneySpecification represents monetary values with optional start and end dates.

    https://schema.org/DatedMoneySpecification

    Deprecated: superseded by MonetaryAmount.
    """

    jsonld_type: ClassVar[str] = "DatedMoneySpecification"
    amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None, prop("amount")
    ] = None
    currency: Annotated[str | list[str] | None, prop("currency")] = None
    end_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("endDate")
    ] = None
    start_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("startDate")
    ] = None


class DeactivateAction(ControlAction):
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).

    https://schema.org/DeactivateAction
    """

    jsonld_type: ClassVar[str] = "DeactivateAction"


class DefinedRegion(Place, StructuredValue):
    """A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria.

    https://schema.org/DefinedRegion
    """

    jsonld_type: ClassVar[str] = "DefinedRegion"
    address_country: Annotated[
        str | Country | list[str | Country] | None, prop("addressCountry")
    ] = None
    address_region: Annotated[
        str | AdministrativeArea | list[str | AdministrativeArea] | None, prop("addressRegion")
    ] = None
    postal_code: Annotated[str | list[str] | None, prop("postalCode")] = None
    postal_code_prefix: Annotated[str | list[str] | None, prop("postalCodePrefix")] = None
    postal_code_range: Annotated[
        PostalCodeRangeSpecification | list[PostalCodeRangeSpecification] | None,
        prop("postalCodeRange"),
    ] = None


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects.

    https://schema.org/DeleteAction
    """

    jsonld_type: ClassVar[str] = "DeleteAction"


class DeliveryTimeSettings(StructuredValue):
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing.

    https://schema.org/DeliveryTimeSettings

    Deprecated: superseded by ShippingConditions.
    """

    jsonld_type: ClassVar[str] = "DeliveryTimeSettings"
    delivery_time: Annotated[
        ShippingDeliveryTime | list[ShippingDeliveryTime] | None, prop("deliveryTime")
    ] = None
    is_unlabelled_fallback: Annotated[bool | list[bool] | None, prop("isUnlabelledFallback")] = None
    shipping_destination: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingDestination")
    ] = None
    transit_time_label: Annotated[str | list[str] | None, prop("transitTimeLabel")] = None


class DepartAction(MoveAction):
    """The act of departing from a place.

    https://schema.org/DepartAction
    """

    jsonld_type: ClassVar[str] = "DepartAction"


class DiagnosticLab(MedicalOrganization):
    """A medical laboratory that offers on-site or off-site diagnostic services.

    https://schema.org/DiagnosticLab
    """

    jsonld_type: ClassVar[str] = "DiagnosticLab"
    available_test: Annotated[MedicalTest | list[MedicalTest] | None, prop("availableTest")] = None


class DiagnosticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.

    https://schema.org/DiagnosticProcedure
    """

    jsonld_type: ClassVar[str] = "DiagnosticProcedure"


class Diet(CreativeWork, LifestyleModification):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.

    https://schema.org/Diet
    """

    jsonld_type: ClassVar[str] = "Diet"
    diet_features: Annotated[str | list[str] | None, prop("dietFeatures")] = None
    endorsers: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("endorsers")
    ] = None
    expert_considerations: Annotated[str | list[str] | None, prop("expertConsiderations")] = None
    physiological_benefits: Annotated[str | list[str] | None, prop("physiologicalBenefits")] = None
    risks: Annotated[str | list[str] | None, prop("risks")] = None


class DietarySupplement(Product, Substance):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the diet.

    https://schema.org/DietarySupplement
    """

    jsonld_type: ClassVar[str] = "DietarySupplement"
    is_proprietary: Annotated[bool | list[bool] | None, prop("isProprietary")] = None
    mechanism_of_action: Annotated[str | list[str] | None, prop("mechanismOfAction")] = None
    non_proprietary_name: Annotated[str | list[str] | None, prop("nonProprietaryName")] = None
    proprietary_name: Annotated[str | list[str] | None, prop("proprietaryName")] = None
    recommended_intake: Annotated[
        RecommendedDoseSchedule | list[RecommendedDoseSchedule] | None, prop("recommendedIntake")
    ] = None
    safety_consideration: Annotated[str | list[str] | None, prop("safetyConsideration")] = None
    target_population: Annotated[str | list[str] | None, prop("targetPopulation")] = None


class DiscoverAction(FindAction):
    """The act of discovering/finding an object.

    https://schema.org/DiscoverAction
    """

    jsonld_type: ClassVar[str] = "DiscoverAction"


class DonateAction(TransferAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic reasons.

    https://schema.org/DonateAction
    """

    jsonld_type: ClassVar[str] = "DonateAction"
    price: Annotated[str | int | float | list[str | int | float] | None, prop("price")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    price_specification: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("priceSpecification")
    ] = None
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement.

    https://schema.org/DoseSchedule
    """

    jsonld_type: ClassVar[str] = "DoseSchedule"
    dose_unit: Annotated[str | list[str] | None, prop("doseUnit")] = None
    dose_value: Annotated[
        int
        | float
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[
            int | float | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue
        ]
        | None,
        prop("doseValue"),
    ] = None
    frequency: Annotated[str | list[str] | None, prop("frequency")] = None
    target_population: Annotated[str | list[str] | None, prop("targetPopulation")] = None


class DownloadAction(TransferAction):
    """The act of downloading an object.

    https://schema.org/DownloadAction
    """

    jsonld_type: ClassVar[str] = "DownloadAction"


class DrawAction(CreateAction):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

    https://schema.org/DrawAction
    """

    jsonld_type: ClassVar[str] = "DrawAction"


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids.

    https://schema.org/DrinkAction
    """

    jsonld_type: ClassVar[str] = "DrinkAction"


class Drug(Product, Substance):
    """A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism.

    https://schema.org/Drug
    """

    jsonld_type: ClassVar[str] = "Drug"
    administration_route: Annotated[str | list[str] | None, prop("administrationRoute")] = None
    alcohol_warning: Annotated[str | list[str] | None, prop("alcoholWarning")] = None
    available_strength: Annotated[
        DrugStrength | list[DrugStrength] | None, prop("availableStrength")
    ] = None
    breastfeeding_warning: Annotated[str | list[str] | None, prop("breastfeedingWarning")] = None
    clincal_pharmacology: Annotated[
        str | list[str] | None, prop("clincalPharmacology", superseded_by=("clinicalPharmacology",))
    ] = None
    clinical_pharmacology: Annotated[str | list[str] | None, prop("clinicalPharmacology")] = None
    dosage_form: Annotated[str | list[str] | None, prop("dosageForm")] = None
    dose_schedule: Annotated[DoseSchedule | list[DoseSchedule] | None, prop("doseSchedule")] = None
    drug_class: Annotated[DrugClass | list[DrugClass] | None, prop("drugClass")] = None
    drug_unit: Annotated[str | list[str] | None, prop("drugUnit")] = None
    food_warning: Annotated[str | list[str] | None, prop("foodWarning")] = None
    interacting_drug: Annotated[Drug | list[Drug] | None, prop("interactingDrug")] = None
    is_available_generically: Annotated[
        bool | list[bool] | None, prop("isAvailableGenerically")
    ] = None
    is_proprietary: Annotated[bool | list[bool] | None, prop("isProprietary")] = None
    label_details: Annotated[str | list[str] | None, prop("labelDetails")] = None
    mechanism_of_action: Annotated[str | list[str] | None, prop("mechanismOfAction")] = None
    non_proprietary_name: Annotated[str | list[str] | None, prop("nonProprietaryName")] = None
    overdosage: Annotated[str | list[str] | None, prop("overdosage")] = None
    pregnancy_category: Annotated[
        DrugPregnancyCategory | list[DrugPregnancyCategory] | None, prop("pregnancyCategory")
    ] = None
    pregnancy_warning: Annotated[str | list[str] | None, prop("pregnancyWarning")] = None
    prescribing_info: Annotated[str | list[str] | None, prop("prescribingInfo")] = None
    prescription_status: Annotated[
        str | DrugPrescriptionStatus | list[str | DrugPrescriptionStatus] | None,
        prop("prescriptionStatus"),
    ] = None
    proprietary_name: Annotated[str | list[str] | None, prop("proprietaryName")] = None
    related_drug: Annotated[Drug | list[Drug] | None, prop("relatedDrug")] = None
    warning: Annotated[str | list[str] | None, prop("warning")] = None


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    https://schema.org/DrugLegalStatus
    """

    jsonld_type: ClassVar[str] = "DrugLegalStatus"
    applicable_location: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("applicableLocation")
    ] = None


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country.

    https://schema.org/DrugStrength
    """

    jsonld_type: ClassVar[str] = "DrugStrength"
    active_ingredient: Annotated[str | list[str] | None, prop("activeIngredient")] = None
    available_in: Annotated[
        AdministrativeArea | list[AdministrativeArea] | None, prop("availableIn")
    ] = None
    maximum_intake: Annotated[
        MaximumDoseSchedule | list[MaximumDoseSchedule] | None, prop("maximumIntake")
    ] = None
    strength_unit: Annotated[str | list[str] | None, prop("strengthUnit")] = None
    strength_value: Annotated[int | float | list[int | float] | None, prop("strengthValue")] = None


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    https://schema.org/DryCleaningOrLaundry
    """

    jsonld_type: ClassVar[str] = "DryCleaningOrLaundry"


class EatAction(ConsumeAction):
    """The act of swallowing solid objects.

    https://schema.org/EatAction
    """

    jsonld_type: ClassVar[str] = "EatAction"


class EducationalAudience(Audience):
    """An EducationalAudience.

    https://schema.org/EducationalAudience
    """

    jsonld_type: ClassVar[str] = "EducationalAudience"
    educational_role: Annotated[str | list[str] | None, prop("educationalRole")] = None


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization.

    https://schema.org/EducationalOrganization
    """

    jsonld_type: ClassVar[str] = "EducationalOrganization"


class EmailMessage(Message):
    """An email message.

    https://schema.org/EmailMessage
    """

    jsonld_type: ClassVar[str] = "EmailMessage"


class EmergencyService(LocalBusiness):
    """An emergency service, such as a fire station or ER.

    https://schema.org/EmergencyService
    """

    jsonld_type: ClassVar[str] = "EmergencyService"


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    https://schema.org/EmploymentAgency
    """

    jsonld_type: ClassVar[str] = "EmploymentAgency"


class EndorsementRating(Rating):
    """An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a "Like" or "+1" on a social network.

    https://schema.org/EndorsementRating
    """

    jsonld_type: ClassVar[str] = "EndorsementRating"


class EnergyEfficiencyEnumeration(Enumeration):
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

    https://schema.org/EnergyEfficiencyEnumeration
    """

    jsonld_type: ClassVar[str] = "EnergyEfficiencyEnumeration"


class EngineSpecification(StructuredValue):
    """Information about the engine of the vehicle.

    https://schema.org/EngineSpecification
    """

    jsonld_type: ClassVar[str] = "EngineSpecification"
    engine_displacement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("engineDisplacement")
    ] = None
    engine_power: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("enginePower")
    ] = None
    engine_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("engineType"),
    ] = None
    fuel_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("fuelType"),
    ] = None
    torque: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("torque")] = None


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    https://schema.org/EntertainmentBusiness
    """

    jsonld_type: ClassVar[str] = "EntertainmentBusiness"


class EventReservation(Reservation):
    """A reservation for an event like a concert, sporting event, or lecture.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/EventReservation
    """

    jsonld_type: ClassVar[str] = "EventReservation"


class EventSeries(Event, Series):
    """A series of Events.

    https://schema.org/EventSeries
    """

    jsonld_type: ClassVar[str] = "EventSeries"


class EventVenue(CivicStructure):
    """An event venue.

    https://schema.org/EventVenue
    """

    jsonld_type: ClassVar[str] = "EventVenue"


class ExchangeRateSpecification(StructuredValue):
    """A structured value representing exchange rate.

    https://schema.org/ExchangeRateSpecification
    """

    jsonld_type: ClassVar[str] = "ExchangeRateSpecification"
    currency: Annotated[str | list[str] | None, prop("currency")] = None
    current_exchange_rate: Annotated[
        UnitPriceSpecification | list[UnitPriceSpecification] | None, prop("currentExchangeRate")
    ] = None
    exchange_rate_spread: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None,
        prop("exchangeRateSpread"),
    ] = None


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and fitness.

    https://schema.org/ExerciseAction
    """

    jsonld_type: ClassVar[str] = "ExerciseAction"
    course: Annotated[
        Place | list[Place] | None, prop("course", superseded_by=("exerciseCourse",))
    ] = None
    diet: Annotated[Diet | list[Diet] | None, prop("diet")] = None
    distance: Annotated[str | list[str] | None, prop("distance")] = None
    exercise_course: Annotated[Place | list[Place] | None, prop("exerciseCourse")] = None
    exercise_plan: Annotated[ExercisePlan | list[ExercisePlan] | None, prop("exercisePlan")] = None
    exercise_related_diet: Annotated[Diet | list[Diet] | None, prop("exerciseRelatedDiet")] = None
    exercise_type: Annotated[str | list[str] | None, prop("exerciseType")] = None
    from_location: Annotated[Place | list[Place] | None, prop("fromLocation")] = None
    opponent: Annotated[Person | list[Person] | None, prop("opponent")] = None
    sports_activity_location: Annotated[
        SportsActivityLocation | list[SportsActivityLocation] | None, prop("sportsActivityLocation")
    ] = None
    sports_event: Annotated[SportsEvent | list[SportsEvent] | None, prop("sportsEvent")] = None
    sports_team: Annotated[SportsTeam | list[SportsTeam] | None, prop("sportsTeam")] = None
    to_location: Annotated[Place | list[Place] | None, prop("toLocation")] = None


class FAQPage(WebPage):
    """A FAQPage is a WebPage presenting one or more "Frequently asked questions" (see also QAPage).

    https://schema.org/FAQPage
    """

    jsonld_type: ClassVar[str] = "FAQPage"


class FilmAction(CreateAction):
    """The act of capturing sound and moving images on film, video, or digitally.

    https://schema.org/FilmAction
    """

    jsonld_type: ClassVar[str] = "FilmAction"


class FinancialProduct(Service):
    """A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.

    https://schema.org/FinancialProduct
    """

    jsonld_type: ClassVar[str] = "FinancialProduct"
    annual_percentage_rate: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("annualPercentageRate"),
    ] = None
    fees_and_commissions_specification: Annotated[
        str | list[str] | None, prop("feesAndCommissionsSpecification")
    ] = None
    interest_rate: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("interestRate"),
    ] = None


class FinancialService(LocalBusiness):
    """Financial services business.

    https://schema.org/FinancialService
    """

    jsonld_type: ClassVar[str] = "FinancialService"
    fees_and_commissions_specification: Annotated[
        str | list[str] | None, prop("feesAndCommissionsSpecification")
    ] = None


class Flight(Trip):
    """An airline flight.

    https://schema.org/Flight
    """

    jsonld_type: ClassVar[str] = "Flight"
    aircraft: Annotated[str | Vehicle | list[str | Vehicle] | None, prop("aircraft")] = None
    arrival_airport: Annotated[Airport | list[Airport] | None, prop("arrivalAirport")] = None
    arrival_gate: Annotated[str | list[str] | None, prop("arrivalGate")] = None
    arrival_terminal: Annotated[str | list[str] | None, prop("arrivalTerminal")] = None
    boarding_policy: Annotated[
        BoardingPolicyType | list[BoardingPolicyType] | None, prop("boardingPolicy")
    ] = None
    carrier: Annotated[
        Organization | list[Organization] | None, prop("carrier", superseded_by=("provider",))
    ] = None
    departure_airport: Annotated[Airport | list[Airport] | None, prop("departureAirport")] = None
    departure_gate: Annotated[str | list[str] | None, prop("departureGate")] = None
    departure_terminal: Annotated[str | list[str] | None, prop("departureTerminal")] = None
    estimated_flight_duration: Annotated[
        str | list[str] | None, prop("estimatedFlightDuration")
    ] = None
    flight_distance: Annotated[str | list[str] | None, prop("flightDistance")] = None
    flight_number: Annotated[str | list[str] | None, prop("flightNumber")] = None
    meal_service: Annotated[str | list[str] | None, prop("mealService")] = None
    seller: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("seller")
    ] = None
    web_checkin_time: Annotated[
        _dt.datetime | list[_dt.datetime] | None, prop("webCheckinTime")
    ] = None


class FlightReservation(Reservation):
    """A reservation for air travel.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/FlightReservation
    """

    jsonld_type: ClassVar[str] = "FlightReservation"
    boarding_group: Annotated[str | list[str] | None, prop("boardingGroup")] = None
    passenger_priority_status: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("passengerPriorityStatus"),
    ] = None
    passenger_sequence_number: Annotated[
        str | list[str] | None, prop("passengerSequenceNumber")
    ] = None
    security_screening: Annotated[str | list[str] | None, prop("securityScreening")] = None


class FollowAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.\\n\\nRelated actions:\\n\\n* BefriendAction: Unlike BefriendAction, FollowAction implies that the connection...

    https://schema.org/FollowAction
    """

    jsonld_type: ClassVar[str] = "FollowAction"
    followee: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("followee")
    ] = None


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    https://schema.org/FoodEstablishment
    """

    jsonld_type: ClassVar[str] = "FoodEstablishment"
    accepts_reservations: Annotated[
        str | bool | list[str | bool] | None, prop("acceptsReservations")
    ] = None
    has_menu: Annotated[str | Menu | list[str | Menu] | None, prop("hasMenu")] = None
    menu: Annotated[
        str | Menu | list[str | Menu] | None, prop("menu", superseded_by=("hasMenu",))
    ] = None
    serves_cuisine: Annotated[str | list[str] | None, prop("servesCuisine")] = None
    star_rating: Annotated[Rating | list[Rating] | None, prop("starRating")] = None


class FoodEstablishmentReservation(Reservation):
    """A reservation to dine at a food-related business.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/FoodEstablishmentReservation
    """

    jsonld_type: ClassVar[str] = "FoodEstablishmentReservation"
    end_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("endTime")
    ] = None
    party_size: Annotated[
        int | QuantitativeValue | list[int | QuantitativeValue] | None, prop("partySize")
    ] = None
    start_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("startTime")
    ] = None


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner.

    https://schema.org/FoodService
    """

    jsonld_type: ClassVar[str] = "FoodService"


class FundingAgency(Project):
    """A FundingAgency is an organization that implements one or more FundingSchemes and manages the granting process (via Grants, typically MonetaryGrants).

    https://schema.org/FundingAgency
    """

    jsonld_type: ClassVar[str] = "FundingAgency"


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community.

    https://schema.org/GatedResidenceCommunity
    """

    jsonld_type: ClassVar[str] = "GatedResidenceCommunity"


class GeoCoordinates(StructuredValue):
    """The geographic coordinates of a place or event.

    https://schema.org/GeoCoordinates
    """

    jsonld_type: ClassVar[str] = "GeoCoordinates"
    address: Annotated[str | PostalAddress | list[str | PostalAddress] | None, prop("address")] = (
        None
    )
    address_country: Annotated[
        str | Country | list[str | Country] | None, prop("addressCountry")
    ] = None
    elevation: Annotated[str | int | float | list[str | int | float] | None, prop("elevation")] = (
        None
    )
    latitude: Annotated[str | int | float | list[str | int | float] | None, prop("latitude")] = None
    longitude: Annotated[str | int | float | list[str | int | float] | None, prop("longitude")] = (
        None
    )
    postal_code: Annotated[str | list[str] | None, prop("postalCode")] = None


class GeoShape(StructuredValue):
    """The geographic shape of a place.

    https://schema.org/GeoShape
    """

    jsonld_type: ClassVar[str] = "GeoShape"
    address: Annotated[str | PostalAddress | list[str | PostalAddress] | None, prop("address")] = (
        None
    )
    address_country: Annotated[
        str | Country | list[str | Country] | None, prop("addressCountry")
    ] = None
    box: Annotated[str | list[str] | None, prop("box")] = None
    circle: Annotated[str | list[str] | None, prop("circle")] = None
    elevation: Annotated[str | int | float | list[str | int | float] | None, prop("elevation")] = (
        None
    )
    line: Annotated[str | list[str] | None, prop("line")] = None
    polygon: Annotated[str | list[str] | None, prop("polygon")] = None
    postal_code: Annotated[str | list[str] | None, prop("postalCode")] = None


class GiveAction(TransferAction):
    """The act of transferring ownership of an object to a destination.

    https://schema.org/GiveAction
    """

    jsonld_type: ClassVar[str] = "GiveAction"
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class GovernmentBuilding(CivicStructure):
    """A government building.

    https://schema.org/GovernmentBuilding
    """

    jsonld_type: ClassVar[str] = "GovernmentBuilding"


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office.

    https://schema.org/GovernmentOffice
    """

    jsonld_type: ClassVar[str] = "GovernmentOffice"


class GovernmentPermit(Permit):
    """A permit issued by a government agency.

    https://schema.org/GovernmentPermit
    """

    jsonld_type: ClassVar[str] = "GovernmentPermit"


class GovernmentService(Service):
    """A service provided by a government organization, e.g. food stamps, veterans benefits, etc.

    https://schema.org/GovernmentService
    """

    jsonld_type: ClassVar[str] = "GovernmentService"
    jurisdiction: Annotated[
        str | AdministrativeArea | list[str | AdministrativeArea] | None, prop("jurisdiction")
    ] = None
    service_operator: Annotated[
        Organization | list[Organization] | None, prop("serviceOperator")
    ] = None


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    https://schema.org/HealthAndBeautyBusiness
    """

    jsonld_type: ClassVar[str] = "HealthAndBeautyBusiness"


class HomeAndConstructionBusiness(LocalBusiness):
    """A construction business.\\n\\nA HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.\\n\\nAs a LocalBusiness it can be described as a provider of one or more Service\\(s).

    https://schema.org/HomeAndConstructionBusiness
    """

    jsonld_type: ClassVar[str] = "HomeAndConstructionBusiness"


class House(Accommodation):
    """A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/House).

    https://schema.org/House
    """

    jsonld_type: ClassVar[str] = "House"


class HowToDirection(CreativeWork, ListItem):
    """A direction indicating a single action to do in the instructions for how to achieve a result.

    https://schema.org/HowToDirection
    """

    jsonld_type: ClassVar[str] = "HowToDirection"
    after_media: Annotated[
        str | MediaObject | list[str | MediaObject] | None, prop("afterMedia")
    ] = None
    before_media: Annotated[
        str | MediaObject | list[str | MediaObject] | None, prop("beforeMedia")
    ] = None
    during_media: Annotated[
        str | MediaObject | list[str | MediaObject] | None, prop("duringMedia")
    ] = None
    perform_time: Annotated[str | list[str] | None, prop("performTime")] = None
    prep_time: Annotated[str | list[str] | None, prop("prepTime")] = None
    supply: Annotated[str | HowToSupply | list[str | HowToSupply] | None, prop("supply")] = None
    tool: Annotated[str | HowToTool | list[str | HowToTool] | None, prop("tool")] = None
    total_time: Annotated[str | list[str] | None, prop("totalTime")] = None


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to achieve a result.

    https://schema.org/HowToItem
    """

    jsonld_type: ClassVar[str] = "HowToItem"
    required_quantity: Annotated[
        str | int | float | QuantitativeValue | list[str | int | float | QuantitativeValue] | None,
        prop("requiredQuantity"),
    ] = None


class HowToSection(CreativeWork, ItemList, ListItem):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).

    https://schema.org/HowToSection
    """

    jsonld_type: ClassVar[str] = "HowToSection"
    steps: Annotated[
        str | CreativeWork | ItemList | list[str | CreativeWork | ItemList] | None,
        prop("steps", superseded_by=("step",)),
    ] = None


class HowToStep(CreativeWork, ItemList, ListItem):
    """A step in the instructions for how to achieve a result.

    https://schema.org/HowToStep
    """

    jsonld_type: ClassVar[str] = "HowToStep"


class HowToTip(CreativeWork, ListItem):
    """An explanation in the instructions for how to achieve a result.

    https://schema.org/HowToTip
    """

    jsonld_type: ClassVar[str] = "HowToTip"


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object.

    https://schema.org/IgnoreAction
    """

    jsonld_type: ClassVar[str] = "IgnoreAction"


class ImageObject(MediaObject):
    """An image file.

    https://schema.org/ImageObject
    """

    jsonld_type: ClassVar[str] = "ImageObject"
    caption: Annotated[str | MediaObject | list[str | MediaObject] | None, prop("caption")] = None
    embedded_text_caption: Annotated[str | list[str] | None, prop("embeddedTextCaption")] = None
    exif_data: Annotated[
        str | PropertyValue | list[str | PropertyValue] | None, prop("exifData")
    ] = None
    representative_of_page: Annotated[bool | list[bool] | None, prop("representativeOfPage")] = None


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes.

    https://schema.org/ImagingTest
    """

    jsonld_type: ClassVar[str] = "ImagingTest"
    imaging_technique: Annotated[
        MedicalImagingTechnique | list[MedicalImagingTechnique] | None, prop("imagingTechnique")
    ] = None


class InfectiousDisease(MedicalCondition):
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions.

    https://schema.org/InfectiousDisease
    """

    jsonld_type: ClassVar[str] = "InfectiousDisease"
    infectious_agent: Annotated[str | list[str] | None, prop("infectiousAgent")] = None
    infectious_agent_class: Annotated[
        InfectiousAgentClass | list[InfectiousAgentClass] | None, prop("infectiousAgentClass")
    ] = None
    transmission_method: Annotated[str | list[str] | None, prop("transmissionMethod")] = None


class InstallAction(ConsumeAction):
    """The act of installing an application.

    https://schema.org/InstallAction
    """

    jsonld_type: ClassVar[str] = "InstallAction"


class InteractionCounter(StructuredValue):
    """A summary of how users have interacted with this CreativeWork.

    https://schema.org/InteractionCounter
    """

    jsonld_type: ClassVar[str] = "InteractionCounter"
    end_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("endTime")
    ] = None
    interaction_service: Annotated[
        SoftwareApplication | WebSite | list[SoftwareApplication | WebSite] | None,
        prop("interactionService"),
    ] = None
    interaction_type: Annotated[Action | list[Action] | None, prop("interactionType")] = None
    location: Annotated[
        str
        | Place
        | PostalAddress
        | VirtualLocation
        | list[str | Place | PostalAddress | VirtualLocation]
        | None,
        prop("location"),
    ] = None
    start_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("startTime")
    ] = None
    user_interaction_count: Annotated[int | list[int] | None, prop("userInteractionCount")] = None


class InternetCafe(LocalBusiness):
    """An internet cafe.

    https://schema.org/InternetCafe
    """

    jsonld_type: ClassVar[str] = "InternetCafe"


class ItemPage(WebPage):
    """A page devoted to a single item, such as a particular product or hotel.

    https://schema.org/ItemPage
    """

    jsonld_type: ClassVar[str] = "ItemPage"


class JoinAction(InteractAction):
    """An agent joins an event/group with participants/friends at a location.\\n\\nRelated actions:\\n\\n* RegisterAction: Unlike RegisterAction, JoinAction refers to joining a group/team of people.\\n* SubscribeAction: Unlike SubscribeAction, JoinA...

    https://schema.org/JoinAction
    """

    jsonld_type: ClassVar[str] = "JoinAction"
    event: Annotated[Event | list[Event] | None, prop("event")] = None


class Joint(AnatomicalStructure):
    """The anatomical location at which two or more bones make contact.

    https://schema.org/Joint
    """

    jsonld_type: ClassVar[str] = "Joint"
    biomechnical_class: Annotated[str | list[str] | None, prop("biomechnicalClass")] = None
    functional_class: Annotated[
        str | MedicalEntity | PhysicalExam | list[str | MedicalEntity | PhysicalExam] | None,
        prop("functionalClass"),
    ] = None
    structural_class: Annotated[str | list[str] | None, prop("structuralClass")] = None


class LeaveAction(InteractAction):
    """An agent leaves an event / group with participants/friends at a location.\\n\\nRelated actions:\\n\\n* JoinAction: The antonym of LeaveAction.\\n* UnRegisterAction: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people r...

    https://schema.org/LeaveAction
    """

    jsonld_type: ClassVar[str] = "LeaveAction"
    event: Annotated[Event | list[Event] | None, prop("event")] = None


class LegalService(LocalBusiness):
    """A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.\\n\\nAs a LocalBusiness it can be described as a provider of one or more Service\\(s).

    https://schema.org/LegalService
    """

    jsonld_type: ClassVar[str] = "LegalService"


class LegislationObject(Legislation, MediaObject):
    """A specific object or file containing a Legislation.

    https://schema.org/LegislationObject
    """

    jsonld_type: ClassVar[str] = "LegislationObject"
    legislation_legal_value: Annotated[
        LegalValueLevel | list[LegalValueLevel] | None, prop("legislationLegalValue")
    ] = None


class LendAction(TransferAction):
    """The act of providing an object under an agreement that it will be returned at a later date.

    https://schema.org/LendAction
    """

    jsonld_type: ClassVar[str] = "LendAction"
    borrower: Annotated[Person | list[Person] | None, prop("borrower")] = None


class Library(LocalBusiness):
    """A library.

    https://schema.org/Library
    """

    jsonld_type: ClassVar[str] = "Library"


class Ligament(AnatomicalStructure):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.

    https://schema.org/Ligament
    """

    jsonld_type: ClassVar[str] = "Ligament"


class LinkRole(Role):
    """A Role that represents a Web link, e.g. as expressed via the 'url' property.

    https://schema.org/LinkRole
    """

    jsonld_type: ClassVar[str] = "LinkRole"
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    link_relationship: Annotated[str | list[str] | None, prop("linkRelationship")] = None


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    https://schema.org/ListenAction
    """

    jsonld_type: ClassVar[str] = "ListenAction"


class LodgingBusiness(LocalBusiness):
    """A lodging business, such as a motel, hotel, or inn.

    https://schema.org/LodgingBusiness
    """

    jsonld_type: ClassVar[str] = "LodgingBusiness"
    audience: Annotated[Audience | list[Audience] | None, prop("audience")] = None
    available_language: Annotated[
        str | Language | list[str | Language] | None, prop("availableLanguage")
    ] = None
    checkin_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("checkinTime")
    ] = None
    checkout_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("checkoutTime")
    ] = None
    number_of_rooms: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("numberOfRooms"),
    ] = None
    pets_allowed: Annotated[str | bool | list[str | bool] | None, prop("petsAllowed")] = None
    star_rating: Annotated[Rating | list[Rating] | None, prop("starRating")] = None


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/LodgingReservation
    """

    jsonld_type: ClassVar[str] = "LodgingReservation"
    checkin_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("checkinTime")
    ] = None
    checkout_time: Annotated[
        _dt.datetime | _dt.time | list[_dt.datetime | _dt.time] | None, prop("checkoutTime")
    ] = None
    lodging_unit_description: Annotated[str | list[str] | None, prop("lodgingUnitDescription")] = (
        None
    )
    lodging_unit_type: Annotated[
        str
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[str | DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("lodgingUnitType"),
    ] = None
    num_adults: Annotated[
        int | QuantitativeValue | list[int | QuantitativeValue] | None, prop("numAdults")
    ] = None
    num_children: Annotated[
        int | QuantitativeValue | list[int | QuantitativeValue] | None, prop("numChildren")
    ] = None


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity.

    https://schema.org/LoseAction
    """

    jsonld_type: ClassVar[str] = "LoseAction"
    winner: Annotated[Person | list[Person] | None, prop("winner")] = None


class MarryAction(InteractAction):
    """The act of marrying a person.

    https://schema.org/MarryAction
    """

    jsonld_type: ClassVar[str] = "MarryAction"


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.

    https://schema.org/MeasurementTypeEnumeration
    """

    jsonld_type: ClassVar[str] = "MeasurementTypeEnumeration"


class MediaEnumeration(Enumeration):
    """MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects.

    https://schema.org/MediaEnumeration
    """

    jsonld_type: ClassVar[str] = "MediaEnumeration"


class MediaReview(Review):
    """A MediaReview is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.

    https://schema.org/MediaReview
    """

    jsonld_type: ClassVar[str] = "MediaReview"
    media_authenticity_category: Annotated[
        MediaManipulationRatingEnumeration | list[MediaManipulationRatingEnumeration] | None,
        prop("mediaAuthenticityCategory"),
    ] = None
    original_media_context_description: Annotated[
        str | list[str] | None, prop("originalMediaContextDescription")
    ] = None
    original_media_link: Annotated[
        str | MediaObject | WebPage | list[str | MediaObject | WebPage] | None,
        prop("originalMediaLink"),
    ] = None


class MedicalBusiness(LocalBusiness):
    """A particular physical or virtual business of an organization for medical purposes.

    https://schema.org/MedicalBusiness
    """

    jsonld_type: ClassVar[str] = "MedicalBusiness"


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    https://schema.org/MedicalConditionStage
    """

    jsonld_type: ClassVar[str] = "MedicalConditionStage"
    stage_as_number: Annotated[int | float | list[int | float] | None, prop("stageAsNumber")] = None
    sub_stage_suffix: Annotated[str | list[str] | None, prop("subStageSuffix")] = None


class MedicalEnumeration(Enumeration):
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.

    https://schema.org/MedicalEnumeration
    """

    jsonld_type: ClassVar[str] = "MedicalEnumeration"


class MedicalGuidelineContraindication(MedicalGuideline):
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.

    https://schema.org/MedicalGuidelineContraindication
    """

    jsonld_type: ClassVar[str] = "MedicalGuidelineContraindication"


class MedicalGuidelineRecommendation(MedicalGuideline):
    """A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.

    https://schema.org/MedicalGuidelineRecommendation
    """

    jsonld_type: ClassVar[str] = "MedicalGuidelineRecommendation"
    recommendation_strength: Annotated[str | list[str] | None, prop("recommendationStrength")] = (
        None
    )


class MedicalObservationalStudy(MedicalStudy):
    """An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time.

    https://schema.org/MedicalObservationalStudy
    """

    jsonld_type: ClassVar[str] = "MedicalObservationalStudy"
    study_design: Annotated[
        MedicalObservationalStudyDesign | list[MedicalObservationalStudyDesign] | None,
        prop("studyDesign"),
    ] = None


class MedicalRiskCalculator(MedicalRiskEstimator):
    """A complex mathematical calculation requiring an online calculator, used to assess prognosis.

    https://schema.org/MedicalRiskCalculator
    """

    jsonld_type: ClassVar[str] = "MedicalRiskCalculator"


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.

    https://schema.org/MedicalRiskScore
    """

    jsonld_type: ClassVar[str] = "MedicalRiskScore"
    algorithm: Annotated[str | list[str] | None, prop("algorithm")] = None


class MedicalSignOrSymptom(MedicalCondition):
    """Any feature associated or not with a medical condition.

    https://schema.org/MedicalSignOrSymptom
    """

    jsonld_type: ClassVar[str] = "MedicalSignOrSymptom"


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    https://schema.org/MedicalTestPanel
    """

    jsonld_type: ClassVar[str] = "MedicalTestPanel"
    sub_test: Annotated[MedicalTest | list[MedicalTest] | None, prop("subTest")] = None


class MedicalTrial(MedicalStudy):
    """A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures.

    https://schema.org/MedicalTrial
    """

    jsonld_type: ClassVar[str] = "MedicalTrial"
    trial_design: Annotated[
        MedicalTrialDesign | list[MedicalTrialDesign] | None, prop("trialDesign")
    ] = None


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    https://schema.org/MedicalWebPage
    """

    jsonld_type: ClassVar[str] = "MedicalWebPage"
    aspect: Annotated[
        str | list[str] | None, prop("aspect", superseded_by=("mainContentOfPage",))
    ] = None
    medical_audience: Annotated[
        MedicalAudience | MedicalAudienceType | list[MedicalAudience | MedicalAudienceType] | None,
        prop("medicalAudience"),
    ] = None


class MobileApplication(SoftwareApplication):
    """A software application designed specifically to work well on a mobile device such as a telephone.

    https://schema.org/MobileApplication
    """

    jsonld_type: ClassVar[str] = "MobileApplication"
    carrier_requirements: Annotated[str | list[str] | None, prop("carrierRequirements")] = None


class MonetaryAmount(StructuredValue):
    """A monetary value or range.

    https://schema.org/MonetaryAmount
    """

    jsonld_type: ClassVar[str] = "MonetaryAmount"
    currency: Annotated[str | list[str] | None, prop("currency")] = None
    max_value: Annotated[int | float | list[int | float] | None, prop("maxValue")] = None
    min_value: Annotated[int | float | list[int | float] | None, prop("minValue")] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None
    value: Annotated[
        str
        | bool
        | int
        | float
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | StructuredValue
        | list[
            str
            | bool
            | int
            | float
            | DriveWheelConfigurationValue
            | QualitativeValue
            | SteeringPositionValue
            | StructuredValue
        ]
        | None,
        prop("value"),
    ] = None


class MonetaryGrant(Grant):
    """A monetary grant.

    https://schema.org/MonetaryGrant
    """

    jsonld_type: ClassVar[str] = "MonetaryGrant"
    amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None, prop("amount")
    ] = None


class MoneyTransfer(TransferAction):
    """The act of transferring money from one place to another place.

    https://schema.org/MoneyTransfer
    """

    jsonld_type: ClassVar[str] = "MoneyTransfer"
    amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None, prop("amount")
    ] = None
    beneficiary_bank: Annotated[
        str | BankOrCreditUnion | list[str | BankOrCreditUnion] | None, prop("beneficiaryBank")
    ] = None


class Motorcycle(Vehicle):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    https://schema.org/Motorcycle
    """

    jsonld_type: ClassVar[str] = "Motorcycle"


class MotorizedBicycle(Vehicle):
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.

    https://schema.org/MotorizedBicycle
    """

    jsonld_type: ClassVar[str] = "MotorizedBicycle"


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest.

    https://schema.org/Mountain
    """

    jsonld_type: ClassVar[str] = "Mountain"


class MovieClip(Clip):
    """A short segment/part of a movie.

    https://schema.org/MovieClip
    """

    jsonld_type: ClassVar[str] = "MovieClip"


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.

    https://schema.org/Muscle
    """

    jsonld_type: ClassVar[str] = "Muscle"
    antagonist: Annotated[Muscle | list[Muscle] | None, prop("antagonist")] = None
    blood_supply: Annotated[Vessel | list[Vessel] | None, prop("bloodSupply")] = None
    insertion: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("insertion")
    ] = None
    muscle_action: Annotated[str | list[str] | None, prop("muscleAction")] = None
    nerve: Annotated[Nerve | list[Nerve] | None, prop("nerve")] = None


class Museum(CivicStructure):
    """A museum.

    https://schema.org/Museum
    """

    jsonld_type: ClassVar[str] = "Museum"


class MusicAlbum(MusicPlaylist):
    """A collection of music tracks.

    https://schema.org/MusicAlbum
    """

    jsonld_type: ClassVar[str] = "MusicAlbum"
    album_production_type: Annotated[
        MusicAlbumProductionType | list[MusicAlbumProductionType] | None,
        prop("albumProductionType"),
    ] = None
    album_release: Annotated[MusicRelease | list[MusicRelease] | None, prop("albumRelease")] = None
    album_release_type: Annotated[
        MusicAlbumReleaseType | list[MusicAlbumReleaseType] | None, prop("albumReleaseType")
    ] = None
    by_artist: Annotated[
        MusicGroup | Person | list[MusicGroup | Person] | None, prop("byArtist")
    ] = None


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir.

    https://schema.org/MusicGroup
    """

    jsonld_type: ClassVar[str] = "MusicGroup"
    album: Annotated[MusicAlbum | list[MusicAlbum] | None, prop("album")] = None
    albums: Annotated[
        MusicAlbum | list[MusicAlbum] | None, prop("albums", superseded_by=("album",))
    ] = None
    genre: Annotated[str | DefinedTerm | list[str | DefinedTerm] | None, prop("genre")] = None
    music_group_member: Annotated[
        Person | list[Person] | None, prop("musicGroupMember", superseded_by=("member",))
    ] = None
    track: Annotated[
        ItemList | MusicRecording | list[ItemList | MusicRecording] | None, prop("track")
    ] = None
    tracks: Annotated[
        MusicRecording | list[MusicRecording] | None, prop("tracks", superseded_by=("track",))
    ] = None


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album.

    https://schema.org/MusicRelease
    """

    jsonld_type: ClassVar[str] = "MusicRelease"
    catalog_number: Annotated[str | list[str] | None, prop("catalogNumber")] = None
    credited_to: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("creditedTo")
    ] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    music_release_format: Annotated[
        MusicReleaseFormatType | list[MusicReleaseFormatType] | None, prop("musicReleaseFormat")
    ] = None
    record_label: Annotated[Organization | list[Organization] | None, prop("recordLabel")] = None
    release_of: Annotated[MusicAlbum | list[MusicAlbum] | None, prop("releaseOf")] = None


class MusicVenue(CivicStructure):
    """A music venue.

    https://schema.org/MusicVenue
    """

    jsonld_type: ClassVar[str] = "MusicVenue"


class MusicVideoObject(MediaObject):
    """A music video file.

    https://schema.org/MusicVideoObject
    """

    jsonld_type: ClassVar[str] = "MusicVideoObject"


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.

    https://schema.org/Nerve
    """

    jsonld_type: ClassVar[str] = "Nerve"
    branch: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None,
        prop("branch", superseded_by=("arterialBranch",)),
    ] = None
    nerve_motor: Annotated[Muscle | list[Muscle] | None, prop("nerveMotor")] = None
    sensory_unit: Annotated[
        AnatomicalStructure
        | SuperficialAnatomy
        | list[AnatomicalStructure | SuperficialAnatomy]
        | None,
        prop("sensoryUnit"),
    ] = None
    sourced_from: Annotated[BrainStructure | list[BrainStructure] | None, prop("sourcedFrom")] = (
        None
    )


class NewsArticle(Article):
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

    https://schema.org/NewsArticle
    """

    jsonld_type: ClassVar[str] = "NewsArticle"
    dateline: Annotated[str | list[str] | None, prop("dateline")] = None
    print_column: Annotated[str | list[str] | None, prop("printColumn")] = None
    print_edition: Annotated[str | list[str] | None, prop("printEdition")] = None
    print_page: Annotated[str | list[str] | None, prop("printPage")] = None
    print_section: Annotated[str | list[str] | None, prop("printSection")] = None


class NonprofitType(Enumeration):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.

    https://schema.org/NonprofitType
    """

    jsonld_type: ClassVar[str] = "NonprofitType"


class NoteDigitalDocument(DigitalDocument):
    """A file containing a note, primarily for the author.

    https://schema.org/NoteDigitalDocument
    """

    jsonld_type: ClassVar[str] = "NoteDigitalDocument"


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    https://schema.org/NutritionInformation
    """

    jsonld_type: ClassVar[str] = "NutritionInformation"
    calories: Annotated[str | list[str] | None, prop("calories")] = None
    carbohydrate_content: Annotated[str | list[str] | None, prop("carbohydrateContent")] = None
    cholesterol_content: Annotated[str | list[str] | None, prop("cholesterolContent")] = None
    fat_content: Annotated[str | list[str] | None, prop("fatContent")] = None
    fiber_content: Annotated[str | list[str] | None, prop("fiberContent")] = None
    protein_content: Annotated[str | list[str] | None, prop("proteinContent")] = None
    saturated_fat_content: Annotated[str | list[str] | None, prop("saturatedFatContent")] = None
    serving_size: Annotated[str | list[str] | None, prop("servingSize")] = None
    sodium_content: Annotated[str | list[str] | None, prop("sodiumContent")] = None
    sugar_content: Annotated[str | list[str] | None, prop("sugarContent")] = None
    trans_fat_content: Annotated[str | list[str] | None, prop("transFatContent")] = None
    unsaturated_fat_content: Annotated[str | list[str] | None, prop("unsaturatedFatContent")] = None


class OfferCatalog(ItemList):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.

    https://schema.org/OfferCatalog
    """

    jsonld_type: ClassVar[str] = "OfferCatalog"


class OfferShippingDetails(StructuredValue):
    """OfferShippingDetails represents information about shipping destinations.

    https://schema.org/OfferShippingDetails
    """

    jsonld_type: ClassVar[str] = "OfferShippingDetails"
    delivery_time: Annotated[
        ShippingDeliveryTime | list[ShippingDeliveryTime] | None, prop("deliveryTime")
    ] = None
    depth: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("depth")
    ] = None
    does_not_ship: Annotated[bool | list[bool] | None, prop("doesNotShip")] = None
    has_shipping_service: Annotated[
        ShippingService | list[ShippingService] | None, prop("hasShippingService")
    ] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    provider: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("provider")
    ] = None
    shipping_destination: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingDestination")
    ] = None
    shipping_label: Annotated[str | list[str] | None, prop("shippingLabel")] = None
    shipping_origin: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingOrigin")
    ] = None
    shipping_rate: Annotated[
        MonetaryAmount | ShippingRateSettings | list[MonetaryAmount | ShippingRateSettings] | None,
        prop("shippingRate"),
    ] = None
    shipping_settings_link: Annotated[str | list[str] | None, prop("shippingSettingsLink")] = None
    transit_time_label: Annotated[str | list[str] | None, prop("transitTimeLabel")] = None
    valid_for_member_tier: Annotated[
        MemberProgramTier | list[MemberProgramTier] | None, prop("validForMemberTier")
    ] = None
    weight: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("weight")
    ] = None
    width: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("width")
    ] = None


class OnDemandEvent(PublicationEvent):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

    https://schema.org/OnDemandEvent
    """

    jsonld_type: ClassVar[str] = "OnDemandEvent"


class OnlineStore(OnlineBusiness):
    """An eCommerce site.

    https://schema.org/OnlineStore
    """

    jsonld_type: ClassVar[str] = "OnlineStore"
    is_store_on: Annotated[
        OnlineMarketplace | list[OnlineMarketplace] | None, prop("isStoreOn")
    ] = None


class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain service inside a place.\\n\\n The place is __open__ if the opens property is specified, and __closed__ otherwise.\\n\\nIf the value for the closes prope...

    https://schema.org/OpeningHoursSpecification
    """

    jsonld_type: ClassVar[str] = "OpeningHoursSpecification"
    closes: Annotated[_dt.time | list[_dt.time] | None, prop("closes")] = None
    day_of_week: Annotated[DayOfWeek | list[DayOfWeek] | None, prop("dayOfWeek")] = None
    opens: Annotated[_dt.time | list[_dt.time] | None, prop("opens")] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent.

    https://schema.org/OrderAction
    """

    jsonld_type: ClassVar[str] = "OrderAction"
    delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("deliveryMethod")
    ] = None


class OrderItem(StructuredValue):
    """An order item is a line of an order.

    https://schema.org/OrderItem
    """

    jsonld_type: ClassVar[str] = "OrderItem"
    order_delivery: Annotated[
        ParcelDelivery | list[ParcelDelivery] | None, prop("orderDelivery")
    ] = None
    order_item_number: Annotated[str | list[str] | None, prop("orderItemNumber")] = None
    order_item_status: Annotated[
        OrderStatus | list[OrderStatus] | None, prop("orderItemStatus")
    ] = None
    order_quantity: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("orderQuantity"),
    ] = None
    ordered_item: Annotated[
        OrderItem | Product | Service | list[OrderItem | Product | Service] | None,
        prop("orderedItem"),
    ] = None


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    https://schema.org/OrganizationRole
    """

    jsonld_type: ClassVar[str] = "OrganizationRole"
    numbered_position: Annotated[
        int | float | list[int | float] | None, prop("numberedPosition")
    ] = None


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person owned a certain product.

    https://schema.org/OwnershipInfo
    """

    jsonld_type: ClassVar[str] = "OwnershipInfo"
    acquired_from: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("acquiredFrom")
    ] = None
    owned_from: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("ownedFrom")] = None
    owned_through: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("ownedThrough")] = None
    type_of_good: Annotated[
        Product | Service | list[Product | Service] | None, prop("typeOfGood")
    ] = None


class PaintAction(CreateAction):
    """The act of producing a painting, typically with paint and canvas as instruments.

    https://schema.org/PaintAction
    """

    jsonld_type: ClassVar[str] = "PaintAction"


class Park(CivicStructure):
    """A park.

    https://schema.org/Park
    """

    jsonld_type: ClassVar[str] = "Park"


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    https://schema.org/ParkingFacility
    """

    jsonld_type: ClassVar[str] = "ParkingFacility"


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.

    https://schema.org/PathologyTest
    """

    jsonld_type: ClassVar[str] = "PathologyTest"
    tissue_sample: Annotated[str | list[str] | None, prop("tissueSample")] = None


class PayAction(TradeAction):
    """An agent pays a price to a participant.

    https://schema.org/PayAction
    """

    jsonld_type: ClassVar[str] = "PayAction"
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    https://schema.org/PeopleAudience
    """

    jsonld_type: ClassVar[str] = "PeopleAudience"
    health_condition: Annotated[
        MedicalCondition | list[MedicalCondition] | None, prop("healthCondition")
    ] = None
    required_gender: Annotated[str | list[str] | None, prop("requiredGender")] = None
    required_max_age: Annotated[int | list[int] | None, prop("requiredMaxAge")] = None
    required_min_age: Annotated[int | list[int] | None, prop("requiredMinAge")] = None
    suggested_age: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("suggestedAge")
    ] = None
    suggested_gender: Annotated[
        str | GenderType | list[str | GenderType] | None, prop("suggestedGender")
    ] = None
    suggested_max_age: Annotated[
        int | float | list[int | float] | None, prop("suggestedMaxAge")
    ] = None
    suggested_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("suggestedMeasurement")
    ] = None
    suggested_min_age: Annotated[
        int | float | list[int | float] | None, prop("suggestedMinAge")
    ] = None


class PerformAction(PlayAction):
    """The act of participating in performance arts.

    https://schema.org/PerformAction
    """

    jsonld_type: ClassVar[str] = "PerformAction"
    entertainment_business: Annotated[
        EntertainmentBusiness | list[EntertainmentBusiness] | None, prop("entertainmentBusiness")
    ] = None


class PerformanceRole(Role):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

    https://schema.org/PerformanceRole
    """

    jsonld_type: ClassVar[str] = "PerformanceRole"
    character_name: Annotated[str | list[str] | None, prop("characterName")] = None


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center.

    https://schema.org/PerformingArtsTheater
    """

    jsonld_type: ClassVar[str] = "PerformingArtsTheater"


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera.

    https://schema.org/PhotographAction
    """

    jsonld_type: ClassVar[str] = "PhotographAction"


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness.

    https://schema.org/PhysicalActivity
    """

    jsonld_type: ClassVar[str] = "PhysicalActivity"
    associated_anatomy: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | SuperficialAnatomy
        | list[AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy]
        | None,
        prop("associatedAnatomy"),
    ] = None
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None
    epidemiology: Annotated[str | list[str] | None, prop("epidemiology")] = None
    pathophysiology: Annotated[str | list[str] | None, prop("pathophysiology")] = None


class PlaceOfWorship(CivicStructure):
    """Place of worship, such as a church, synagogue, or mosque.

    https://schema.org/PlaceOfWorship
    """

    jsonld_type: ClassVar[str] = "PlaceOfWorship"


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future date.

    https://schema.org/PlanAction
    """

    jsonld_type: ClassVar[str] = "PlanAction"
    scheduled_time: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("scheduledTime")
    ] = None


class PlayGameAction(ConsumeAction):
    """The act of playing a video game.

    https://schema.org/PlayGameAction
    """

    jsonld_type: ClassVar[str] = "PlayGameAction"
    game_availability_type: Annotated[
        str | GameAvailabilityEnumeration | list[str | GameAvailabilityEnumeration] | None,
        prop("gameAvailabilityType"),
    ] = None


class Playground(CivicStructure):
    """A playground.

    https://schema.org/Playground
    """

    jsonld_type: ClassVar[str] = "Playground"


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postal codes, usually defined as the set of valid codes between postalCodeBegin and postalCodeEnd, inclusively.

    https://schema.org/PostalCodeRangeSpecification
    """

    jsonld_type: ClassVar[str] = "PostalCodeRangeSpecification"
    postal_code_begin: Annotated[str | list[str] | None, prop("postalCodeBegin")] = None
    postal_code_end: Annotated[str | list[str] | None, prop("postalCodeEnd")] = None


class PreOrderAction(TradeAction):
    """An agent orders a (not yet released) object/product/service to be delivered/sent.

    https://schema.org/PreOrderAction
    """

    jsonld_type: ClassVar[str] = "PreOrderAction"


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation.

    https://schema.org/PresentationDigitalDocument
    """

    jsonld_type: ClassVar[str] = "PresentationDigitalDocument"


class PreventionIndication(MedicalIndication):
    """An indication for preventing an underlying condition, symptom, etc.

    https://schema.org/PreventionIndication
    """

    jsonld_type: ClassVar[str] = "PreventionIndication"


class PriceSpecification(StructuredValue):
    """A structured value representing a price or price range.

    https://schema.org/PriceSpecification
    """

    jsonld_type: ClassVar[str] = "PriceSpecification"
    eligible_quantity: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("eligibleQuantity")
    ] = None
    eligible_transaction_volume: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("eligibleTransactionVolume")
    ] = None
    max_price: Annotated[int | float | list[int | float] | None, prop("maxPrice")] = None
    membership_points_earned: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("membershipPointsEarned"),
    ] = None
    min_price: Annotated[int | float | list[int | float] | None, prop("minPrice")] = None
    price: Annotated[str | int | float | list[str | int | float] | None, prop("price")] = None
    price_currency: Annotated[str | list[str] | None, prop("priceCurrency")] = None
    valid_for_member_tier: Annotated[
        MemberProgramTier | list[MemberProgramTier] | None, prop("validForMemberTier")
    ] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None
    value_added_tax_included: Annotated[bool | list[bool] | None, prop("valueAddedTaxIncluded")] = (
        None
    )


class ProfessionalService(LocalBusiness):
    """Original definition: "provider of professional services."\\n\\nThe general ProfessionalService type for local businesses was deprecated due to confusion with Service.

    https://schema.org/ProfessionalService
    """

    jsonld_type: ClassVar[str] = "ProfessionalService"


class ProfilePage(WebPage):
    """Web page type: Profile page.

    https://schema.org/ProfilePage
    """

    jsonld_type: ClassVar[str] = "ProfilePage"


class PropertyValue(StructuredValue):
    """A property-value pair, e.g. representing a feature of a product or place.

    https://schema.org/PropertyValue
    """

    jsonld_type: ClassVar[str] = "PropertyValue"
    max_value: Annotated[int | float | list[int | float] | None, prop("maxValue")] = None
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None
    min_value: Annotated[int | float | list[int | float] | None, prop("minValue")] = None
    property_id: Annotated[str | list[str] | None, prop("propertyID")] = None
    unit_code: Annotated[str | list[str] | None, prop("unitCode")] = None
    unit_text: Annotated[str | list[str] | None, prop("unitText")] = None
    value: Annotated[
        str
        | bool
        | int
        | float
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | StructuredValue
        | list[
            str
            | bool
            | int
            | float
            | DriveWheelConfigurationValue
            | QualitativeValue
            | SteeringPositionValue
            | StructuredValue
        ]
        | None,
        prop("value"),
    ] = None
    value_reference: Annotated[
        str
        | BodyMeasurementTypeEnumeration
        | DefinedTerm
        | DriveWheelConfigurationValue
        | Enumeration
        | MeasurementTypeEnumeration
        | PropertyValue
        | QualitativeValue
        | QuantitativeValue
        | SchemaEnumeration
        | SteeringPositionValue
        | StructuredValue
        | WearableMeasurementTypeEnumeration
        | list[
            str
            | BodyMeasurementTypeEnumeration
            | DefinedTerm
            | DriveWheelConfigurationValue
            | Enumeration
            | MeasurementTypeEnumeration
            | PropertyValue
            | QualitativeValue
            | QuantitativeValue
            | SchemaEnumeration
            | SteeringPositionValue
            | StructuredValue
            | WearableMeasurementTypeEnumeration
        ]
        | None,
        prop("valueReference"),
    ] = None


class PublicToilet(CivicStructure):
    """A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses.

    https://schema.org/PublicToilet
    """

    jsonld_type: ClassVar[str] = "PublicToilet"


class QAPage(WebPage):
    """A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).

    https://schema.org/QAPage
    """

    jsonld_type: ClassVar[str] = "QAPage"


class QualitativeValue(Enumeration):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.

    https://schema.org/QualitativeValue
    """

    jsonld_type: ClassVar[str] = "QualitativeValue"
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    equal: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("equal"),
    ] = None
    greater: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("greater"),
    ] = None
    greater_or_equal: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("greaterOrEqual"),
    ] = None
    lesser: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("lesser"),
    ] = None
    lesser_or_equal: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("lesserOrEqual"),
    ] = None
    non_equal: Annotated[
        DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | list[DriveWheelConfigurationValue | QualitativeValue | SteeringPositionValue]
        | None,
        prop("nonEqual"),
    ] = None
    value_reference: Annotated[
        str
        | BodyMeasurementTypeEnumeration
        | DefinedTerm
        | DriveWheelConfigurationValue
        | Enumeration
        | MeasurementTypeEnumeration
        | PropertyValue
        | QualitativeValue
        | QuantitativeValue
        | SchemaEnumeration
        | SteeringPositionValue
        | StructuredValue
        | WearableMeasurementTypeEnumeration
        | list[
            str
            | BodyMeasurementTypeEnumeration
            | DefinedTerm
            | DriveWheelConfigurationValue
            | Enumeration
            | MeasurementTypeEnumeration
            | PropertyValue
            | QualitativeValue
            | QuantitativeValue
            | SchemaEnumeration
            | SteeringPositionValue
            | StructuredValue
            | WearableMeasurementTypeEnumeration
        ]
        | None,
        prop("valueReference"),
    ] = None


class QuantitativeValue(StructuredValue):
    """A point value or interval for product characteristics and other purposes.

    https://schema.org/QuantitativeValue
    """

    jsonld_type: ClassVar[str] = "QuantitativeValue"
    additional_property: Annotated[
        PropertyValue | list[PropertyValue] | None, prop("additionalProperty")
    ] = None
    max_value: Annotated[int | float | list[int | float] | None, prop("maxValue")] = None
    min_value: Annotated[int | float | list[int | float] | None, prop("minValue")] = None
    unit_code: Annotated[str | list[str] | None, prop("unitCode")] = None
    unit_text: Annotated[str | list[str] | None, prop("unitText")] = None
    value: Annotated[
        str
        | bool
        | int
        | float
        | DriveWheelConfigurationValue
        | QualitativeValue
        | SteeringPositionValue
        | StructuredValue
        | list[
            str
            | bool
            | int
            | float
            | DriveWheelConfigurationValue
            | QualitativeValue
            | SteeringPositionValue
            | StructuredValue
        ]
        | None,
        prop("value"),
    ] = None
    value_reference: Annotated[
        str
        | BodyMeasurementTypeEnumeration
        | DefinedTerm
        | DriveWheelConfigurationValue
        | Enumeration
        | MeasurementTypeEnumeration
        | PropertyValue
        | QualitativeValue
        | QuantitativeValue
        | SchemaEnumeration
        | SteeringPositionValue
        | StructuredValue
        | WearableMeasurementTypeEnumeration
        | list[
            str
            | BodyMeasurementTypeEnumeration
            | DefinedTerm
            | DriveWheelConfigurationValue
            | Enumeration
            | MeasurementTypeEnumeration
            | PropertyValue
            | QualitativeValue
            | QuantitativeValue
            | SchemaEnumeration
            | SteeringPositionValue
            | StructuredValue
            | WearableMeasurementTypeEnumeration
        ]
        | None,
        prop("valueReference"),
    ] = None


class QuantitativeValueDistribution(StructuredValue):
    """A statistical distribution of values.

    https://schema.org/QuantitativeValueDistribution
    """

    jsonld_type: ClassVar[str] = "QuantitativeValueDistribution"
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None
    median: Annotated[int | float | list[int | float] | None, prop("median")] = None
    percentile10: Annotated[int | float | list[int | float] | None, prop("percentile10")] = None
    percentile25: Annotated[int | float | list[int | float] | None, prop("percentile25")] = None
    percentile75: Annotated[int | float | list[int | float] | None, prop("percentile75")] = None
    percentile90: Annotated[int | float | list[int | float] | None, prop("percentile90")] = None


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.

    https://schema.org/Question
    """

    jsonld_type: ClassVar[str] = "Question"
    accepted_answer: Annotated[
        Answer | ItemList | list[Answer | ItemList] | None, prop("acceptedAnswer")
    ] = None
    answer_count: Annotated[int | list[int] | None, prop("answerCount")] = None
    edu_question_type: Annotated[str | list[str] | None, prop("eduQuestionType")] = None
    suggested_answer: Annotated[
        Answer | ItemList | list[Answer | ItemList] | None, prop("suggestedAnswer")
    ] = None


class QuoteAction(TradeAction):
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store.

    https://schema.org/QuoteAction
    """

    jsonld_type: ClassVar[str] = "QuoteAction"


class RVPark(CivicStructure):
    """A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.

    https://schema.org/RVPark
    """

    jsonld_type: ClassVar[str] = "RVPark"


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.

    https://schema.org/RadioChannel
    """

    jsonld_type: ClassVar[str] = "RadioChannel"


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program.

    https://schema.org/RadioClip
    """

    jsonld_type: ClassVar[str] = "RadioClip"


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season.

    https://schema.org/RadioEpisode
    """

    jsonld_type: ClassVar[str] = "RadioEpisode"


class RadioSeason(CreativeWorkSeason):
    """Season dedicated to radio broadcast and associated online delivery.

    https://schema.org/RadioSeason
    """

    jsonld_type: ClassVar[str] = "RadioSeason"


class RadioStation(LocalBusiness):
    """A radio station.

    https://schema.org/RadioStation
    """

    jsonld_type: ClassVar[str] = "RadioStation"


class ReactAction(AssessAction):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    https://schema.org/ReactAction
    """

    jsonld_type: ClassVar[str] = "ReactAction"


class ReadAction(ConsumeAction):
    """The act of consuming written content.

    https://schema.org/ReadAction
    """

    jsonld_type: ClassVar[str] = "ReadAction"


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    https://schema.org/RealEstateAgent
    """

    jsonld_type: ClassVar[str] = "RealEstateAgent"


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination.

    https://schema.org/ReceiveAction
    """

    jsonld_type: ClassVar[str] = "ReceiveAction"
    delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("deliveryMethod")
    ] = None
    sender: Annotated[
        Audience | Organization | Person | list[Audience | Organization | Person] | None,
        prop("sender"),
    ] = None


class Recipe(HowTo):
    """A recipe.

    https://schema.org/Recipe
    """

    jsonld_type: ClassVar[str] = "Recipe"
    cook_time: Annotated[str | list[str] | None, prop("cookTime")] = None
    cooking_method: Annotated[str | list[str] | None, prop("cookingMethod")] = None
    ingredients: Annotated[
        str | list[str] | None, prop("ingredients", superseded_by=("recipeIngredient",))
    ] = None
    nutrition: Annotated[
        NutritionInformation | list[NutritionInformation] | None, prop("nutrition")
    ] = None
    recipe_category: Annotated[str | list[str] | None, prop("recipeCategory")] = None
    recipe_cuisine: Annotated[str | list[str] | None, prop("recipeCuisine")] = None
    recipe_ingredient: Annotated[
        str | ItemList | PropertyValue | list[str | ItemList | PropertyValue] | None,
        prop("recipeIngredient"),
    ] = None
    recipe_instructions: Annotated[
        str | CreativeWork | ItemList | list[str | CreativeWork | ItemList] | None,
        prop("recipeInstructions"),
    ] = None
    recipe_yield: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("recipeYield")
    ] = None
    suitable_for_diet: Annotated[
        Diet | RestrictedDiet | list[Diet | RestrictedDiet] | None, prop("suitableForDiet")
    ] = None


class Recommendation(Review):
    """Recommendation is a type of Review that suggests or proposes something as the best option or best course of action.

    https://schema.org/Recommendation
    """

    jsonld_type: ClassVar[str] = "Recommendation"
    category: Annotated[
        str
        | CategoryCode
        | PhysicalActivityCategory
        | SchemaEnumeration
        | Thing
        | list[str | CategoryCode | PhysicalActivityCategory | SchemaEnumeration | Thing]
        | None,
        prop("category"),
    ] = None


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    https://schema.org/RecyclingCenter
    """

    jsonld_type: ClassVar[str] = "RecyclingCenter"


class RegisterAction(InteractAction):
    """The act of registering to be a user of a service, product or web page.\\n\\nRelated actions:\\n\\n* JoinAction: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.\\n* FollowA...

    https://schema.org/RegisterAction
    """

    jsonld_type: ClassVar[str] = "RegisterAction"


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property.

    https://schema.org/RentAction
    """

    jsonld_type: ClassVar[str] = "RentAction"
    landlord: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("landlord")
    ] = None
    real_estate_agent: Annotated[
        RealEstateAgent | list[RealEstateAgent] | None, prop("realEstateAgent")
    ] = None


class RentalCarReservation(Reservation):
    """A reservation for a rental car.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/RentalCarReservation
    """

    jsonld_type: ClassVar[str] = "RentalCarReservation"
    dropoff_location: Annotated[Place | list[Place] | None, prop("dropoffLocation")] = None
    dropoff_time: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("dropoffTime")] = None
    pickup_location: Annotated[Place | list[Place] | None, prop("pickupLocation")] = None
    pickup_time: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("pickupTime")] = None


class RepaymentSpecification(StructuredValue):
    """A structured value representing repayment.

    https://schema.org/RepaymentSpecification
    """

    jsonld_type: ClassVar[str] = "RepaymentSpecification"
    down_payment: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None,
        prop("downPayment"),
    ] = None
    early_prepayment_penalty: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("earlyPrepaymentPenalty")
    ] = None
    loan_payment_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("loanPaymentAmount")
    ] = None
    loan_payment_frequency: Annotated[
        int | float | list[int | float] | None, prop("loanPaymentFrequency")
    ] = None
    number_of_loan_payments: Annotated[
        int | float | list[int | float] | None, prop("numberOfLoanPayments")
    ] = None


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    https://schema.org/ReplaceAction
    """

    jsonld_type: ClassVar[str] = "ReplaceAction"
    replacee: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("replacee")
    ] = None
    replacer: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("replacer")
    ] = None


class Report(Article):
    """A Report generated by governmental or non-governmental organization.

    https://schema.org/Report
    """

    jsonld_type: ClassVar[str] = "Report"
    report_number: Annotated[str | list[str] | None, prop("reportNumber")] = None


class ResearchProject(Project):
    """A Research project.

    https://schema.org/ResearchProject
    """

    jsonld_type: ClassVar[str] = "ResearchProject"


class Researcher(Audience):
    """Researchers.

    https://schema.org/Researcher
    """

    jsonld_type: ClassVar[str] = "Researcher"


class ReservationPackage(Reservation):
    """A group of multiple reservations with common values for all sub-reservations.

    https://schema.org/ReservationPackage
    """

    jsonld_type: ClassVar[str] = "ReservationPackage"
    sub_reservation: Annotated[Reservation | list[Reservation] | None, prop("subReservation")] = (
        None
    )


class ResumeAction(ControlAction):
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).

    https://schema.org/ResumeAction
    """

    jsonld_type: ClassVar[str] = "ResumeAction"


class ReturnAction(TransferAction):
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    https://schema.org/ReturnAction
    """

    jsonld_type: ClassVar[str] = "ReturnAction"
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class ReviewAction(AssessAction):
    """The act of producing a balanced opinion about the object for an audience.

    https://schema.org/ReviewAction
    """

    jsonld_type: ClassVar[str] = "ReviewAction"
    result_review: Annotated[Review | list[Review] | None, prop("resultReview")] = None


class Room(Accommodation):
    """A room is a distinguishable space within a structure, usually separated from other spaces by interior walls (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Room).

    https://schema.org/Room
    """

    jsonld_type: ClassVar[str] = "Room"


class SatiricalArticle(Article):
    """An Article whose content is primarily satirical(https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true.

    https://schema.org/SatiricalArticle
    """

    jsonld_type: ClassVar[str] = "SatiricalArticle"


class ScholarlyArticle(Article):
    """A scholarly article.

    https://schema.org/ScholarlyArticle
    """

    jsonld_type: ClassVar[str] = "ScholarlyArticle"


class SearchResultsPage(WebPage):
    """Web page type: Search results page.

    https://schema.org/SearchResultsPage
    """

    jsonld_type: ClassVar[str] = "SearchResultsPage"


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    https://schema.org/SelfStorage
    """

    jsonld_type: ClassVar[str] = "SelfStorage"


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered.

    https://schema.org/SellAction
    """

    jsonld_type: ClassVar[str] = "SellAction"
    buyer: Annotated[Organization | Person | list[Organization | Person] | None, prop("buyer")] = (
        None
    )
    warranty_promise: Annotated[
        WarrantyPromise | list[WarrantyPromise] | None,
        prop("warrantyPromise", superseded_by=("warranty",)),
    ] = None


class SendAction(TransferAction):
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination.

    https://schema.org/SendAction
    """

    jsonld_type: ClassVar[str] = "SendAction"
    delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("deliveryMethod")
    ] = None
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class SequentialArt(Book, VisualArtwork):
    """An art forms that use images deployed in a specific order for the purpose of graphic storytelling (i.e., narration of graphic stories) or conveying information.

    https://schema.org/SequentialArt
    """

    jsonld_type: ClassVar[str] = "SequentialArt"


class ServicePeriod(StructuredValue):
    """ServicePeriod represents a duration with some constraints about cutoff time and business days.

    https://schema.org/ServicePeriod
    """

    jsonld_type: ClassVar[str] = "ServicePeriod"
    business_days: Annotated[
        DayOfWeek | OpeningHoursSpecification | list[DayOfWeek | OpeningHoursSpecification] | None,
        prop("businessDays"),
    ] = None
    cutoff_time: Annotated[_dt.time | list[_dt.time] | None, prop("cutoffTime")] = None
    duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("duration")
    ] = None


class ShippingConditions(StructuredValue):
    """ShippingConditions represent a set of constraints and information about the conditions of shipping a product.

    https://schema.org/ShippingConditions
    """

    jsonld_type: ClassVar[str] = "ShippingConditions"
    depth: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("depth")
    ] = None
    does_not_ship: Annotated[bool | list[bool] | None, prop("doesNotShip")] = None
    height: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("height")
    ] = None
    num_items: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("numItems")] = (
        None
    )
    order_value: Annotated[MonetaryAmount | list[MonetaryAmount] | None, prop("orderValue")] = None
    seasonal_override: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None, prop("seasonalOverride")
    ] = None
    shipping_destination: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingDestination")
    ] = None
    shipping_origin: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingOrigin")
    ] = None
    shipping_rate: Annotated[
        MonetaryAmount | ShippingRateSettings | list[MonetaryAmount | ShippingRateSettings] | None,
        prop("shippingRate"),
    ] = None
    transit_time: Annotated[
        QuantitativeValue | ServicePeriod | list[QuantitativeValue | ServicePeriod] | None,
        prop("transitTime"),
    ] = None
    weight: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("weight")
    ] = None
    width: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("width")
    ] = None


class ShippingDeliveryTime(StructuredValue):
    """ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

    https://schema.org/ShippingDeliveryTime
    """

    jsonld_type: ClassVar[str] = "ShippingDeliveryTime"
    business_days: Annotated[
        DayOfWeek | OpeningHoursSpecification | list[DayOfWeek | OpeningHoursSpecification] | None,
        prop("businessDays"),
    ] = None
    cutoff_time: Annotated[_dt.time | list[_dt.time] | None, prop("cutoffTime")] = None
    handling_time: Annotated[
        QuantitativeValue | ServicePeriod | list[QuantitativeValue | ServicePeriod] | None,
        prop("handlingTime"),
    ] = None
    transit_time: Annotated[
        QuantitativeValue | ServicePeriod | list[QuantitativeValue | ServicePeriod] | None,
        prop("transitTime"),
    ] = None


class ShippingRateSettings(StructuredValue):
    """A ShippingRateSettings represents re-usable pieces of shipping information.

    https://schema.org/ShippingRateSettings
    """

    jsonld_type: ClassVar[str] = "ShippingRateSettings"
    does_not_ship: Annotated[bool | list[bool] | None, prop("doesNotShip")] = None
    free_shipping_threshold: Annotated[
        DeliveryChargeSpecification
        | MonetaryAmount
        | list[DeliveryChargeSpecification | MonetaryAmount]
        | None,
        prop("freeShippingThreshold"),
    ] = None
    is_unlabelled_fallback: Annotated[bool | list[bool] | None, prop("isUnlabelledFallback")] = None
    order_percentage: Annotated[int | float | list[int | float] | None, prop("orderPercentage")] = (
        None
    )
    shipping_destination: Annotated[
        DefinedRegion | list[DefinedRegion] | None, prop("shippingDestination")
    ] = None
    shipping_label: Annotated[str | list[str] | None, prop("shippingLabel")] = None
    shipping_rate: Annotated[
        MonetaryAmount | ShippingRateSettings | list[MonetaryAmount | ShippingRateSettings] | None,
        prop("shippingRate"),
    ] = None
    weight_percentage: Annotated[
        int | float | list[int | float] | None, prop("weightPercentage")
    ] = None


class ShippingService(StructuredValue):
    """ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer.

    https://schema.org/ShippingService
    """

    jsonld_type: ClassVar[str] = "ShippingService"
    fulfillment_type: Annotated[
        FulfillmentTypeEnumeration | list[FulfillmentTypeEnumeration] | None,
        prop("fulfillmentType"),
    ] = None
    handling_time: Annotated[
        QuantitativeValue | ServicePeriod | list[QuantitativeValue | ServicePeriod] | None,
        prop("handlingTime"),
    ] = None
    shipping_conditions: Annotated[
        ShippingConditions | list[ShippingConditions] | None, prop("shippingConditions")
    ] = None
    valid_for_member_tier: Annotated[
        MemberProgramTier | list[MemberProgramTier] | None, prop("validForMemberTier")
    ] = None


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    https://schema.org/ShoppingCenter
    """

    jsonld_type: ClassVar[str] = "ShoppingCenter"


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    https://schema.org/SiteNavigationElement
    """

    jsonld_type: ClassVar[str] = "SiteNavigationElement"


class SizeGroupEnumeration(Enumeration):
    """Enumerates common size groups for various product categories.

    https://schema.org/SizeGroupEnumeration
    """

    jsonld_type: ClassVar[str] = "SizeGroupEnumeration"


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    https://schema.org/SocialMediaPosting
    """

    jsonld_type: ClassVar[str] = "SocialMediaPosting"
    shared_content: Annotated[CreativeWork | list[CreativeWork] | None, prop("sharedContent")] = (
        None
    )


class Specialty(Enumeration):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

    https://schema.org/Specialty
    """

    jsonld_type: ClassVar[str] = "Specialty"


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    https://schema.org/SportsActivityLocation
    """

    jsonld_type: ClassVar[str] = "SportsActivityLocation"


class SportsTeam(SportsOrganization):
    """Organization: Sports team.

    https://schema.org/SportsTeam
    """

    jsonld_type: ClassVar[str] = "SportsTeam"
    athlete: Annotated[Person | list[Person] | None, prop("athlete")] = None
    coach: Annotated[Person | list[Person] | None, prop("coach")] = None
    gender: Annotated[str | GenderType | list[str | GenderType] | None, prop("gender")] = None


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    https://schema.org/SpreadsheetDigitalDocument
    """

    jsonld_type: ClassVar[str] = "SpreadsheetDigitalDocument"


class State(AdministrativeArea):
    """A state or province of a country.

    https://schema.org/State
    """

    jsonld_type: ClassVar[str] = "State"


class StatisticalVariable(ConstraintNode):
    """StatisticalVariable represents any type of statistical metric that can be measured at a place and time.

    https://schema.org/StatisticalVariable
    """

    jsonld_type: ClassVar[str] = "StatisticalVariable"
    measurement_denominator: Annotated[
        StatisticalVariable | list[StatisticalVariable] | None, prop("measurementDenominator")
    ] = None
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_qualifier: Annotated[
        Enumeration | SchemaEnumeration | list[Enumeration | SchemaEnumeration] | None,
        prop("measurementQualifier"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None
    stat_type: Annotated[str | list[str] | None, prop("statType")] = None


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    https://schema.org/StatusEnumeration
    """

    jsonld_type: ClassVar[str] = "StatusEnumeration"


class Store(LocalBusiness):
    """A retail good store.

    https://schema.org/Store
    """

    jsonld_type: ClassVar[str] = "Store"


class SubscribeAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.\\n\\nRelated actions:\\n\\n* FollowAction: Unlike FollowAction, SubscribeAction implies that the subscriber ac...

    https://schema.org/SubscribeAction
    """

    jsonld_type: ClassVar[str] = "SubscribeAction"


class SubwayStation(CivicStructure):
    """A subway station.

    https://schema.org/SubwayStation
    """

    jsonld_type: ClassVar[str] = "SubwayStation"


class Suite(Accommodation):
    """A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Suite_(hotel)).

    https://schema.org/Suite
    """

    jsonld_type: ClassVar[str] = "Suite"


class SurgicalProcedure(MedicalProcedure):
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.

    https://schema.org/SurgicalProcedure
    """

    jsonld_type: ClassVar[str] = "SurgicalProcedure"


class SuspendAction(ControlAction):
    """The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).

    https://schema.org/SuspendAction
    """

    jsonld_type: ClassVar[str] = "SuspendAction"


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program.

    https://schema.org/TVClip
    """

    jsonld_type: ClassVar[str] = "TVClip"
    part_of_tv_series: Annotated[
        TVSeries | list[TVSeries] | None, prop("partOfTVSeries", superseded_by=("partOfSeries",))
    ] = None


class TVEpisode(Episode):
    """A TV episode which can be part of a series or season.

    https://schema.org/TVEpisode
    """

    jsonld_type: ClassVar[str] = "TVEpisode"
    part_of_tv_series: Annotated[
        TVSeries | list[TVSeries] | None, prop("partOfTVSeries", superseded_by=("partOfSeries",))
    ] = None
    subtitle_language: Annotated[
        str | Language | list[str | Language] | None, prop("subtitleLanguage")
    ] = None
    title_eidr: Annotated[str | list[str] | None, prop("titleEIDR")] = None


class TVSeason(CreativeWorkSeason):
    """Season dedicated to TV broadcast and associated online delivery.

    https://schema.org/TVSeason
    """

    jsonld_type: ClassVar[str] = "TVSeason"
    part_of_tv_series: Annotated[
        TVSeries | list[TVSeries] | None, prop("partOfTVSeries", superseded_by=("partOfSeries",))
    ] = None
    title_eidr: Annotated[str | list[str] | None, prop("titleEIDR")] = None


class Table(WebPageElement):
    """A table on a Web page.

    https://schema.org/Table
    """

    jsonld_type: ClassVar[str] = "Table"


class TakeAction(TransferAction):
    """The act of gaining ownership of an object from an origin.

    https://schema.org/TakeAction
    """

    jsonld_type: ClassVar[str] = "TakeAction"


class Taxi(Service):
    """A taxi.

    https://schema.org/Taxi

    Deprecated: superseded by TaxiService.
    """

    jsonld_type: ClassVar[str] = "Taxi"


class TaxiReservation(Reservation):
    """A reservation for a taxi.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/TaxiReservation
    """

    jsonld_type: ClassVar[str] = "TaxiReservation"
    party_size: Annotated[
        int | QuantitativeValue | list[int | QuantitativeValue] | None, prop("partySize")
    ] = None
    pickup_location: Annotated[Place | list[Place] | None, prop("pickupLocation")] = None
    pickup_time: Annotated[_dt.datetime | list[_dt.datetime] | None, prop("pickupTime")] = None


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel.

    https://schema.org/TaxiService
    """

    jsonld_type: ClassVar[str] = "TaxiService"


class TaxiStand(CivicStructure):
    """A taxi stand.

    https://schema.org/TaxiStand
    """

    jsonld_type: ClassVar[str] = "TaxiStand"


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.

    https://schema.org/TechArticle
    """

    jsonld_type: ClassVar[str] = "TechArticle"
    dependencies: Annotated[str | list[str] | None, prop("dependencies")] = None
    proficiency_level: Annotated[str | list[str] | None, prop("proficiencyLevel")] = None


class TelevisionChannel(BroadcastChannel):
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.

    https://schema.org/TelevisionChannel
    """

    jsonld_type: ClassVar[str] = "TelevisionChannel"


class TelevisionStation(LocalBusiness):
    """A television station.

    https://schema.org/TelevisionStation
    """

    jsonld_type: ClassVar[str] = "TelevisionStation"


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    https://schema.org/TextDigitalDocument
    """

    jsonld_type: ClassVar[str] = "TextDigitalDocument"


class TextObject(MediaObject):
    """A text file.

    https://schema.org/TextObject
    """

    jsonld_type: ClassVar[str] = "TextObject"


class TheaterGroup(PerformingGroup):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

    https://schema.org/TheaterGroup
    """

    jsonld_type: ClassVar[str] = "TheaterGroup"


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

    https://schema.org/TherapeuticProcedure
    """

    jsonld_type: ClassVar[str] = "TherapeuticProcedure"
    adverse_outcome: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("adverseOutcome"),
    ] = None
    dose_schedule: Annotated[DoseSchedule | list[DoseSchedule] | None, prop("doseSchedule")] = None
    drug: Annotated[Drug | list[Drug] | None, prop("drug")] = None


class TieAction(AchieveAction):
    """The act of reaching a draw in a competitive activity.

    https://schema.org/TieAction
    """

    jsonld_type: ClassVar[str] = "TieAction"


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    https://schema.org/TipAction
    """

    jsonld_type: ClassVar[str] = "TipAction"
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class TouristInformationCenter(LocalBusiness):
    """A tourist information center.

    https://schema.org/TouristInformationCenter
    """

    jsonld_type: ClassVar[str] = "TouristInformationCenter"


class TrackAction(FindAction):
    """An agent tracks an object for updates.\\n\\nRelated actions:\\n\\n* FollowAction: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.\\n* SubscribeAction: Unlike SubscribeAction, TrackAction refers...

    https://schema.org/TrackAction
    """

    jsonld_type: ClassVar[str] = "TrackAction"
    delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("deliveryMethod")
    ] = None


class TrainReservation(Reservation):
    """A reservation for train travel.\\n\\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    https://schema.org/TrainReservation
    """

    jsonld_type: ClassVar[str] = "TrainReservation"


class TrainStation(CivicStructure):
    """A train station.

    https://schema.org/TrainStation
    """

    jsonld_type: ClassVar[str] = "TrainStation"


class TrainTrip(Trip):
    """A trip on a commercial train line.

    https://schema.org/TrainTrip
    """

    jsonld_type: ClassVar[str] = "TrainTrip"
    arrival_platform: Annotated[str | list[str] | None, prop("arrivalPlatform")] = None
    arrival_station: Annotated[TrainStation | list[TrainStation] | None, prop("arrivalStation")] = (
        None
    )
    departure_platform: Annotated[str | list[str] | None, prop("departurePlatform")] = None
    departure_station: Annotated[
        TrainStation | list[TrainStation] | None, prop("departureStation")
    ] = None
    train_name: Annotated[str | list[str] | None, prop("trainName")] = None
    train_number: Annotated[str | list[str] | None, prop("trainNumber")] = None


class TravelAction(MoveAction):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    https://schema.org/TravelAction
    """

    jsonld_type: ClassVar[str] = "TravelAction"
    distance: Annotated[str | list[str] | None, prop("distance")] = None


class TravelAgency(LocalBusiness):
    """A travel agency.

    https://schema.org/TravelAgency
    """

    jsonld_type: ClassVar[str] = "TravelAgency"


class TreatmentIndication(MedicalIndication):
    """An indication for treating an underlying condition, symptom, etc.

    https://schema.org/TreatmentIndication
    """

    jsonld_type: ClassVar[str] = "TreatmentIndication"


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.

    https://schema.org/TypeAndQuantityNode
    """

    jsonld_type: ClassVar[str] = "TypeAndQuantityNode"
    amount_of_this_good: Annotated[
        int | float | list[int | float] | None, prop("amountOfThisGood")
    ] = None
    business_function: Annotated[
        BusinessFunction | list[BusinessFunction] | None, prop("businessFunction")
    ] = None
    type_of_good: Annotated[
        Product | Service | list[Product | Service] | None, prop("typeOfGood")
    ] = None
    unit_code: Annotated[str | list[str] | None, prop("unitCode")] = None
    unit_text: Annotated[str | list[str] | None, prop("unitText")] = None


class UnRegisterAction(InteractAction):
    """The act of un-registering from a service.\\n\\nRelated actions:\\n\\n* RegisterAction: antonym of UnRegisterAction.\\n* LeaveAction: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously re...

    https://schema.org/UnRegisterAction
    """

    jsonld_type: ClassVar[str] = "UnRegisterAction"


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose.

    https://schema.org/UseAction
    """

    jsonld_type: ClassVar[str] = "UseAction"


class UserBlocks(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserBlocks

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserBlocks"


class UserCheckins(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserCheckins

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserCheckins"


class UserComments(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserComments

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserComments"
    comment_text: Annotated[str | list[str] | None, prop("commentText")] = None
    comment_time: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("commentTime")
    ] = None
    creator: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("creator")
    ] = None
    discusses: Annotated[CreativeWork | list[CreativeWork] | None, prop("discusses")] = None
    reply_to_url: Annotated[str | list[str] | None, prop("replyToUrl")] = None


class UserDownloads(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserDownloads

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserDownloads"


class UserLikes(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserLikes

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserLikes"


class UserPageVisits(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserPageVisits

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserPageVisits"


class UserPlays(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserPlays

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserPlays"


class UserPlusOnes(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserPlusOnes

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserPlusOnes"


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with CriticReview.

    https://schema.org/UserReview
    """

    jsonld_type: ClassVar[str] = "UserReview"


class UserTweets(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages.

    https://schema.org/UserTweets

    Deprecated: superseded by InteractionCounter.
    """

    jsonld_type: ClassVar[str] = "UserTweets"


class Vessel(AnatomicalStructure):
    """A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.

    https://schema.org/Vessel
    """

    jsonld_type: ClassVar[str] = "Vessel"


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    https://schema.org/VeterinaryCare
    """

    jsonld_type: ClassVar[str] = "VeterinaryCare"


class VideoGame(Game, SoftwareApplication):
    """A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.

    https://schema.org/VideoGame
    """

    jsonld_type: ClassVar[str] = "VideoGame"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    cheat_code: Annotated[CreativeWork | list[CreativeWork] | None, prop("cheatCode")] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    game_edition: Annotated[str | list[str] | None, prop("gameEdition")] = None
    game_platform: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("gamePlatform"),
    ] = None
    game_server: Annotated[GameServer | list[GameServer] | None, prop("gameServer")] = None
    game_tip: Annotated[CreativeWork | list[CreativeWork] | None, prop("gameTip")] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    play_mode: Annotated[GamePlayMode | list[GamePlayMode] | None, prop("playMode")] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class VideoGameClip(Clip):
    """A short segment/part of a video game.

    https://schema.org/VideoGameClip
    """

    jsonld_type: ClassVar[str] = "VideoGameClip"


class VideoObject(MediaObject):
    """A video file.

    https://schema.org/VideoObject
    """

    jsonld_type: ClassVar[str] = "VideoObject"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    caption: Annotated[str | MediaObject | list[str | MediaObject] | None, prop("caption")] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    embedded_text_caption: Annotated[str | list[str] | None, prop("embeddedTextCaption")] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    transcript: Annotated[str | list[str] | None, prop("transcript")] = None
    video_frame_size: Annotated[str | list[str] | None, prop("videoFrameSize")] = None
    video_quality: Annotated[str | list[str] | None, prop("videoQuality")] = None


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    https://schema.org/ViewAction
    """

    jsonld_type: ClassVar[str] = "ViewAction"


class Volcano(Landform):
    """A volcano, like Fujisan.

    https://schema.org/Volcano
    """

    jsonld_type: ClassVar[str] = "Volcano"


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    https://schema.org/WPAdBlock
    """

    jsonld_type: ClassVar[str] = "WPAdBlock"


class WPFooter(WebPageElement):
    """The footer section of the page.

    https://schema.org/WPFooter
    """

    jsonld_type: ClassVar[str] = "WPFooter"


class WPHeader(WebPageElement):
    """The header section of the page.

    https://schema.org/WPHeader
    """

    jsonld_type: ClassVar[str] = "WPHeader"


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    https://schema.org/WPSideBar
    """

    jsonld_type: ClassVar[str] = "WPSideBar"


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    https://schema.org/WarrantyPromise
    """

    jsonld_type: ClassVar[str] = "WarrantyPromise"
    duration_of_warranty: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("durationOfWarranty")
    ] = None
    warranty_scope: Annotated[WarrantyScope | list[WarrantyScope] | None, prop("warrantyScope")] = (
        None
    )


class WarrantyScope(Enumeration):
    """A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\\n\\nCommonly used values:\\n\\n* http://purl.org/goodrelations/v1#Labor-BringIn\\n* http://purl.org/goodrelations/v1#Part...

    https://schema.org/WarrantyScope
    """

    jsonld_type: ClassVar[str] = "WarrantyScope"


class WatchAction(ConsumeAction):
    """The act of consuming dynamic/moving visual content.

    https://schema.org/WatchAction
    """

    jsonld_type: ClassVar[str] = "WatchAction"


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    https://schema.org/WebAPI
    """

    jsonld_type: ClassVar[str] = "WebAPI"
    documentation: Annotated[
        str | CreativeWork | list[str | CreativeWork] | None, prop("documentation")
    ] = None


class WebApplication(SoftwareApplication):
    """Web applications.

    https://schema.org/WebApplication
    """

    jsonld_type: ClassVar[str] = "WebApplication"
    browser_requirements: Annotated[str | list[str] | None, prop("browserRequirements")] = None


class WinAction(AchieveAction):
    """The act of achieving victory in a competitive activity.

    https://schema.org/WinAction
    """

    jsonld_type: ClassVar[str] = "WinAction"
    loser: Annotated[Person | list[Person] | None, prop("loser")] = None


class WorkBasedProgram(EducationalOccupationalProgram):
    """A program with both an educational and employment component.

    https://schema.org/WorkBasedProgram
    """

    jsonld_type: ClassVar[str] = "WorkBasedProgram"


class WriteAction(CreateAction):
    """The act of authoring written creative content.

    https://schema.org/WriteAction
    """

    jsonld_type: ClassVar[str] = "WriteAction"
    in_language: Annotated[str | Language | list[str | Language] | None, prop("inLanguage")] = None
    language: Annotated[
        Language | list[Language] | None, prop("language", superseded_by=("inLanguage",))
    ] = None


class Zoo(CivicStructure):
    """A zoo.

    https://schema.org/Zoo
    """

    jsonld_type: ClassVar[str] = "Zoo"


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM.

    https://schema.org/AMRadioChannel
    """

    jsonld_type: ClassVar[str] = "AMRadioChannel"


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs).

    https://schema.org/APIReference
    """

    jsonld_type: ClassVar[str] = "APIReference"
    assembly: Annotated[
        str | list[str] | None, prop("assembly", superseded_by=("executableLibraryName",))
    ] = None
    assembly_version: Annotated[str | list[str] | None, prop("assemblyVersion")] = None
    executable_library_name: Annotated[str | list[str] | None, prop("executableLibraryName")] = None
    programming_model: Annotated[str | list[str] | None, prop("programmingModel")] = None
    target_platform: Annotated[str | list[str] | None, prop("targetPlatform")] = None


class AcceptAction(AllocateAction):
    """The act of committing to/adopting an object.\\n\\nRelated actions:\\n\\n* RejectAction: The antonym of AcceptAction.

    https://schema.org/AcceptAction
    """

    jsonld_type: ClassVar[str] = "AcceptAction"


class AccountingService(FinancialService):
    """Accountancy business.\\n\\nAs a LocalBusiness it can be described as a provider of one or more Service\\(s).

    https://schema.org/AccountingService
    """

    jsonld_type: ClassVar[str] = "AccountingService"


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    https://schema.org/AdultEntertainment
    """

    jsonld_type: ClassVar[str] = "AdultEntertainment"


class AgreeAction(ReactAction):
    """The act of expressing a consistency of opinion with the object.

    https://schema.org/AgreeAction
    """

    jsonld_type: ClassVar[str] = "AgreeAction"


class AmusementPark(EntertainmentBusiness):
    """An amusement park.

    https://schema.org/AmusementPark
    """

    jsonld_type: ClassVar[str] = "AmusementPark"


class AnalysisNewsArticle(NewsArticle):
    """An AnalysisNewsArticle is a NewsArticle that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.

    https://schema.org/AnalysisNewsArticle
    """

    jsonld_type: ClassVar[str] = "AnalysisNewsArticle"


class ArtGallery(EntertainmentBusiness):
    """An art gallery.

    https://schema.org/ArtGallery
    """

    jsonld_type: ClassVar[str] = "ArtGallery"


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart.

    https://schema.org/Artery
    """

    jsonld_type: ClassVar[str] = "Artery"
    arterial_branch: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("arterialBranch")
    ] = None
    supply_to: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("supplyTo")
    ] = None


class AskAction(CommunicateAction):
    """The act of posing a question / favor to someone.\\n\\nRelated actions:\\n\\n* ReplyAction: Appears generally as a response to AskAction.

    https://schema.org/AskAction
    """

    jsonld_type: ClassVar[str] = "AskAction"
    question: Annotated[Question | list[Question] | None, prop("question")] = None


class AskPublicNewsArticle(NewsArticle):
    """A NewsArticle expressing an open call by a NewsMediaOrganization asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.

    https://schema.org/AskPublicNewsArticle
    """

    jsonld_type: ClassVar[str] = "AskPublicNewsArticle"


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    https://schema.org/AssignAction
    """

    jsonld_type: ClassVar[str] = "AssignAction"


class Attorney(LegalService):
    """Professional service: Attorney.

    https://schema.org/Attorney
    """

    jsonld_type: ClassVar[str] = "Attorney"


class AudioObjectSnapshot(AudioObject):
    """A specific and exact (byte-for-byte) version of an AudioObject.

    https://schema.org/AudioObjectSnapshot
    """

    jsonld_type: ClassVar[str] = "AudioObjectSnapshot"


class Audiobook(AudioObject, Book):
    """An audiobook.

    https://schema.org/Audiobook
    """

    jsonld_type: ClassVar[str] = "Audiobook"
    read_by: Annotated[Person | list[Person] | None, prop("readBy")] = None


class AuthorizeAction(AllocateAction):
    """The act of granting permission to an object.

    https://schema.org/AuthorizeAction
    """

    jsonld_type: ClassVar[str] = "AuthorizeAction"
    recipient: Annotated[
        Audience
        | ContactPoint
        | Organization
        | Person
        | list[Audience | ContactPoint | Organization | Person]
        | None,
        prop("recipient"),
    ] = None


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    https://schema.org/AutoBodyShop
    """

    jsonld_type: ClassVar[str] = "AutoBodyShop"


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    https://schema.org/AutoDealer
    """

    jsonld_type: ClassVar[str] = "AutoDealer"


class AutoPartsStore(AutomotiveBusiness, Store):
    """An auto parts store.

    https://schema.org/AutoPartsStore
    """

    jsonld_type: ClassVar[str] = "AutoPartsStore"


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    https://schema.org/AutoRental
    """

    jsonld_type: ClassVar[str] = "AutoRental"


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    https://schema.org/AutoRepair
    """

    jsonld_type: ClassVar[str] = "AutoRepair"


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    https://schema.org/AutoWash
    """

    jsonld_type: ClassVar[str] = "AutoWash"


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    https://schema.org/AutomatedTeller
    """

    jsonld_type: ClassVar[str] = "AutomatedTeller"


class BackgroundNewsArticle(NewsArticle):
    """A NewsArticle providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder").

    https://schema.org/BackgroundNewsArticle
    """

    jsonld_type: ClassVar[str] = "BackgroundNewsArticle"


class Bakery(FoodEstablishment):
    """A bakery.

    https://schema.org/Bakery
    """

    jsonld_type: ClassVar[str] = "Bakery"


class BankAccount(FinancialProduct):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

    https://schema.org/BankAccount
    """

    jsonld_type: ClassVar[str] = "BankAccount"
    account_minimum_inflow: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("accountMinimumInflow")
    ] = None
    account_overdraft_limit: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("accountOverdraftLimit")
    ] = None
    bank_account_type: Annotated[str | list[str] | None, prop("bankAccountType")] = None


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    https://schema.org/BankOrCreditUnion
    """

    jsonld_type: ClassVar[str] = "BankOrCreditUnion"


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    https://schema.org/BarOrPub
    """

    jsonld_type: ClassVar[str] = "BarOrPub"


class Barcode(ImageObject):
    """An image of a visual machine-readable code such as a barcode or QR code.

    https://schema.org/Barcode
    """

    jsonld_type: ClassVar[str] = "Barcode"


class BeautySalon(HealthAndBeautyBusiness):
    """Beauty salon.

    https://schema.org/BeautySalon
    """

    jsonld_type: ClassVar[str] = "BeautySalon"


class BedAndBreakfast(LodgingBusiness):
    """Bed and breakfast.

    https://schema.org/BedAndBreakfast
    """

    jsonld_type: ClassVar[str] = "BedAndBreakfast"


class BedType(QualitativeValue):
    """A type of bed.

    https://schema.org/BedType
    """

    jsonld_type: ClassVar[str] = "BedType"


class BikeStore(Store):
    """A bike store.

    https://schema.org/BikeStore
    """

    jsonld_type: ClassVar[str] = "BikeStore"


class BlogPosting(SocialMediaPosting):
    """A blog post.

    https://schema.org/BlogPosting
    """

    jsonld_type: ClassVar[str] = "BlogPosting"


class BookSeries(CreativeWorkSeries):
    """A series of books.

    https://schema.org/BookSeries
    """

    jsonld_type: ClassVar[str] = "BookSeries"


class BookStore(Store):
    """A bookstore.

    https://schema.org/BookStore
    """

    jsonld_type: ClassVar[str] = "BookStore"


class BowlingAlley(SportsActivityLocation):
    """A bowling alley.

    https://schema.org/BowlingAlley
    """

    jsonld_type: ClassVar[str] = "BowlingAlley"


class Brewery(FoodEstablishment):
    """Brewery.

    https://schema.org/Brewery
    """

    jsonld_type: ClassVar[str] = "Brewery"


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    https://schema.org/BuddhistTemple
    """

    jsonld_type: ClassVar[str] = "BuddhistTemple"


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    https://schema.org/CafeOrCoffeeShop
    """

    jsonld_type: ClassVar[str] = "CafeOrCoffeeShop"


class Campground(CivicStructure, LodgingBusiness):
    """A camping site, campsite, or Campground is a place used for overnight stay in the outdoors, typically containing individual CampingPitch locations.

    https://schema.org/Campground
    """

    jsonld_type: ClassVar[str] = "Campground"


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    https://schema.org/Canal
    """

    jsonld_type: ClassVar[str] = "Canal"


class CancelAction(PlanAction):
    """The act of asserting that a future event/action is no longer going to happen.\\n\\nRelated actions:\\n\\n* ConfirmAction: The antonym of CancelAction.

    https://schema.org/CancelAction
    """

    jsonld_type: ClassVar[str] = "CancelAction"


class Casino(EntertainmentBusiness):
    """A casino.

    https://schema.org/Casino
    """

    jsonld_type: ClassVar[str] = "Casino"


class CheckInAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding...

    https://schema.org/CheckInAction
    """

    jsonld_type: ClassVar[str] = "CheckInAction"


class CheckOutAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check-in) or place (e.g. hotel).\\n\\nRelated actions:\\n\\n* CheckInAction: The antonym of CheckOutAction....

    https://schema.org/CheckOutAction
    """

    jsonld_type: ClassVar[str] = "CheckOutAction"


class Church(PlaceOfWorship):
    """A church.

    https://schema.org/Church
    """

    jsonld_type: ClassVar[str] = "Church"


class CityHall(GovernmentBuilding):
    """A city hall.

    https://schema.org/CityHall
    """

    jsonld_type: ClassVar[str] = "CityHall"


class ClothingStore(Store):
    """A clothing store.

    https://schema.org/ClothingStore
    """

    jsonld_type: ClassVar[str] = "ClothingStore"


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    https://schema.org/CollegeOrUniversity
    """

    jsonld_type: ClassVar[str] = "CollegeOrUniversity"


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    https://schema.org/ComedyClub
    """

    jsonld_type: ClassVar[str] = "ComedyClub"


class ComicCoverArt(ComicStory, CoverArt):
    """The artwork on the cover of a comic.

    https://schema.org/ComicCoverArt
    """

    jsonld_type: ClassVar[str] = "ComicCoverArt"


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    https://schema.org/CommentAction
    """

    jsonld_type: ClassVar[str] = "CommentAction"
    result_comment: Annotated[Comment | list[Comment] | None, prop("resultComment")] = None


class CompleteDataFeed(DataFeed):
    """A CompleteDataFeed is a DataFeed whose standard representation includes content for every item currently in the feed.

    https://schema.org/CompleteDataFeed
    """

    jsonld_type: ClassVar[str] = "CompleteDataFeed"


class CompoundPriceSpecification(PriceSpecification):
    """A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption.

    https://schema.org/CompoundPriceSpecification
    """

    jsonld_type: ClassVar[str] = "CompoundPriceSpecification"
    price_component: Annotated[
        PriceSpecification | list[PriceSpecification] | None, prop("priceComponent")
    ] = None
    price_type: Annotated[
        str | PriceTypeEnumeration | list[str | PriceTypeEnumeration] | None, prop("priceType")
    ] = None


class ComputerStore(Store):
    """A computer store.

    https://schema.org/ComputerStore
    """

    jsonld_type: ClassVar[str] = "ComputerStore"


class ConvenienceStore(Store):
    """A convenience store.

    https://schema.org/ConvenienceStore
    """

    jsonld_type: ClassVar[str] = "ConvenienceStore"


class Courthouse(GovernmentBuilding):
    """A courthouse.

    https://schema.org/Courthouse
    """

    jsonld_type: ClassVar[str] = "Courthouse"


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency.

    https://schema.org/CurrencyConversionService
    """

    jsonld_type: ClassVar[str] = "CurrencyConversionService"


class DaySpa(HealthAndBeautyBusiness):
    """A day spa.

    https://schema.org/DaySpa
    """

    jsonld_type: ClassVar[str] = "DaySpa"


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base.

    https://schema.org/DefenceEstablishment
    """

    jsonld_type: ClassVar[str] = "DefenceEstablishment"


class DeliveryChargeSpecification(PriceSpecification):
    """The price for the delivery of an offer using a particular delivery method.

    https://schema.org/DeliveryChargeSpecification
    """

    jsonld_type: ClassVar[str] = "DeliveryChargeSpecification"
    applies_to_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("appliesToDeliveryMethod")
    ] = None
    area_served: Annotated[
        str
        | AdministrativeArea
        | GeoShape
        | Place
        | list[str | AdministrativeArea | GeoShape | Place]
        | None,
        prop("areaServed"),
    ] = None
    eligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("eligibleRegion")
    ] = None
    ineligible_region: Annotated[
        str | GeoShape | Place | list[str | GeoShape | Place] | None, prop("ineligibleRegion")
    ] = None


class Dentist(MedicalBusiness, MedicalOrganization):
    """A dentist.

    https://schema.org/Dentist
    """

    jsonld_type: ClassVar[str] = "Dentist"


class DepartmentStore(Store):
    """A department store.

    https://schema.org/DepartmentStore
    """

    jsonld_type: ClassVar[str] = "DepartmentStore"


class DisagreeAction(ReactAction):
    """The act of expressing a difference of opinion with the object.

    https://schema.org/DisagreeAction
    """

    jsonld_type: ClassVar[str] = "DisagreeAction"


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    https://schema.org/DiscussionForumPosting
    """

    jsonld_type: ClassVar[str] = "DiscussionForumPosting"


class DislikeAction(ReactAction):
    """The act of expressing a negative sentiment about the object.

    https://schema.org/DislikeAction
    """

    jsonld_type: ClassVar[str] = "DislikeAction"


class Distillery(FoodEstablishment):
    """A distillery.

    https://schema.org/Distillery
    """

    jsonld_type: ClassVar[str] = "Distillery"


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    https://schema.org/Electrician
    """

    jsonld_type: ClassVar[str] = "Electrician"


class ElectronicsStore(Store):
    """An electronics store.

    https://schema.org/ElectronicsStore
    """

    jsonld_type: ClassVar[str] = "ElectronicsStore"


class ElementarySchool(EducationalOrganization):
    """An elementary school.

    https://schema.org/ElementarySchool
    """

    jsonld_type: ClassVar[str] = "ElementarySchool"


class Embassy(GovernmentBuilding):
    """An embassy.

    https://schema.org/Embassy
    """

    jsonld_type: ClassVar[str] = "Embassy"


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships.

    https://schema.org/EmployeeRole
    """

    jsonld_type: ClassVar[str] = "EmployeeRole"
    base_salary: Annotated[
        int
        | float
        | MonetaryAmount
        | PriceSpecification
        | list[int | float | MonetaryAmount | PriceSpecification]
        | None,
        prop("baseSalary"),
    ] = None
    salary_currency: Annotated[str | list[str] | None, prop("salaryCurrency")] = None


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer.

    https://schema.org/EmployerAggregateRating
    """

    jsonld_type: ClassVar[str] = "EmployerAggregateRating"


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanctions an object.

    https://schema.org/EndorseAction
    """

    jsonld_type: ClassVar[str] = "EndorseAction"
    endorsee: Annotated[
        Organization | Person | list[Organization | Person] | None, prop("endorsee")
    ] = None


class ExerciseGym(SportsActivityLocation):
    """A gym.

    https://schema.org/ExerciseGym
    """

    jsonld_type: ClassVar[str] = "ExerciseGym"


class ExercisePlan(CreativeWork, PhysicalActivity):
    """Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.

    https://schema.org/ExercisePlan
    """

    jsonld_type: ClassVar[str] = "ExercisePlan"
    activity_duration: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("activityDuration")
    ] = None
    activity_frequency: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("activityFrequency")
    ] = None
    additional_variable: Annotated[str | list[str] | None, prop("additionalVariable")] = None
    exercise_type: Annotated[str | list[str] | None, prop("exerciseType")] = None
    intensity: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("intensity")
    ] = None
    repetitions: Annotated[
        int | float | QuantitativeValue | list[int | float | QuantitativeValue] | None,
        prop("repetitions"),
    ] = None
    rest_periods: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("restPeriods")
    ] = None
    workload: Annotated[
        str | QuantitativeValue | list[str | QuantitativeValue] | None, prop("workload")
    ] = None


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    https://schema.org/FMRadioChannel
    """

    jsonld_type: ClassVar[str] = "FMRadioChannel"


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    https://schema.org/FastFoodRestaurant
    """

    jsonld_type: ClassVar[str] = "FastFoodRestaurant"


class FireStation(CivicStructure, EmergencyService):
    """A fire station.

    https://schema.org/FireStation
    """

    jsonld_type: ClassVar[str] = "FireStation"


class Florist(Store):
    """A florist.

    https://schema.org/Florist
    """

    jsonld_type: ClassVar[str] = "Florist"


class FurnitureStore(Store):
    """A furniture store.

    https://schema.org/FurnitureStore
    """

    jsonld_type: ClassVar[str] = "FurnitureStore"


class GardenStore(Store):
    """A garden store.

    https://schema.org/GardenStore
    """

    jsonld_type: ClassVar[str] = "GardenStore"


class GasStation(AutomotiveBusiness):
    """A gas station.

    https://schema.org/GasStation
    """

    jsonld_type: ClassVar[str] = "GasStation"


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    https://schema.org/GeneralContractor
    """

    jsonld_type: ClassVar[str] = "GeneralContractor"


class GeoCircle(GeoShape):
    """A GeoCircle is a GeoShape representing a circular geographic area.

    https://schema.org/GeoCircle
    """

    jsonld_type: ClassVar[str] = "GeoCircle"
    geo_midpoint: Annotated[GeoCoordinates | list[GeoCoordinates] | None, prop("geoMidpoint")] = (
        None
    )
    geo_radius: Annotated[str | int | float | list[str | int | float] | None, prop("geoRadius")] = (
        None
    )


class GolfCourse(SportsActivityLocation):
    """A golf course.

    https://schema.org/GolfCourse
    """

    jsonld_type: ClassVar[str] = "GolfCourse"


class GroceryStore(Store):
    """A grocery store.

    https://schema.org/GroceryStore
    """

    jsonld_type: ClassVar[str] = "GroceryStore"


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    https://schema.org/HVACBusiness
    """

    jsonld_type: ClassVar[str] = "HVACBusiness"


class HairSalon(HealthAndBeautyBusiness):
    """A hair salon.

    https://schema.org/HairSalon
    """

    jsonld_type: ClassVar[str] = "HairSalon"


class HardwareStore(Store):
    """A hardware store.

    https://schema.org/HardwareStore
    """

    jsonld_type: ClassVar[str] = "HardwareStore"


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club.

    https://schema.org/HealthClub
    """

    jsonld_type: ClassVar[str] = "HealthClub"


class HighSchool(EducationalOrganization):
    """A high school.

    https://schema.org/HighSchool
    """

    jsonld_type: ClassVar[str] = "HighSchool"


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    https://schema.org/HinduTemple
    """

    jsonld_type: ClassVar[str] = "HinduTemple"


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies.

    https://schema.org/HobbyShop
    """

    jsonld_type: ClassVar[str] = "HobbyShop"


class HomeGoodsStore(Store):
    """A home goods store.

    https://schema.org/HomeGoodsStore
    """

    jsonld_type: ClassVar[str] = "HomeGoodsStore"


class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    """A hospital.

    https://schema.org/Hospital
    """

    jsonld_type: ClassVar[str] = "Hospital"
    available_service: Annotated[
        MedicalProcedure
        | MedicalTest
        | MedicalTherapy
        | PhysicalExam
        | list[MedicalProcedure | MedicalTest | MedicalTherapy | PhysicalExam]
        | None,
        prop("availableService"),
    ] = None
    healthcare_reporting_data: Annotated[
        CDCPMDRecord | Dataset | list[CDCPMDRecord | Dataset] | None,
        prop("healthcareReportingData"),
    ] = None


class Hostel(LodgingBusiness):
    """A hostel - cheap accommodation, often in shared dormitories.

    https://schema.org/Hostel
    """

    jsonld_type: ClassVar[str] = "Hostel"


class Hotel(LodgingBusiness):
    """A hotel is an establishment that provides lodging paid on a short-term basis (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).

    https://schema.org/Hotel
    """

    jsonld_type: ClassVar[str] = "Hotel"


class HotelRoom(Room):
    """A hotel room is a single room in a hotel.

    https://schema.org/HotelRoom
    """

    jsonld_type: ClassVar[str] = "HotelRoom"


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    https://schema.org/HousePainter
    """

    jsonld_type: ClassVar[str] = "HousePainter"


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result.

    https://schema.org/HowToSupply
    """

    jsonld_type: ClassVar[str] = "HowToSupply"
    estimated_cost: Annotated[
        str | MonetaryAmount | list[str | MonetaryAmount] | None, prop("estimatedCost")
    ] = None


class HowToTool(HowToItem):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    https://schema.org/HowToTool
    """

    jsonld_type: ClassVar[str] = "HowToTool"


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    https://schema.org/IceCreamShop
    """

    jsonld_type: ClassVar[str] = "IceCreamShop"


class ImageObjectSnapshot(ImageObject):
    """A specific and exact (byte-for-byte) version of an ImageObject.

    https://schema.org/ImageObjectSnapshot
    """

    jsonld_type: ClassVar[str] = "ImageObjectSnapshot"


class InformAction(CommunicateAction):
    """The act of notifying someone of information pertinent to them, with no expectation of a response.

    https://schema.org/InformAction
    """

    jsonld_type: ClassVar[str] = "InformAction"
    event: Annotated[Event | list[Event] | None, prop("event")] = None


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection.

    https://schema.org/InsertAction
    """

    jsonld_type: ClassVar[str] = "InsertAction"
    to_location: Annotated[Place | list[Place] | None, prop("toLocation")] = None


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    https://schema.org/InsuranceAgency
    """

    jsonld_type: ClassVar[str] = "InsuranceAgency"


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.

    https://schema.org/InvestmentOrDeposit
    """

    jsonld_type: ClassVar[str] = "InvestmentOrDeposit"
    amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None, prop("amount")
    ] = None


class InviteAction(CommunicateAction):
    """The act of asking someone to attend an event.

    https://schema.org/InviteAction
    """

    jsonld_type: ClassVar[str] = "InviteAction"
    event: Annotated[Event | list[Event] | None, prop("event")] = None


class JewelryStore(Store):
    """A jewelry store.

    https://schema.org/JewelryStore
    """

    jsonld_type: ClassVar[str] = "JewelryStore"


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    https://schema.org/LakeBodyOfWater
    """

    jsonld_type: ClassVar[str] = "LakeBodyOfWater"


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    https://schema.org/LegislativeBuilding
    """

    jsonld_type: ClassVar[str] = "LegislativeBuilding"


class LikeAction(ReactAction):
    """The act of expressing a positive sentiment about the object.

    https://schema.org/LikeAction
    """

    jsonld_type: ClassVar[str] = "LikeAction"


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    https://schema.org/LiquorStore
    """

    jsonld_type: ClassVar[str] = "LiquorStore"


class LoanOrCredit(FinancialProduct):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

    https://schema.org/LoanOrCredit
    """

    jsonld_type: ClassVar[str] = "LoanOrCredit"
    amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None, prop("amount")
    ] = None
    currency: Annotated[str | list[str] | None, prop("currency")] = None
    grace_period: Annotated[str | list[str] | None, prop("gracePeriod")] = None
    loan_repayment_form: Annotated[
        RepaymentSpecification | list[RepaymentSpecification] | None, prop("loanRepaymentForm")
    ] = None
    loan_term: Annotated[QuantitativeValue | list[QuantitativeValue] | None, prop("loanTerm")] = (
        None
    )
    loan_type: Annotated[str | list[str] | None, prop("loanType")] = None
    recourse_loan: Annotated[bool | list[bool] | None, prop("recourseLoan")] = None
    renegotiable_loan: Annotated[bool | list[bool] | None, prop("renegotiableLoan")] = None
    required_collateral: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("requiredCollateral"),
    ] = None


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

    https://schema.org/LocationFeatureSpecification
    """

    jsonld_type: ClassVar[str] = "LocationFeatureSpecification"
    hours_available: Annotated[
        OpeningHoursSpecification | list[OpeningHoursSpecification] | None, prop("hoursAvailable")
    ] = None
    valid_from: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validFrom")
    ] = None
    valid_through: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("validThrough")
    ] = None


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    https://schema.org/Locksmith
    """

    jsonld_type: ClassVar[str] = "Locksmith"


class LymphaticVessel(Vessel):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.

    https://schema.org/LymphaticVessel
    """

    jsonld_type: ClassVar[str] = "LymphaticVessel"
    originates_from: Annotated[Vessel | list[Vessel] | None, prop("originatesFrom")] = None
    region_drained: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | list[AnatomicalStructure | AnatomicalSystem]
        | None,
        prop("regionDrained"),
    ] = None
    runs_to: Annotated[Vessel | list[Vessel] | None, prop("runsTo")] = None


class MaximumDoseSchedule(DoseSchedule):
    """The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer.

    https://schema.org/MaximumDoseSchedule
    """

    jsonld_type: ClassVar[str] = "MaximumDoseSchedule"


class MediaGallery(CollectionPage):
    """Web page type: Media gallery page.

    https://schema.org/MediaGallery
    """

    jsonld_type: ClassVar[str] = "MediaGallery"


class MedicalAudience(PeopleAudience):
    """Target audiences for medical web pages.

    https://schema.org/MedicalAudience
    """

    jsonld_type: ClassVar[str] = "MedicalAudience"


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare.

    https://schema.org/MedicalClinic
    """

    jsonld_type: ClassVar[str] = "MedicalClinic"
    available_service: Annotated[
        MedicalProcedure
        | MedicalTest
        | MedicalTherapy
        | PhysicalExam
        | list[MedicalProcedure | MedicalTest | MedicalTherapy | PhysicalExam]
        | None,
        prop("availableService"),
    ] = None


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    https://schema.org/MedicalCode
    """

    jsonld_type: ClassVar[str] = "MedicalCode"
    coding_system: Annotated[str | list[str] | None, prop("codingSystem")] = None


class MedicalScholarlyArticle(ScholarlyArticle):
    """A scholarly article in the medical domain.

    https://schema.org/MedicalScholarlyArticle
    """

    jsonld_type: ClassVar[str] = "MedicalScholarlyArticle"
    publication_type: Annotated[str | list[str] | None, prop("publicationType")] = None


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.

    https://schema.org/MedicalSign
    """

    jsonld_type: ClassVar[str] = "MedicalSign"
    identifying_exam: Annotated[
        PhysicalExam | list[PhysicalExam] | None, prop("identifyingExam")
    ] = None
    identifying_test: Annotated[MedicalTest | list[MedicalTest] | None, prop("identifyingTest")] = (
        None
    )


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective) like stomachache, lower-back pain, or fatigue.

    https://schema.org/MedicalSymptom
    """

    jsonld_type: ClassVar[str] = "MedicalSymptom"


class MedicalTherapy(TherapeuticProcedure):
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies.

    https://schema.org/MedicalTherapy
    """

    jsonld_type: ClassVar[str] = "MedicalTherapy"
    contraindication: Annotated[
        str | MedicalContraindication | list[str | MedicalContraindication] | None,
        prop("contraindication"),
    ] = None
    duplicate_therapy: Annotated[
        MedicalTherapy | list[MedicalTherapy] | None, prop("duplicateTherapy")
    ] = None
    serious_adverse_outcome: Annotated[
        MedicalEntity | PhysicalExam | list[MedicalEntity | PhysicalExam] | None,
        prop("seriousAdverseOutcome"),
    ] = None


class MeetingRoom(Room):
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Conference_hall).

    https://schema.org/MeetingRoom
    """

    jsonld_type: ClassVar[str] = "MeetingRoom"


class MensClothingStore(Store):
    """A men's clothing store.

    https://schema.org/MensClothingStore
    """

    jsonld_type: ClassVar[str] = "MensClothingStore"


class MiddleSchool(EducationalOrganization):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    https://schema.org/MiddleSchool
    """

    jsonld_type: ClassVar[str] = "MiddleSchool"


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories.

    https://schema.org/MobilePhoneStore
    """

    jsonld_type: ClassVar[str] = "MobilePhoneStore"


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """A statistical distribution of monetary amounts.

    https://schema.org/MonetaryAmountDistribution
    """

    jsonld_type: ClassVar[str] = "MonetaryAmountDistribution"
    currency: Annotated[str | list[str] | None, prop("currency")] = None


class Mosque(PlaceOfWorship):
    """A mosque.

    https://schema.org/Mosque
    """

    jsonld_type: ClassVar[str] = "Mosque"


class Motel(LodgingBusiness):
    """A motel.

    https://schema.org/Motel
    """

    jsonld_type: ClassVar[str] = "Motel"


class MotorcycleDealer(AutomotiveBusiness):
    """A motorcycle dealer.

    https://schema.org/MotorcycleDealer
    """

    jsonld_type: ClassVar[str] = "MotorcycleDealer"


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    https://schema.org/MotorcycleRepair
    """

    jsonld_type: ClassVar[str] = "MotorcycleRepair"


class MovieRentalStore(Store):
    """A movie rental store.

    https://schema.org/MovieRentalStore
    """

    jsonld_type: ClassVar[str] = "MovieRentalStore"


class MovieSeries(CreativeWorkSeries):
    """A series of movies.

    https://schema.org/MovieSeries
    """

    jsonld_type: ClassVar[str] = "MovieSeries"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class MovieTheater(CivicStructure, EntertainmentBusiness):
    """A movie theater.

    https://schema.org/MovieTheater
    """

    jsonld_type: ClassVar[str] = "MovieTheater"
    screen_count: Annotated[int | float | list[int | float] | None, prop("screenCount")] = None


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    https://schema.org/MovingCompany
    """

    jsonld_type: ClassVar[str] = "MovingCompany"


class MusicStore(Store):
    """A music store.

    https://schema.org/MusicStore
    """

    jsonld_type: ClassVar[str] = "MusicStore"


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    https://schema.org/NailSalon
    """

    jsonld_type: ClassVar[str] = "NailSalon"


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    https://schema.org/NightClub
    """

    jsonld_type: ClassVar[str] = "NightClub"


class Notary(LegalService):
    """A notary.

    https://schema.org/Notary
    """

    jsonld_type: ClassVar[str] = "Notary"


class Observation(QuantitativeValue):
    """Instances of the class Observation are used to specify observations about an entity at a particular time.

    https://schema.org/Observation
    """

    jsonld_type: ClassVar[str] = "Observation"
    margin_of_error: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("marginOfError")
    ] = None
    measurement_denominator: Annotated[
        StatisticalVariable | list[StatisticalVariable] | None, prop("measurementDenominator")
    ] = None
    measurement_method: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementMethod"),
    ] = None
    measurement_qualifier: Annotated[
        Enumeration | SchemaEnumeration | list[Enumeration | SchemaEnumeration] | None,
        prop("measurementQualifier"),
    ] = None
    measurement_technique: Annotated[
        str
        | DefinedTerm
        | MeasurementMethodEnum
        | list[str | DefinedTerm | MeasurementMethodEnum]
        | None,
        prop("measurementTechnique"),
    ] = None
    observation_about: Annotated[
        Place | SchemaEnumeration | Thing | list[Place | SchemaEnumeration | Thing] | None,
        prop("observationAbout"),
    ] = None
    observation_date: Annotated[
        _dt.date | _dt.datetime | list[_dt.date | _dt.datetime] | None, prop("observationDate")
    ] = None
    observation_period: Annotated[str | list[str] | None, prop("observationPeriod")] = None
    variable_measured: Annotated[
        str
        | PropertyValue
        | StatisticalVariable
        | list[str | PropertyValue | StatisticalVariable]
        | None,
        prop("variableMeasured"),
    ] = None


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific).

    https://schema.org/OceanBodyOfWater
    """

    jsonld_type: ClassVar[str] = "OceanBodyOfWater"


class OfficeEquipmentStore(Store):
    """An office equipment store.

    https://schema.org/OfficeEquipmentStore
    """

    jsonld_type: ClassVar[str] = "OfficeEquipmentStore"


class OnlineMarketplace(OnlineStore):
    """An eCommerce marketplace.

    https://schema.org/OnlineMarketplace
    """

    jsonld_type: ClassVar[str] = "OnlineMarketplace"
    has_store: Annotated[OnlineStore | list[OnlineStore] | None, prop("hasStore")] = None


class OpinionNewsArticle(NewsArticle):
    """An OpinionNewsArticle is a NewsArticle that primarily expresses opinions rather than journalistic reporting of news and events.

    https://schema.org/OpinionNewsArticle
    """

    jsonld_type: ClassVar[str] = "OpinionNewsArticle"


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision.

    https://schema.org/Optician
    """

    jsonld_type: ClassVar[str] = "Optician"


class OutletStore(Store):
    """An outlet store.

    https://schema.org/OutletStore
    """

    jsonld_type: ClassVar[str] = "OutletStore"


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    https://schema.org/ParentAudience
    """

    jsonld_type: ClassVar[str] = "ParentAudience"
    child_max_age: Annotated[int | float | list[int | float] | None, prop("childMaxAge")] = None
    child_min_age: Annotated[int | float | list[int | float] | None, prop("childMinAge")] = None


class PawnShop(Store):
    """A shop that will buy, or lend money against the security of, personal possessions.

    https://schema.org/PawnShop
    """

    jsonld_type: ClassVar[str] = "PawnShop"


class PaymentCard(FinancialProduct, PaymentMethod):
    """A payment method using a credit, debit, store or other card to associate the payment with an account.

    https://schema.org/PaymentCard
    """

    jsonld_type: ClassVar[str] = "PaymentCard"
    cash_back: Annotated[bool | int | float | list[bool | int | float] | None, prop("cashBack")] = (
        None
    )
    contactless_payment: Annotated[bool | list[bool] | None, prop("contactlessPayment")] = None
    floor_limit: Annotated[MonetaryAmount | list[MonetaryAmount] | None, prop("floorLimit")] = None
    monthly_minimum_repayment_amount: Annotated[
        int | float | MonetaryAmount | list[int | float | MonetaryAmount] | None,
        prop("monthlyMinimumRepaymentAmount"),
    ] = None


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    https://schema.org/PaymentChargeSpecification
    """

    jsonld_type: ClassVar[str] = "PaymentChargeSpecification"
    applies_to_delivery_method: Annotated[
        DeliveryMethod | list[DeliveryMethod] | None, prop("appliesToDeliveryMethod")
    ] = None
    applies_to_payment_method: Annotated[
        PaymentMethod | list[PaymentMethod] | None, prop("appliesToPaymentMethod")
    ] = None


class PaymentService(FinancialProduct, PaymentMethod):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    https://schema.org/PaymentService
    """

    jsonld_type: ClassVar[str] = "PaymentService"


class Periodical(CreativeWorkSeries):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.\\n\\nSee also blog post.

    https://schema.org/Periodical
    """

    jsonld_type: ClassVar[str] = "Periodical"


class PetStore(Store):
    """A pet store.

    https://schema.org/PetStore
    """

    jsonld_type: ClassVar[str] = "PetStore"


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    https://schema.org/Pharmacy
    """

    jsonld_type: ClassVar[str] = "Pharmacy"


class Physician(MedicalBusiness, MedicalOrganization):
    """An individual physician or a physician's office considered as a MedicalOrganization.

    https://schema.org/Physician
    """

    jsonld_type: ClassVar[str] = "Physician"
    available_service: Annotated[
        MedicalProcedure
        | MedicalTest
        | MedicalTherapy
        | PhysicalExam
        | list[MedicalProcedure | MedicalTest | MedicalTherapy | PhysicalExam]
        | None,
        prop("availableService"),
    ] = None
    hospital_affiliation: Annotated[
        Hospital | list[Hospital] | None, prop("hospitalAffiliation")
    ] = None


class Plumber(HomeAndConstructionBusiness):
    """A plumbing service.

    https://schema.org/Plumber
    """

    jsonld_type: ClassVar[str] = "Plumber"


class PoliceStation(CivicStructure, EmergencyService):
    """A police station.

    https://schema.org/PoliceStation
    """

    jsonld_type: ClassVar[str] = "PoliceStation"


class Pond(BodyOfWater):
    """A pond.

    https://schema.org/Pond
    """

    jsonld_type: ClassVar[str] = "Pond"


class PostOffice(GovernmentOffice):
    """A post office.

    https://schema.org/PostOffice
    """

    jsonld_type: ClassVar[str] = "PostOffice"


class PostalAddress(ContactPoint):
    """The mailing address.

    https://schema.org/PostalAddress
    """

    jsonld_type: ClassVar[str] = "PostalAddress"
    address_country: Annotated[
        str | Country | list[str | Country] | None, prop("addressCountry")
    ] = None
    address_locality: Annotated[str | list[str] | None, prop("addressLocality")] = None
    address_region: Annotated[
        str | AdministrativeArea | list[str | AdministrativeArea] | None, prop("addressRegion")
    ] = None
    extended_address: Annotated[str | list[str] | None, prop("extendedAddress")] = None
    post_office_box_number: Annotated[str | list[str] | None, prop("postOfficeBoxNumber")] = None
    postal_code: Annotated[str | list[str] | None, prop("postalCode")] = None
    street_address: Annotated[str | list[str] | None, prop("streetAddress")] = None


class Preschool(EducationalOrganization):
    """A preschool.

    https://schema.org/Preschool
    """

    jsonld_type: ClassVar[str] = "Preschool"


class PsychologicalTreatment(TherapeuticProcedure):
    """A process of care relying upon counseling, dialogue and communication aimed at improving a mental health condition without use of drugs.

    https://schema.org/PsychologicalTreatment
    """

    jsonld_type: ClassVar[str] = "PsychologicalTreatment"


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    https://schema.org/PublicSwimmingPool
    """

    jsonld_type: ClassVar[str] = "PublicSwimmingPool"


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air or online.

    https://schema.org/RadioBroadcastService
    """

    jsonld_type: ClassVar[str] = "RadioBroadcastService"


class RadioSeries(CreativeWorkSeries):
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    https://schema.org/RadioSeries
    """

    jsonld_type: ClassVar[str] = "RadioSeries"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    contains_season: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None, prop("containsSeason")
    ] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    episode: Annotated[Episode | list[Episode] | None, prop("episode")] = None
    episodes: Annotated[
        Episode | list[Episode] | None, prop("episodes", superseded_by=("episode",))
    ] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    number_of_episodes: Annotated[int | list[int] | None, prop("numberOfEpisodes")] = None
    number_of_seasons: Annotated[int | list[int] | None, prop("numberOfSeasons")] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    season: Annotated[
        str | CreativeWorkSeason | list[str | CreativeWorkSeason] | None,
        prop("season", superseded_by=("containsSeason",)),
    ] = None
    seasons: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None,
        prop("seasons", superseded_by=("season",)),
    ] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class RecommendedDoseSchedule(DoseSchedule):
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer.

    https://schema.org/RecommendedDoseSchedule
    """

    jsonld_type: ClassVar[str] = "RecommendedDoseSchedule"


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object.\\n\\nRelated actions:\\n\\n* AcceptAction: The antonym of RejectAction.

    https://schema.org/RejectAction
    """

    jsonld_type: ClassVar[str] = "RejectAction"


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object.

    https://schema.org/ReplyAction
    """

    jsonld_type: ClassVar[str] = "ReplyAction"
    result_comment: Annotated[Comment | list[Comment] | None, prop("resultComment")] = None


class ReportageNewsArticle(NewsArticle):
    """The ReportageNewsArticle type is a subtype of NewsArticle representing news articles which are the result of journalistic news reporting conventions.

    https://schema.org/ReportageNewsArticle
    """

    jsonld_type: ClassVar[str] = "ReportageNewsArticle"


class ReportedDoseSchedule(DoseSchedule):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    https://schema.org/ReportedDoseSchedule
    """

    jsonld_type: ClassVar[str] = "ReportedDoseSchedule"


class ReserveAction(PlanAction):
    """Reserving a concrete object.\\n\\nRelated actions:\\n\\n* ScheduleAction: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

    https://schema.org/ReserveAction
    """

    jsonld_type: ClassVar[str] = "ReserveAction"


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    https://schema.org/Reservoir
    """

    jsonld_type: ClassVar[str] = "Reservoir"


class Resort(LodgingBusiness):
    """A resort is a place used for relaxation or recreation, attracting visitors for holidays or vacations.

    https://schema.org/Resort
    """

    jsonld_type: ClassVar[str] = "Resort"


class Restaurant(FoodEstablishment):
    """A restaurant.

    https://schema.org/Restaurant
    """

    jsonld_type: ClassVar[str] = "Restaurant"


class ReviewNewsArticle(CriticReview, NewsArticle):
    """A NewsArticle and CriticReview providing a professional critic's assessment of a service, product, performance, or artistic or literary work.

    https://schema.org/ReviewNewsArticle
    """

    jsonld_type: ClassVar[str] = "ReviewNewsArticle"


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon).

    https://schema.org/RiverBodyOfWater
    """

    jsonld_type: ClassVar[str] = "RiverBodyOfWater"


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    https://schema.org/RoofingContractor
    """

    jsonld_type: ClassVar[str] = "RoofingContractor"


class ScheduleAction(PlanAction):
    """Scheduling future actions, events, or tasks.\\n\\nRelated actions:\\n\\n* ReserveAction: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

    https://schema.org/ScheduleAction
    """

    jsonld_type: ClassVar[str] = "ScheduleAction"


class School(EducationalOrganization):
    """A school.

    https://schema.org/School
    """

    jsonld_type: ClassVar[str] = "School"


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea).

    https://schema.org/SeaBodyOfWater
    """

    jsonld_type: ClassVar[str] = "SeaBodyOfWater"


class ShareAction(CommunicateAction):
    """The act of distributing content to people for their amusement or edification.

    https://schema.org/ShareAction
    """

    jsonld_type: ClassVar[str] = "ShareAction"


class ShoeStore(Store):
    """A shoe store.

    https://schema.org/ShoeStore
    """

    jsonld_type: ClassVar[str] = "ShoeStore"


class SingleFamilyResidence(House):
    """Residence type: Single-family home.

    https://schema.org/SingleFamilyResidence
    """

    jsonld_type: ClassVar[str] = "SingleFamilyResidence"


class SizeSpecification(QualitativeValue):
    """Size related properties of a product, typically a size code (name) and optionally a sizeSystem, sizeGroup, and product measurements (hasMeasurement).

    https://schema.org/SizeSpecification
    """

    jsonld_type: ClassVar[str] = "SizeSpecification"
    has_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("hasMeasurement")
    ] = None
    size_group: Annotated[
        str
        | SizeGroupEnumeration
        | WearableSizeGroupEnumeration
        | list[str | SizeGroupEnumeration | WearableSizeGroupEnumeration]
        | None,
        prop("sizeGroup"),
    ] = None
    size_system: Annotated[
        str
        | SizeSystemEnumeration
        | WearableSizeSystemEnumeration
        | list[str | SizeSystemEnumeration | WearableSizeSystemEnumeration]
        | None,
        prop("sizeSystem"),
    ] = None
    suggested_age: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("suggestedAge")
    ] = None
    suggested_gender: Annotated[
        str | GenderType | list[str | GenderType] | None, prop("suggestedGender")
    ] = None
    suggested_measurement: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("suggestedMeasurement")
    ] = None


class SportingGoodsStore(Store):
    """A sporting goods store.

    https://schema.org/SportingGoodsStore
    """

    jsonld_type: ClassVar[str] = "SportingGoodsStore"


class SportsClub(SportsActivityLocation):
    """A sports club.

    https://schema.org/SportsClub
    """

    jsonld_type: ClassVar[str] = "SportsClub"


class StadiumOrArena(CivicStructure, SportsActivityLocation):
    """A stadium.

    https://schema.org/StadiumOrArena
    """

    jsonld_type: ClassVar[str] = "StadiumOrArena"


class Synagogue(PlaceOfWorship):
    """A synagogue.

    https://schema.org/Synagogue
    """

    jsonld_type: ClassVar[str] = "Synagogue"


class TVSeries(CreativeWorkSeries):
    """CreativeWorkSeries dedicated to TV broadcast and associated online delivery.

    https://schema.org/TVSeries
    """

    jsonld_type: ClassVar[str] = "TVSeries"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    contains_season: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None, prop("containsSeason")
    ] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    episode: Annotated[Episode | list[Episode] | None, prop("episode")] = None
    episodes: Annotated[
        Episode | list[Episode] | None, prop("episodes", superseded_by=("episode",))
    ] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    number_of_episodes: Annotated[int | list[int] | None, prop("numberOfEpisodes")] = None
    number_of_seasons: Annotated[int | list[int] | None, prop("numberOfSeasons")] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    season: Annotated[
        str | CreativeWorkSeason | list[str | CreativeWorkSeason] | None,
        prop("season", superseded_by=("containsSeason",)),
    ] = None
    seasons: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None,
        prop("seasons", superseded_by=("season",)),
    ] = None
    title_eidr: Annotated[str | list[str] | None, prop("titleEIDR")] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    https://schema.org/TattooParlor
    """

    jsonld_type: ClassVar[str] = "TattooParlor"


class TennisComplex(SportsActivityLocation):
    """A tennis complex.

    https://schema.org/TennisComplex
    """

    jsonld_type: ClassVar[str] = "TennisComplex"


class TireShop(Store):
    """A tire shop.

    https://schema.org/TireShop
    """

    jsonld_type: ClassVar[str] = "TireShop"


class ToyStore(Store):
    """A toy store.

    https://schema.org/ToyStore
    """

    jsonld_type: ClassVar[str] = "ToyStore"


class UnitPriceSpecification(PriceSpecification):
    """The price asked for a given offer by the respective organization or person.

    https://schema.org/UnitPriceSpecification
    """

    jsonld_type: ClassVar[str] = "UnitPriceSpecification"
    billing_duration: Annotated[
        str | int | float | QuantitativeValue | list[str | int | float | QuantitativeValue] | None,
        prop("billingDuration"),
    ] = None
    billing_increment: Annotated[
        int | float | list[int | float] | None, prop("billingIncrement")
    ] = None
    billing_start: Annotated[int | float | list[int | float] | None, prop("billingStart")] = None
    price_component_type: Annotated[
        PriceComponentTypeEnumeration | list[PriceComponentTypeEnumeration] | None,
        prop("priceComponentType"),
    ] = None
    price_type: Annotated[
        str | PriceTypeEnumeration | list[str | PriceTypeEnumeration] | None, prop("priceType")
    ] = None
    reference_quantity: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("referenceQuantity")
    ] = None
    unit_code: Annotated[str | list[str] | None, prop("unitCode")] = None
    unit_text: Annotated[str | list[str] | None, prop("unitText")] = None


class VacationRental(LodgingBusiness):
    """A kind of lodging business that focuses on renting single properties for limited time.

    https://schema.org/VacationRental
    """

    jsonld_type: ClassVar[str] = "VacationRental"


class Vein(Vessel):
    """A type of blood vessel that specifically carries blood to the heart.

    https://schema.org/Vein
    """

    jsonld_type: ClassVar[str] = "Vein"
    drains_to: Annotated[Vessel | list[Vessel] | None, prop("drainsTo")] = None
    region_drained: Annotated[
        AnatomicalStructure
        | AnatomicalSystem
        | list[AnatomicalStructure | AnatomicalSystem]
        | None,
        prop("regionDrained"),
    ] = None
    tributary: Annotated[
        AnatomicalStructure | list[AnatomicalStructure] | None, prop("tributary")
    ] = None


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    https://schema.org/VideoGameSeries
    """

    jsonld_type: ClassVar[str] = "VideoGameSeries"
    actor: Annotated[
        PerformingGroup | Person | list[PerformingGroup | Person] | None, prop("actor")
    ] = None
    actors: Annotated[Person | list[Person] | None, prop("actors", superseded_by=("actor",))] = None
    character_attribute: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None,
        prop("characterAttribute"),
    ] = None
    cheat_code: Annotated[CreativeWork | list[CreativeWork] | None, prop("cheatCode")] = None
    contains_season: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None, prop("containsSeason")
    ] = None
    director: Annotated[Person | list[Person] | None, prop("director")] = None
    directors: Annotated[
        Person | list[Person] | None, prop("directors", superseded_by=("director",))
    ] = None
    episode: Annotated[Episode | list[Episode] | None, prop("episode")] = None
    episodes: Annotated[
        Episode | list[Episode] | None, prop("episodes", superseded_by=("episode",))
    ] = None
    game_item: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("gameItem")
    ] = None
    game_location: Annotated[
        str | Place | PostalAddress | list[str | Place | PostalAddress] | None, prop("gameLocation")
    ] = None
    game_platform: Annotated[
        str | SchemaEnumeration | Thing | list[str | SchemaEnumeration | Thing] | None,
        prop("gamePlatform"),
    ] = None
    music_by: Annotated[MusicGroup | Person | list[MusicGroup | Person] | None, prop("musicBy")] = (
        None
    )
    number_of_episodes: Annotated[int | list[int] | None, prop("numberOfEpisodes")] = None
    number_of_players: Annotated[
        QuantitativeValue | list[QuantitativeValue] | None, prop("numberOfPlayers")
    ] = None
    number_of_seasons: Annotated[int | list[int] | None, prop("numberOfSeasons")] = None
    play_mode: Annotated[GamePlayMode | list[GamePlayMode] | None, prop("playMode")] = None
    production_company: Annotated[
        Organization | list[Organization] | None, prop("productionCompany")
    ] = None
    quest: Annotated[
        SchemaEnumeration | Thing | list[SchemaEnumeration | Thing] | None, prop("quest")
    ] = None
    season: Annotated[
        str | CreativeWorkSeason | list[str | CreativeWorkSeason] | None,
        prop("season", superseded_by=("containsSeason",)),
    ] = None
    seasons: Annotated[
        CreativeWorkSeason | list[CreativeWorkSeason] | None,
        prop("seasons", superseded_by=("season",)),
    ] = None
    trailer: Annotated[VideoObject | list[VideoObject] | None, prop("trailer")] = None


class VideoObjectSnapshot(VideoObject):
    """A specific and exact (byte-for-byte) version of a VideoObject.

    https://schema.org/VideoObjectSnapshot
    """

    jsonld_type: ClassVar[str] = "VideoObjectSnapshot"


class VoteAction(ChooseAction):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options.

    https://schema.org/VoteAction
    """

    jsonld_type: ClassVar[str] = "VoteAction"
    candidate: Annotated[Person | list[Person] | None, prop("candidate")] = None


class WantAction(ReactAction):
    """The act of expressing a desire about the object.

    https://schema.org/WantAction
    """

    jsonld_type: ClassVar[str] = "WantAction"


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara.

    https://schema.org/Waterfall
    """

    jsonld_type: ClassVar[str] = "Waterfall"


class WearAction(UseAction):
    """The act of dressing oneself in clothing.

    https://schema.org/WearAction
    """

    jsonld_type: ClassVar[str] = "WearAction"


class WholesaleStore(Store):
    """A wholesale store.

    https://schema.org/WholesaleStore
    """

    jsonld_type: ClassVar[str] = "WholesaleStore"


class Winery(FoodEstablishment):
    """A winery.

    https://schema.org/Winery
    """

    jsonld_type: ClassVar[str] = "Winery"


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection.

    https://schema.org/AppendAction
    """

    jsonld_type: ClassVar[str] = "AppendAction"


class BrokerageAccount(InvestmentOrDeposit):
    """An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.

    https://schema.org/BrokerageAccount
    """

    jsonld_type: ClassVar[str] = "BrokerageAccount"


class CatholicChurch(Church):
    """A Catholic church.

    https://schema.org/CatholicChurch
    """

    jsonld_type: ClassVar[str] = "CatholicChurch"


class ComicSeries(Periodical):
    """A sequential publication of comic stories under a unifying title, for example "The Amazing Spider-Man" or "Groo the Wanderer".

    https://schema.org/ComicSeries
    """

    jsonld_type: ClassVar[str] = "ComicSeries"


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected.\\n\\nRelated actions:\\n\\n* CancelAction: The antonym of ConfirmAction.

    https://schema.org/ConfirmAction
    """

    jsonld_type: ClassVar[str] = "ConfirmAction"


class CovidTestingFacility(MedicalClinic):
    """A CovidTestingFacility is a MedicalClinic where testing for the COVID-19 Coronavirus disease is available.

    https://schema.org/CovidTestingFacility
    """

    jsonld_type: ClassVar[str] = "CovidTestingFacility"


class CreditCard(LoanOrCredit, PaymentCard):
    """A card payment method of a particular brand or name.

    https://schema.org/CreditCard
    """

    jsonld_type: ClassVar[str] = "CreditCard"


class DepositAccount(BankAccount, InvestmentOrDeposit):
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.

    https://schema.org/DepositAccount
    """

    jsonld_type: ClassVar[str] = "DepositAccount"


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    https://schema.org/ImageGallery
    """

    jsonld_type: ClassVar[str] = "ImageGallery"


class IndividualPhysician(Physician):
    """An individual medical practitioner.

    https://schema.org/IndividualPhysician
    """

    jsonld_type: ClassVar[str] = "IndividualPhysician"


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.

    https://schema.org/InvestmentFund
    """

    jsonld_type: ClassVar[str] = "InvestmentFund"


class LiveBlogPosting(BlogPosting):
    """A LiveBlogPosting is a BlogPosting intended to provide a rolling textual coverage of an ongoing event through continuous updates.

    https://schema.org/LiveBlogPosting
    """

    jsonld_type: ClassVar[str] = "LiveBlogPosting"
    coverage_end_time: Annotated[
        _dt.datetime | list[_dt.datetime] | None, prop("coverageEndTime")
    ] = None
    coverage_start_time: Annotated[
        _dt.datetime | list[_dt.datetime] | None, prop("coverageStartTime")
    ] = None
    live_blog_update: Annotated[BlogPosting | list[BlogPosting] | None, prop("liveBlogUpdate")] = (
        None
    )


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral.

    https://schema.org/MortgageLoan
    """

    jsonld_type: ClassVar[str] = "MortgageLoan"
    domiciled_mortgage: Annotated[bool | list[bool] | None, prop("domiciledMortgage")] = None
    loan_mortgage_mandate_amount: Annotated[
        MonetaryAmount | list[MonetaryAmount] | None, prop("loanMortgageMandateAmount")
    ] = None


class Newspaper(Periodical):
    """A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education).

    https://schema.org/Newspaper
    """

    jsonld_type: ClassVar[str] = "Newspaper"


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.

    https://schema.org/OccupationalTherapy
    """

    jsonld_type: ClassVar[str] = "OccupationalTherapy"


class PalliativeProcedure(MedicalTherapy):
    """A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.

    https://schema.org/PalliativeProcedure
    """

    jsonld_type: ClassVar[str] = "PalliativeProcedure"


class Patient(MedicalAudience, Person):
    """A patient is any person recipient of health care services.

    https://schema.org/Patient
    """

    jsonld_type: ClassVar[str] = "Patient"
    diagnosis: Annotated[MedicalCondition | list[MedicalCondition] | None, prop("diagnosis")] = None
    drug: Annotated[Drug | list[Drug] | None, prop("drug")] = None


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health condition.

    https://schema.org/PhysicalTherapy
    """

    jsonld_type: ClassVar[str] = "PhysicalTherapy"


class PhysiciansOffice(Physician):
    """A doctor's office or clinic.

    https://schema.org/PhysiciansOffice
    """

    jsonld_type: ClassVar[str] = "PhysiciansOffice"


class PrependAction(InsertAction):
    """The act of inserting at the beginning if an ordered collection.

    https://schema.org/PrependAction
    """

    jsonld_type: ClassVar[str] = "PrependAction"


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition.

    https://schema.org/RadiationTherapy
    """

    jsonld_type: ClassVar[str] = "RadiationTherapy"


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    https://schema.org/RsvpAction
    """

    jsonld_type: ClassVar[str] = "RsvpAction"
    additional_number_of_guests: Annotated[
        int | float | list[int | float] | None, prop("additionalNumberOfGuests")
    ] = None
    comment: Annotated[Comment | list[Comment] | None, prop("comment")] = None
    rsvp_response: Annotated[
        RsvpResponseType | list[RsvpResponseType] | None, prop("rsvpResponse")
    ] = None


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort.

    https://schema.org/SkiResort
    """

    jsonld_type: ClassVar[str] = "SkiResort"


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page.

    https://schema.org/VideoGallery
    """

    jsonld_type: ClassVar[str] = "VideoGallery"


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions.

    https://schema.org/VitalSign
    """

    jsonld_type: ClassVar[str] = "VitalSign"
