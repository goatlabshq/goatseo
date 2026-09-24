"""Schema.org enumerations, generated from Schema.org 30.1.

Do not edit: run `uv run goatseo-schema generate` instead.
"""

from goatseo.schema.base import SchemaEnumeration

__all__ = [
    "ActionStatusType",
    "BoardingPolicyType",
    "BodyMeasurementTypeEnumeration",
    "BookFormatType",
    "CarUsageType",
    "CertificationStatusEnumeration",
    "ContactPointOption",
    "DayOfWeek",
    "DeliveryMethod",
    "DigitalDocumentPermissionType",
    "DigitalPlatformEnumeration",
    "DriveWheelConfigurationValue",
    "DrugCostCategory",
    "DrugPregnancyCategory",
    "DrugPrescriptionStatus",
    "EUEnergyEfficiencyEnumeration",
    "EnergyStarEnergyEfficiencyEnumeration",
    "EventAttendanceModeEnumeration",
    "EventStatusType",
    "FulfillmentTypeEnumeration",
    "GameAvailabilityEnumeration",
    "GamePlayMode",
    "GameServerStatus",
    "GenderType",
    "GovernmentBenefitsType",
    "HealthAspectEnumeration",
    "IPTCDigitalSourceEnumeration",
    "IncentiveQualifiedExpenseType",
    "IncentiveStatus",
    "IncentiveType",
    "InfectiousAgentClass",
    "ItemAvailability",
    "ItemListOrderType",
    "LegalForceStatus",
    "LegalValueLevel",
    "MapCategoryType",
    "MeasurementMethodEnum",
    "MediaManipulationRatingEnumeration",
    "MedicalAudienceType",
    "MedicalDevicePurpose",
    "MedicalEvidenceLevel",
    "MedicalImagingTechnique",
    "MedicalObservationalStudyDesign",
    "MedicalProcedureType",
    "MedicalSpecialty",
    "MedicalStudyStatus",
    "MedicalTrialDesign",
    "MedicineSystem",
    "MerchantReturnEnumeration",
    "MusicAlbumProductionType",
    "MusicAlbumReleaseType",
    "MusicReleaseFormatType",
    "NLNonprofitType",
    "OfferItemCondition",
    "OrderStatus",
    "PaymentMethodType",
    "PaymentStatusType",
    "PhysicalActivityCategory",
    "PhysicalExam",
    "PriceComponentTypeEnumeration",
    "PriceTypeEnumeration",
    "ProductReturnEnumeration",
    "PurchaseType",
    "RefundTypeEnumeration",
    "ReservationStatusType",
    "RestrictedDiet",
    "ReturnFeesEnumeration",
    "ReturnLabelSourceEnumeration",
    "ReturnMethodEnumeration",
    "RsvpResponseType",
    "SizeSystemEnumeration",
    "SteeringPositionValue",
    "TierBenefitEnumeration",
    "UKNonprofitType",
    "USNonprofitType",
    "WearableMeasurementTypeEnumeration",
    "WearableSizeGroupEnumeration",
    "WearableSizeSystemEnumeration",
]


class ActionStatusType(SchemaEnumeration):
    """The status of an Action.

    https://schema.org/ActionStatusType
    """

    ActiveActionStatus = "https://schema.org/ActiveActionStatus"
    CompletedActionStatus = "https://schema.org/CompletedActionStatus"
    FailedActionStatus = "https://schema.org/FailedActionStatus"
    PotentialActionStatus = "https://schema.org/PotentialActionStatus"


class BoardingPolicyType(SchemaEnumeration):
    """A type of boarding policy used by an airline.

    https://schema.org/BoardingPolicyType
    """

    GroupBoardingPolicy = "https://schema.org/GroupBoardingPolicy"
    ZoneBoardingPolicy = "https://schema.org/ZoneBoardingPolicy"


class BodyMeasurementTypeEnumeration(SchemaEnumeration):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.

    https://schema.org/BodyMeasurementTypeEnumeration
    """

    BodyMeasurementArm = "https://schema.org/BodyMeasurementArm"
    BodyMeasurementBust = "https://schema.org/BodyMeasurementBust"
    BodyMeasurementChest = "https://schema.org/BodyMeasurementChest"
    BodyMeasurementFoot = "https://schema.org/BodyMeasurementFoot"
    BodyMeasurementHand = "https://schema.org/BodyMeasurementHand"
    BodyMeasurementHead = "https://schema.org/BodyMeasurementHead"
    BodyMeasurementHeight = "https://schema.org/BodyMeasurementHeight"
    BodyMeasurementHips = "https://schema.org/BodyMeasurementHips"
    BodyMeasurementInsideLeg = "https://schema.org/BodyMeasurementInsideLeg"
    BodyMeasurementNeck = "https://schema.org/BodyMeasurementNeck"
    BodyMeasurementUnderbust = "https://schema.org/BodyMeasurementUnderbust"
    BodyMeasurementWaist = "https://schema.org/BodyMeasurementWaist"
    BodyMeasurementWeight = "https://schema.org/BodyMeasurementWeight"


class BookFormatType(SchemaEnumeration):
    """The publication format of the book.

    https://schema.org/BookFormatType
    """

    AudiobookFormat = "https://schema.org/AudiobookFormat"
    EBook = "https://schema.org/EBook"
    GraphicNovel = "https://schema.org/GraphicNovel"
    Hardcover = "https://schema.org/Hardcover"
    Pamphlet = "https://schema.org/Pamphlet"
    Paperback = "https://schema.org/Paperback"


class CarUsageType(SchemaEnumeration):
    """A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.

    https://schema.org/CarUsageType
    """

    DrivingSchoolVehicleUsage = "https://schema.org/DrivingSchoolVehicleUsage"
    RentalVehicleUsage = "https://schema.org/RentalVehicleUsage"
    TaxiVehicleUsage = "https://schema.org/TaxiVehicleUsage"


class CertificationStatusEnumeration(SchemaEnumeration):
    """Enumerates the different statuses of a Certification (Active and Inactive).

    https://schema.org/CertificationStatusEnumeration
    """

    CertificationActive = "https://schema.org/CertificationActive"
    CertificationInactive = "https://schema.org/CertificationInactive"


class ContactPointOption(SchemaEnumeration):
    """Enumerated options related to a ContactPoint.

    https://schema.org/ContactPointOption
    """

    HearingImpairedSupported = "https://schema.org/HearingImpairedSupported"
    TollFree = "https://schema.org/TollFree"


class DayOfWeek(SchemaEnumeration):
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.

    https://schema.org/DayOfWeek
    """

    Friday = "https://schema.org/Friday"
    Monday = "https://schema.org/Monday"
    PublicHolidays = "https://schema.org/PublicHolidays"
    Saturday = "https://schema.org/Saturday"
    Sunday = "https://schema.org/Sunday"
    Thursday = "https://schema.org/Thursday"
    Tuesday = "https://schema.org/Tuesday"
    Wednesday = "https://schema.org/Wednesday"


class DeliveryMethod(SchemaEnumeration):
    """A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer.

    https://schema.org/DeliveryMethod
    """

    LockerDelivery = "https://schema.org/LockerDelivery"
    OnSitePickup = "https://schema.org/OnSitePickup"
    ParcelService = "https://schema.org/ParcelService"


class DigitalDocumentPermissionType(SchemaEnumeration):
    """A type of permission which can be granted for accessing a digital document.

    https://schema.org/DigitalDocumentPermissionType
    """

    CommentPermission = "https://schema.org/CommentPermission"
    ReadPermission = "https://schema.org/ReadPermission"
    WritePermission = "https://schema.org/WritePermission"


class DigitalPlatformEnumeration(SchemaEnumeration):
    """Enumerates some common technology platforms, for use with properties such as actionPlatform.

    https://schema.org/DigitalPlatformEnumeration
    """

    AndroidPlatform = "https://schema.org/AndroidPlatform"
    DesktopWebPlatform = "https://schema.org/DesktopWebPlatform"
    GenericWebPlatform = "https://schema.org/GenericWebPlatform"
    IOSPlatform = "https://schema.org/IOSPlatform"
    MobileWebPlatform = "https://schema.org/MobileWebPlatform"


class DriveWheelConfigurationValue(SchemaEnumeration):
    """A value indicating which roadwheels will receive torque.

    https://schema.org/DriveWheelConfigurationValue
    """

    AllWheelDriveConfiguration = "https://schema.org/AllWheelDriveConfiguration"
    FourWheelDriveConfiguration = "https://schema.org/FourWheelDriveConfiguration"
    FrontWheelDriveConfiguration = "https://schema.org/FrontWheelDriveConfiguration"
    RearWheelDriveConfiguration = "https://schema.org/RearWheelDriveConfiguration"


class DrugCostCategory(SchemaEnumeration):
    """Enumerated categories of medical drug costs.

    https://schema.org/DrugCostCategory
    """

    ReimbursementCap = "https://schema.org/ReimbursementCap"
    Retail = "https://schema.org/Retail"
    Wholesale = "https://schema.org/Wholesale"


class DrugPregnancyCategory(SchemaEnumeration):
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.

    https://schema.org/DrugPregnancyCategory
    """

    FDAcategoryA = "https://schema.org/FDAcategoryA"
    FDAcategoryB = "https://schema.org/FDAcategoryB"
    FDAcategoryC = "https://schema.org/FDAcategoryC"
    FDAcategoryD = "https://schema.org/FDAcategoryD"
    FDAcategoryX = "https://schema.org/FDAcategoryX"
    FDAnotEvaluated = "https://schema.org/FDAnotEvaluated"


class DrugPrescriptionStatus(SchemaEnumeration):
    """Indicates whether this drug is available by prescription or over-the-counter.

    https://schema.org/DrugPrescriptionStatus
    """

    OTC = "https://schema.org/OTC"
    PrescriptionOnly = "https://schema.org/PrescriptionOnly"


class EUEnergyEfficiencyEnumeration(SchemaEnumeration):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.

    https://schema.org/EUEnergyEfficiencyEnumeration
    """

    EUEnergyEfficiencyCategoryA = "https://schema.org/EUEnergyEfficiencyCategoryA"
    EUEnergyEfficiencyCategoryA1Plus = "https://schema.org/EUEnergyEfficiencyCategoryA1Plus"
    EUEnergyEfficiencyCategoryA2Plus = "https://schema.org/EUEnergyEfficiencyCategoryA2Plus"
    EUEnergyEfficiencyCategoryA3Plus = "https://schema.org/EUEnergyEfficiencyCategoryA3Plus"
    EUEnergyEfficiencyCategoryB = "https://schema.org/EUEnergyEfficiencyCategoryB"
    EUEnergyEfficiencyCategoryC = "https://schema.org/EUEnergyEfficiencyCategoryC"
    EUEnergyEfficiencyCategoryD = "https://schema.org/EUEnergyEfficiencyCategoryD"
    EUEnergyEfficiencyCategoryE = "https://schema.org/EUEnergyEfficiencyCategoryE"
    EUEnergyEfficiencyCategoryF = "https://schema.org/EUEnergyEfficiencyCategoryF"
    EUEnergyEfficiencyCategoryG = "https://schema.org/EUEnergyEfficiencyCategoryG"


class EnergyStarEnergyEfficiencyEnumeration(SchemaEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    """

    EnergyStarCertified = "https://schema.org/EnergyStarCertified"


class EventAttendanceModeEnumeration(SchemaEnumeration):
    """An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.

    https://schema.org/EventAttendanceModeEnumeration
    """

    MixedEventAttendanceMode = "https://schema.org/MixedEventAttendanceMode"
    OfflineEventAttendanceMode = "https://schema.org/OfflineEventAttendanceMode"
    OnlineEventAttendanceMode = "https://schema.org/OnlineEventAttendanceMode"


class EventStatusType(SchemaEnumeration):
    """EventStatusType is an enumeration type whose instances represent several states that an Event may be in.

    https://schema.org/EventStatusType
    """

    EventCancelled = "https://schema.org/EventCancelled"
    EventMovedOnline = "https://schema.org/EventMovedOnline"
    EventPostponed = "https://schema.org/EventPostponed"
    EventRescheduled = "https://schema.org/EventRescheduled"
    EventScheduled = "https://schema.org/EventScheduled"


class FulfillmentTypeEnumeration(SchemaEnumeration):
    """A type of product fulfillment.

    https://schema.org/FulfillmentTypeEnumeration
    """

    FulfillmentTypeCollectionPoint = "https://schema.org/FulfillmentTypeCollectionPoint"
    FulfillmentTypeDelivery = "https://schema.org/FulfillmentTypeDelivery"
    FulfillmentTypePickupDropoff = "https://schema.org/FulfillmentTypePickupDropoff"
    FulfillmentTypePickupInStore = "https://schema.org/FulfillmentTypePickupInStore"
    FulfillmentTypeScheduledDelivery = "https://schema.org/FulfillmentTypeScheduledDelivery"


class GameAvailabilityEnumeration(SchemaEnumeration):
    """For a VideoGame, such as used with a PlayGameAction, an enumeration of the kind of game availability offered.

    https://schema.org/GameAvailabilityEnumeration
    """

    DemoGameAvailability = "https://schema.org/DemoGameAvailability"
    FullGameAvailability = "https://schema.org/FullGameAvailability"


class GamePlayMode(SchemaEnumeration):
    """Indicates whether this game is multi-player, co-op or single-player.

    https://schema.org/GamePlayMode
    """

    CoOp = "https://schema.org/CoOp"
    MultiPlayer = "https://schema.org/MultiPlayer"
    SinglePlayer = "https://schema.org/SinglePlayer"


class GameServerStatus(SchemaEnumeration):
    """Status of a game server.

    https://schema.org/GameServerStatus
    """

    OfflinePermanently = "https://schema.org/OfflinePermanently"
    OfflineTemporarily = "https://schema.org/OfflineTemporarily"
    Online = "https://schema.org/Online"
    OnlineFull = "https://schema.org/OnlineFull"


class GenderType(SchemaEnumeration):
    """An enumeration of genders.

    https://schema.org/GenderType
    """

    Female = "https://schema.org/Female"
    Male = "https://schema.org/Male"


class GovernmentBenefitsType(SchemaEnumeration):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation.

    https://schema.org/GovernmentBenefitsType
    """

    BasicIncome = "https://schema.org/BasicIncome"
    BusinessSupport = "https://schema.org/BusinessSupport"
    DisabilitySupport = "https://schema.org/DisabilitySupport"
    HealthCare = "https://schema.org/HealthCare"
    OneTimePayments = "https://schema.org/OneTimePayments"
    PaidLeave = "https://schema.org/PaidLeave"
    ParentalSupport = "https://schema.org/ParentalSupport"
    UnemploymentSupport = "https://schema.org/UnemploymentSupport"


class HealthAspectEnumeration(SchemaEnumeration):
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using hasHealthAspect and HealthTopicContent.

    https://schema.org/HealthAspectEnumeration
    """

    AllergiesHealthAspect = "https://schema.org/AllergiesHealthAspect"
    BenefitsHealthAspect = "https://schema.org/BenefitsHealthAspect"
    CausesHealthAspect = "https://schema.org/CausesHealthAspect"
    ContagiousnessHealthAspect = "https://schema.org/ContagiousnessHealthAspect"
    EffectivenessHealthAspect = "https://schema.org/EffectivenessHealthAspect"
    GettingAccessHealthAspect = "https://schema.org/GettingAccessHealthAspect"
    HowItWorksHealthAspect = "https://schema.org/HowItWorksHealthAspect"
    HowOrWhereHealthAspect = "https://schema.org/HowOrWhereHealthAspect"
    IngredientsHealthAspect = "https://schema.org/IngredientsHealthAspect"
    LivingWithHealthAspect = "https://schema.org/LivingWithHealthAspect"
    MayTreatHealthAspect = "https://schema.org/MayTreatHealthAspect"
    MisconceptionsHealthAspect = "https://schema.org/MisconceptionsHealthAspect"
    OverviewHealthAspect = "https://schema.org/OverviewHealthAspect"
    PatientExperienceHealthAspect = "https://schema.org/PatientExperienceHealthAspect"
    PregnancyHealthAspect = "https://schema.org/PregnancyHealthAspect"
    PreventionHealthAspect = "https://schema.org/PreventionHealthAspect"
    PrognosisHealthAspect = "https://schema.org/PrognosisHealthAspect"
    RelatedTopicsHealthAspect = "https://schema.org/RelatedTopicsHealthAspect"
    RisksOrComplicationsHealthAspect = "https://schema.org/RisksOrComplicationsHealthAspect"
    SafetyHealthAspect = "https://schema.org/SafetyHealthAspect"
    ScreeningHealthAspect = "https://schema.org/ScreeningHealthAspect"
    SeeDoctorHealthAspect = "https://schema.org/SeeDoctorHealthAspect"
    SelfCareHealthAspect = "https://schema.org/SelfCareHealthAspect"
    SideEffectsHealthAspect = "https://schema.org/SideEffectsHealthAspect"
    StagesHealthAspect = "https://schema.org/StagesHealthAspect"
    SymptomsHealthAspect = "https://schema.org/SymptomsHealthAspect"
    TreatmentsHealthAspect = "https://schema.org/TreatmentsHealthAspect"
    TypesHealthAspect = "https://schema.org/TypesHealthAspect"
    UsageOrScheduleHealthAspect = "https://schema.org/UsageOrScheduleHealthAspect"


class IPTCDigitalSourceEnumeration(SchemaEnumeration):
    """IPTC "Digital Source" codes for use with the digitalSourceType property, providing information about the source for a digital media object.

    https://schema.org/IPTCDigitalSourceEnumeration
    """

    AlgorithmicMediaDigitalSource = "https://schema.org/AlgorithmicMediaDigitalSource"
    AlgorithmicallyEnhancedDigitalSource = "https://schema.org/AlgorithmicallyEnhancedDigitalSource"
    CompositeCaptureDigitalSource = "https://schema.org/CompositeCaptureDigitalSource"
    CompositeDigitalSource = "https://schema.org/CompositeDigitalSource"
    CompositeSyntheticDigitalSource = "https://schema.org/CompositeSyntheticDigitalSource"
    CompositeWithTrainedAlgorithmicMediaDigitalSource = (
        "https://schema.org/CompositeWithTrainedAlgorithmicMediaDigitalSource"
    )
    DataDrivenMediaDigitalSource = "https://schema.org/DataDrivenMediaDigitalSource"
    DigitalArtDigitalSource = "https://schema.org/DigitalArtDigitalSource"
    DigitalCaptureDigitalSource = "https://schema.org/DigitalCaptureDigitalSource"
    MinorHumanEditsDigitalSource = "https://schema.org/MinorHumanEditsDigitalSource"
    MultiFrameComputationalCaptureDigitalSource = (
        "https://schema.org/MultiFrameComputationalCaptureDigitalSource"
    )
    NegativeFilmDigitalSource = "https://schema.org/NegativeFilmDigitalSource"
    PositiveFilmDigitalSource = "https://schema.org/PositiveFilmDigitalSource"
    PrintDigitalSource = "https://schema.org/PrintDigitalSource"
    ScreenCaptureDigitalSource = "https://schema.org/ScreenCaptureDigitalSource"
    TrainedAlgorithmicMediaDigitalSource = "https://schema.org/TrainedAlgorithmicMediaDigitalSource"
    VirtualRecordingDigitalSource = "https://schema.org/VirtualRecordingDigitalSource"


class IncentiveQualifiedExpenseType(SchemaEnumeration):
    """The types of expenses that are covered by the incentive.

    https://schema.org/IncentiveQualifiedExpenseType
    """

    IncentiveQualifiedExpenseTypeGoodsOnly = (
        "https://schema.org/IncentiveQualifiedExpenseTypeGoodsOnly"
    )
    IncentiveQualifiedExpenseTypeGoodsOrServices = (
        "https://schema.org/IncentiveQualifiedExpenseTypeGoodsOrServices"
    )
    IncentiveQualifiedExpenseTypeServicesOnly = (
        "https://schema.org/IncentiveQualifiedExpenseTypeServicesOnly"
    )
    IncentiveQualifiedExpenseTypeUtilityBill = (
        "https://schema.org/IncentiveQualifiedExpenseTypeUtilityBill"
    )


class IncentiveStatus(SchemaEnumeration):
    """Enumerates a status for an incentive, such as whether it is active.

    https://schema.org/IncentiveStatus
    """

    IncentiveStatusActive = "https://schema.org/IncentiveStatusActive"
    IncentiveStatusInDevelopment = "https://schema.org/IncentiveStatusInDevelopment"
    IncentiveStatusOnHold = "https://schema.org/IncentiveStatusOnHold"
    IncentiveStatusRetired = "https://schema.org/IncentiveStatusRetired"


class IncentiveType(SchemaEnumeration):
    """Enumerates common financial incentives for products, including tax credits, tax deductions, rebates and subsidies, etc.

    https://schema.org/IncentiveType
    """

    IncentiveTypeLoan = "https://schema.org/IncentiveTypeLoan"
    IncentiveTypeRebateOrSubsidy = "https://schema.org/IncentiveTypeRebateOrSubsidy"
    IncentiveTypeTaxCredit = "https://schema.org/IncentiveTypeTaxCredit"
    IncentiveTypeTaxDeduction = "https://schema.org/IncentiveTypeTaxDeduction"
    IncentiveTypeTaxWaiver = "https://schema.org/IncentiveTypeTaxWaiver"


class InfectiousAgentClass(SchemaEnumeration):
    """Classes of agents or pathogens that transmit infectious diseases.

    https://schema.org/InfectiousAgentClass
    """

    Bacteria = "https://schema.org/Bacteria"
    Fungus = "https://schema.org/Fungus"
    MulticellularParasite = "https://schema.org/MulticellularParasite"
    Prion = "https://schema.org/Prion"
    Protozoa = "https://schema.org/Protozoa"
    Virus = "https://schema.org/Virus"


class ItemAvailability(SchemaEnumeration):
    """A list of possible product availability options.

    https://schema.org/ItemAvailability
    """

    BackOrder = "https://schema.org/BackOrder"
    Discontinued = "https://schema.org/Discontinued"
    InStock = "https://schema.org/InStock"
    InStoreOnly = "https://schema.org/InStoreOnly"
    LimitedAvailability = "https://schema.org/LimitedAvailability"
    MadeToOrder = "https://schema.org/MadeToOrder"
    OnlineOnly = "https://schema.org/OnlineOnly"
    OutOfStock = "https://schema.org/OutOfStock"
    PreOrder = "https://schema.org/PreOrder"
    PreSale = "https://schema.org/PreSale"
    Reserved = "https://schema.org/Reserved"
    SoldOut = "https://schema.org/SoldOut"


class ItemListOrderType(SchemaEnumeration):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    https://schema.org/ItemListOrderType
    """

    ItemListOrderAscending = "https://schema.org/ItemListOrderAscending"
    ItemListOrderDescending = "https://schema.org/ItemListOrderDescending"
    ItemListUnordered = "https://schema.org/ItemListUnordered"


class LegalForceStatus(SchemaEnumeration):
    """A list of possible statuses for the legal force of a legislation.

    https://schema.org/LegalForceStatus
    """

    InForce = "https://schema.org/InForce"
    NotInForce = "https://schema.org/NotInForce"
    PartiallyInForce = "https://schema.org/PartiallyInForce"


class LegalValueLevel(SchemaEnumeration):
    """A list of possible levels for the legal validity of a legislation.

    https://schema.org/LegalValueLevel
    """

    AuthoritativeLegalValue = "https://schema.org/AuthoritativeLegalValue"
    DefinitiveLegalValue = "https://schema.org/DefinitiveLegalValue"
    OfficialLegalValue = "https://schema.org/OfficialLegalValue"
    UnofficialLegalValue = "https://schema.org/UnofficialLegalValue"


class MapCategoryType(SchemaEnumeration):
    """An enumeration of several kinds of Map.

    https://schema.org/MapCategoryType
    """

    ParkingMap = "https://schema.org/ParkingMap"
    SeatingMap = "https://schema.org/SeatingMap"
    TransitMap = "https://schema.org/TransitMap"
    VenueMap = "https://schema.org/VenueMap"


class MeasurementMethodEnum(SchemaEnumeration):
    """Enumeration(s) for use with measurementMethod.

    https://schema.org/MeasurementMethodEnum
    """

    ExampleMeasurementMethodEnum = "https://schema.org/ExampleMeasurementMethodEnum"


class MediaManipulationRatingEnumeration(SchemaEnumeration):
    """Codes for use with the mediaAuthenticityCategory property, indicating the authenticity of a media object (in the context of how it was published or shared).

    https://schema.org/MediaManipulationRatingEnumeration
    """

    DecontextualizedContent = "https://schema.org/DecontextualizedContent"
    EditedOrCroppedContent = "https://schema.org/EditedOrCroppedContent"
    OriginalMediaContent = "https://schema.org/OriginalMediaContent"
    SatireOrParodyContent = "https://schema.org/SatireOrParodyContent"
    StagedContent = "https://schema.org/StagedContent"
    TransformedContent = "https://schema.org/TransformedContent"


class MedicalAudienceType(SchemaEnumeration):
    """Target audiences types for medical web pages.

    https://schema.org/MedicalAudienceType
    """

    Clinician = "https://schema.org/Clinician"
    MedicalResearcher = "https://schema.org/MedicalResearcher"


class MedicalDevicePurpose(SchemaEnumeration):
    """Categories of medical devices, organized by the purpose or intended use of the device.

    https://schema.org/MedicalDevicePurpose
    """

    Diagnostic = "https://schema.org/Diagnostic"
    Therapeutic = "https://schema.org/Therapeutic"


class MedicalEvidenceLevel(SchemaEnumeration):
    """Level of evidence for a medical guideline.

    https://schema.org/MedicalEvidenceLevel
    """

    EvidenceLevelA = "https://schema.org/EvidenceLevelA"
    EvidenceLevelB = "https://schema.org/EvidenceLevelB"
    EvidenceLevelC = "https://schema.org/EvidenceLevelC"


class MedicalImagingTechnique(SchemaEnumeration):
    """Any medical imaging modality typically used for diagnostic purposes.

    https://schema.org/MedicalImagingTechnique
    """

    CT = "https://schema.org/CT"
    MRI = "https://schema.org/MRI"
    PET = "https://schema.org/PET"
    Radiography = "https://schema.org/Radiography"
    Ultrasound = "https://schema.org/Ultrasound"
    XRay = "https://schema.org/XRay"


class MedicalObservationalStudyDesign(SchemaEnumeration):
    """Design models for observational medical studies.

    https://schema.org/MedicalObservationalStudyDesign
    """

    CaseSeries = "https://schema.org/CaseSeries"
    CohortStudy = "https://schema.org/CohortStudy"
    CrossSectional = "https://schema.org/CrossSectional"
    Longitudinal = "https://schema.org/Longitudinal"
    Observational = "https://schema.org/Observational"
    Registry = "https://schema.org/Registry"


class MedicalProcedureType(SchemaEnumeration):
    """An enumeration that describes different types of medical procedures.

    https://schema.org/MedicalProcedureType
    """

    NoninvasiveProcedure = "https://schema.org/NoninvasiveProcedure"
    PercutaneousProcedure = "https://schema.org/PercutaneousProcedure"


class MedicalSpecialty(SchemaEnumeration):
    """Any specific branch of medical science or practice.

    https://schema.org/MedicalSpecialty
    """

    Anesthesia = "https://schema.org/Anesthesia"
    Audiology = "https://schema.org/Audiology"
    Cardiovascular = "https://schema.org/Cardiovascular"
    CommunityHealth = "https://schema.org/CommunityHealth"
    Dentistry = "https://schema.org/Dentistry"
    Dermatologic = "https://schema.org/Dermatologic"
    Dermatology = "https://schema.org/Dermatology"
    DietNutrition = "https://schema.org/DietNutrition"
    Emergency = "https://schema.org/Emergency"
    Endocrine = "https://schema.org/Endocrine"
    Gastroenterologic = "https://schema.org/Gastroenterologic"
    Genetic = "https://schema.org/Genetic"
    Geriatric = "https://schema.org/Geriatric"
    Gynecologic = "https://schema.org/Gynecologic"
    Hematologic = "https://schema.org/Hematologic"
    Infectious = "https://schema.org/Infectious"
    LaboratoryScience = "https://schema.org/LaboratoryScience"
    Midwifery = "https://schema.org/Midwifery"
    Musculoskeletal = "https://schema.org/Musculoskeletal"
    Neurologic = "https://schema.org/Neurologic"
    Nursing = "https://schema.org/Nursing"
    Obstetric = "https://schema.org/Obstetric"
    Oncologic = "https://schema.org/Oncologic"
    Ophthalmology = "https://schema.org/Ophthalmology"
    Optometric = "https://schema.org/Optometric"
    Otolaryngologic = "https://schema.org/Otolaryngologic"
    Pathology = "https://schema.org/Pathology"
    Pediatric = "https://schema.org/Pediatric"
    PharmacySpecialty = "https://schema.org/PharmacySpecialty"
    Physiotherapy = "https://schema.org/Physiotherapy"
    PlasticSurgery = "https://schema.org/PlasticSurgery"
    Podiatric = "https://schema.org/Podiatric"
    PrimaryCare = "https://schema.org/PrimaryCare"
    Psychiatric = "https://schema.org/Psychiatric"
    PublicHealth = "https://schema.org/PublicHealth"
    Pulmonary = "https://schema.org/Pulmonary"
    Radiography = "https://schema.org/Radiography"
    Renal = "https://schema.org/Renal"
    RespiratoryTherapy = "https://schema.org/RespiratoryTherapy"
    Rheumatologic = "https://schema.org/Rheumatologic"
    SpeechPathology = "https://schema.org/SpeechPathology"
    Surgical = "https://schema.org/Surgical"
    Toxicologic = "https://schema.org/Toxicologic"
    Urologic = "https://schema.org/Urologic"


class MedicalStudyStatus(SchemaEnumeration):
    """The status of a medical study.

    https://schema.org/MedicalStudyStatus
    """

    ActiveNotRecruiting = "https://schema.org/ActiveNotRecruiting"
    Completed = "https://schema.org/Completed"
    EnrollingByInvitation = "https://schema.org/EnrollingByInvitation"
    NotYetRecruiting = "https://schema.org/NotYetRecruiting"
    Recruiting = "https://schema.org/Recruiting"
    ResultsAvailable = "https://schema.org/ResultsAvailable"
    ResultsNotAvailable = "https://schema.org/ResultsNotAvailable"
    Suspended = "https://schema.org/Suspended"
    Terminated = "https://schema.org/Terminated"
    Withdrawn = "https://schema.org/Withdrawn"


class MedicalTrialDesign(SchemaEnumeration):
    """Design models for medical trials.

    https://schema.org/MedicalTrialDesign
    """

    DoubleBlindedTrial = "https://schema.org/DoubleBlindedTrial"
    InternationalTrial = "https://schema.org/InternationalTrial"
    MultiCenterTrial = "https://schema.org/MultiCenterTrial"
    OpenTrial = "https://schema.org/OpenTrial"
    PlaceboControlledTrial = "https://schema.org/PlaceboControlledTrial"
    RandomizedTrial = "https://schema.org/RandomizedTrial"
    SingleBlindedTrial = "https://schema.org/SingleBlindedTrial"
    SingleCenterTrial = "https://schema.org/SingleCenterTrial"
    TripleBlindedTrial = "https://schema.org/TripleBlindedTrial"


class MedicineSystem(SchemaEnumeration):
    """Systems of medical practice.

    https://schema.org/MedicineSystem
    """

    Ayurvedic = "https://schema.org/Ayurvedic"
    Chiropractic = "https://schema.org/Chiropractic"
    Homeopathic = "https://schema.org/Homeopathic"
    Osteopathic = "https://schema.org/Osteopathic"
    TraditionalChinese = "https://schema.org/TraditionalChinese"
    WesternConventional = "https://schema.org/WesternConventional"


class MerchantReturnEnumeration(SchemaEnumeration):
    """Enumerates several kinds of product return policies.

    https://schema.org/MerchantReturnEnumeration
    """

    MerchantReturnFiniteReturnWindow = "https://schema.org/MerchantReturnFiniteReturnWindow"
    MerchantReturnNotPermitted = "https://schema.org/MerchantReturnNotPermitted"
    MerchantReturnUnlimitedWindow = "https://schema.org/MerchantReturnUnlimitedWindow"
    MerchantReturnUnspecified = "https://schema.org/MerchantReturnUnspecified"


class MusicAlbumProductionType(SchemaEnumeration):
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc.

    https://schema.org/MusicAlbumProductionType
    """

    CompilationAlbum = "https://schema.org/CompilationAlbum"
    DJMixAlbum = "https://schema.org/DJMixAlbum"
    DemoAlbum = "https://schema.org/DemoAlbum"
    LiveAlbum = "https://schema.org/LiveAlbum"
    MixtapeAlbum = "https://schema.org/MixtapeAlbum"
    RemixAlbum = "https://schema.org/RemixAlbum"
    SoundtrackAlbum = "https://schema.org/SoundtrackAlbum"
    SpokenWordAlbum = "https://schema.org/SpokenWordAlbum"
    StudioAlbum = "https://schema.org/StudioAlbum"


class MusicAlbumReleaseType(SchemaEnumeration):
    """The kind of release which this album is: single, EP or album.

    https://schema.org/MusicAlbumReleaseType
    """

    AlbumRelease = "https://schema.org/AlbumRelease"
    BroadcastRelease = "https://schema.org/BroadcastRelease"
    EPRelease = "https://schema.org/EPRelease"
    SingleRelease = "https://schema.org/SingleRelease"


class MusicReleaseFormatType(SchemaEnumeration):
    """Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).

    https://schema.org/MusicReleaseFormatType
    """

    CDFormat = "https://schema.org/CDFormat"
    CassetteFormat = "https://schema.org/CassetteFormat"
    DVDFormat = "https://schema.org/DVDFormat"
    DigitalAudioTapeFormat = "https://schema.org/DigitalAudioTapeFormat"
    DigitalFormat = "https://schema.org/DigitalFormat"
    LaserDiscFormat = "https://schema.org/LaserDiscFormat"
    VinylFormat = "https://schema.org/VinylFormat"


class NLNonprofitType(SchemaEnumeration):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    https://schema.org/NLNonprofitType
    """

    NonprofitANBI = "https://schema.org/NonprofitANBI"
    NonprofitSBBI = "https://schema.org/NonprofitSBBI"


class OfferItemCondition(SchemaEnumeration):
    """A list of possible conditions for the item.

    https://schema.org/OfferItemCondition
    """

    DamagedCondition = "https://schema.org/DamagedCondition"
    NewCondition = "https://schema.org/NewCondition"
    RefurbishedCondition = "https://schema.org/RefurbishedCondition"
    UsedCondition = "https://schema.org/UsedCondition"


class OrderStatus(SchemaEnumeration):
    """Enumerated status values for Order.

    https://schema.org/OrderStatus
    """

    OrderCancelled = "https://schema.org/OrderCancelled"
    OrderDelivered = "https://schema.org/OrderDelivered"
    OrderInTransit = "https://schema.org/OrderInTransit"
    OrderPaymentDue = "https://schema.org/OrderPaymentDue"
    OrderPickupAvailable = "https://schema.org/OrderPickupAvailable"
    OrderProblem = "https://schema.org/OrderProblem"
    OrderProcessing = "https://schema.org/OrderProcessing"
    OrderReturned = "https://schema.org/OrderReturned"


class PaymentMethodType(SchemaEnumeration):
    """The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.

    https://schema.org/PaymentMethodType
    """

    ByBankTransferInAdvance = "https://schema.org/ByBankTransferInAdvance"
    ByInvoice = "https://schema.org/ByInvoice"
    COD = "https://schema.org/COD"
    Cash = "https://schema.org/Cash"
    CheckInAdvance = "https://schema.org/CheckInAdvance"
    DirectDebit = "https://schema.org/DirectDebit"
    InStorePrepay = "https://schema.org/InStorePrepay"
    PhoneCarrierPayment = "https://schema.org/PhoneCarrierPayment"


class PaymentStatusType(SchemaEnumeration):
    """A specific payment status.

    https://schema.org/PaymentStatusType
    """

    PaymentAutomaticallyApplied = "https://schema.org/PaymentAutomaticallyApplied"
    PaymentComplete = "https://schema.org/PaymentComplete"
    PaymentDeclined = "https://schema.org/PaymentDeclined"
    PaymentDue = "https://schema.org/PaymentDue"
    PaymentPastDue = "https://schema.org/PaymentPastDue"


class PhysicalActivityCategory(SchemaEnumeration):
    """Categories of physical activity, organized by physiologic classification.

    https://schema.org/PhysicalActivityCategory
    """

    AerobicActivity = "https://schema.org/AerobicActivity"
    AnaerobicActivity = "https://schema.org/AnaerobicActivity"
    Balance = "https://schema.org/Balance"
    Flexibility = "https://schema.org/Flexibility"
    LeisureTimeActivity = "https://schema.org/LeisureTimeActivity"
    OccupationalActivity = "https://schema.org/OccupationalActivity"
    StrengthTraining = "https://schema.org/StrengthTraining"


class PhysicalExam(SchemaEnumeration):
    """A type of physical examination of a patient performed by a physician.

    https://schema.org/PhysicalExam
    """

    Abdomen = "https://schema.org/Abdomen"
    Appearance = "https://schema.org/Appearance"
    CardiovascularExam = "https://schema.org/CardiovascularExam"
    Ear = "https://schema.org/Ear"
    Eye = "https://schema.org/Eye"
    Genitourinary = "https://schema.org/Genitourinary"
    Head = "https://schema.org/Head"
    Lung = "https://schema.org/Lung"
    MusculoskeletalExam = "https://schema.org/MusculoskeletalExam"
    Neck = "https://schema.org/Neck"
    Neuro = "https://schema.org/Neuro"
    Nose = "https://schema.org/Nose"
    Skin = "https://schema.org/Skin"
    Throat = "https://schema.org/Throat"


class PriceComponentTypeEnumeration(SchemaEnumeration):
    """Enumerates different price components that together make up the total price for an offered product.

    https://schema.org/PriceComponentTypeEnumeration
    """

    ActivationFee = "https://schema.org/ActivationFee"
    CleaningFee = "https://schema.org/CleaningFee"
    DistanceFee = "https://schema.org/DistanceFee"
    Downpayment = "https://schema.org/Downpayment"
    Installment = "https://schema.org/Installment"
    Subscription = "https://schema.org/Subscription"


class PriceTypeEnumeration(SchemaEnumeration):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    https://schema.org/PriceTypeEnumeration
    """

    InvoicePrice = "https://schema.org/InvoicePrice"
    ListPrice = "https://schema.org/ListPrice"
    MSRP = "https://schema.org/MSRP"
    MinimumAdvertisedPrice = "https://schema.org/MinimumAdvertisedPrice"
    RegularPrice = "https://schema.org/RegularPrice"
    SRP = "https://schema.org/SRP"
    SalePrice = "https://schema.org/SalePrice"
    StrikethroughPrice = "https://schema.org/StrikethroughPrice"


class ProductReturnEnumeration(SchemaEnumeration):
    """ProductReturnEnumeration enumerates several kinds of product return policy.

    https://schema.org/ProductReturnEnumeration

    Deprecated: superseded by MerchantReturnEnumeration.
    """

    ProductReturnFiniteReturnWindow = "https://schema.org/ProductReturnFiniteReturnWindow"
    ProductReturnNotPermitted = "https://schema.org/ProductReturnNotPermitted"
    ProductReturnUnlimitedWindow = "https://schema.org/ProductReturnUnlimitedWindow"
    ProductReturnUnspecified = "https://schema.org/ProductReturnUnspecified"


class PurchaseType(SchemaEnumeration):
    """Enumerates a purchase type for an item.

    https://schema.org/PurchaseType
    """

    PurchaseTypeLease = "https://schema.org/PurchaseTypeLease"
    PurchaseTypeNewPurchase = "https://schema.org/PurchaseTypeNewPurchase"
    PurchaseTypeTradeIn = "https://schema.org/PurchaseTypeTradeIn"
    PurchaseTypeUsedPurchase = "https://schema.org/PurchaseTypeUsedPurchase"


class RefundTypeEnumeration(SchemaEnumeration):
    """Enumerates several kinds of product return refund types.

    https://schema.org/RefundTypeEnumeration
    """

    ExchangeRefund = "https://schema.org/ExchangeRefund"
    FullRefund = "https://schema.org/FullRefund"
    StoreCreditRefund = "https://schema.org/StoreCreditRefund"


class ReservationStatusType(SchemaEnumeration):
    """Enumerated status values for Reservation.

    https://schema.org/ReservationStatusType
    """

    ReservationCancelled = "https://schema.org/ReservationCancelled"
    ReservationConfirmed = "https://schema.org/ReservationConfirmed"
    ReservationHold = "https://schema.org/ReservationHold"
    ReservationPending = "https://schema.org/ReservationPending"


class RestrictedDiet(SchemaEnumeration):
    """A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.

    https://schema.org/RestrictedDiet
    """

    DiabeticDiet = "https://schema.org/DiabeticDiet"
    GlutenFreeDiet = "https://schema.org/GlutenFreeDiet"
    HalalDiet = "https://schema.org/HalalDiet"
    HinduDiet = "https://schema.org/HinduDiet"
    KosherDiet = "https://schema.org/KosherDiet"
    LowCalorieDiet = "https://schema.org/LowCalorieDiet"
    LowFatDiet = "https://schema.org/LowFatDiet"
    LowLactoseDiet = "https://schema.org/LowLactoseDiet"
    LowSaltDiet = "https://schema.org/LowSaltDiet"
    VeganDiet = "https://schema.org/VeganDiet"
    VegetarianDiet = "https://schema.org/VegetarianDiet"


class ReturnFeesEnumeration(SchemaEnumeration):
    """Enumerates several kinds of policies for product return fees.

    https://schema.org/ReturnFeesEnumeration
    """

    FreeReturn = "https://schema.org/FreeReturn"
    OriginalShippingFees = "https://schema.org/OriginalShippingFees"
    RestockingFees = "https://schema.org/RestockingFees"
    ReturnFeesCustomerResponsibility = "https://schema.org/ReturnFeesCustomerResponsibility"
    ReturnShippingFees = "https://schema.org/ReturnShippingFees"


class ReturnLabelSourceEnumeration(SchemaEnumeration):
    """Enumerates several types of return labels for product returns.

    https://schema.org/ReturnLabelSourceEnumeration
    """

    ReturnLabelCustomerResponsibility = "https://schema.org/ReturnLabelCustomerResponsibility"
    ReturnLabelDownloadAndPrint = "https://schema.org/ReturnLabelDownloadAndPrint"
    ReturnLabelInBox = "https://schema.org/ReturnLabelInBox"


class ReturnMethodEnumeration(SchemaEnumeration):
    """Enumerates several types of product return methods.

    https://schema.org/ReturnMethodEnumeration
    """

    KeepProduct = "https://schema.org/KeepProduct"
    ReturnAtKiosk = "https://schema.org/ReturnAtKiosk"
    ReturnByMail = "https://schema.org/ReturnByMail"
    ReturnInStore = "https://schema.org/ReturnInStore"


class RsvpResponseType(SchemaEnumeration):
    """RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.

    https://schema.org/RsvpResponseType
    """

    RsvpResponseMaybe = "https://schema.org/RsvpResponseMaybe"
    RsvpResponseNo = "https://schema.org/RsvpResponseNo"
    RsvpResponseYes = "https://schema.org/RsvpResponseYes"


class SizeSystemEnumeration(SchemaEnumeration):
    """Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.

    https://schema.org/SizeSystemEnumeration
    """

    SizeSystemImperial = "https://schema.org/SizeSystemImperial"
    SizeSystemMetric = "https://schema.org/SizeSystemMetric"


class SteeringPositionValue(SchemaEnumeration):
    """A value indicating a steering position.

    https://schema.org/SteeringPositionValue
    """

    LeftHandDriving = "https://schema.org/LeftHandDriving"
    RightHandDriving = "https://schema.org/RightHandDriving"


class TierBenefitEnumeration(SchemaEnumeration):
    """An enumeration of possible benefits as part of a loyalty (members) program.

    https://schema.org/TierBenefitEnumeration
    """

    TierBenefitLoyaltyPoints = "https://schema.org/TierBenefitLoyaltyPoints"
    TierBenefitLoyaltyPrice = "https://schema.org/TierBenefitLoyaltyPrice"
    TierBenefitLoyaltyReturns = "https://schema.org/TierBenefitLoyaltyReturns"
    TierBenefitLoyaltyShipping = "https://schema.org/TierBenefitLoyaltyShipping"


class UKNonprofitType(SchemaEnumeration):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    https://schema.org/UKNonprofitType
    """

    CharitableIncorporatedOrganization = "https://schema.org/CharitableIncorporatedOrganization"
    LimitedByGuaranteeCharity = "https://schema.org/LimitedByGuaranteeCharity"
    UKTrust = "https://schema.org/UKTrust"
    UnincorporatedAssociationCharity = "https://schema.org/UnincorporatedAssociationCharity"


class USNonprofitType(SchemaEnumeration):
    """USNonprofitType: Non-profit organization type originating from the United States.

    https://schema.org/USNonprofitType
    """

    Nonprofit501a = "https://schema.org/Nonprofit501a"
    Nonprofit501c1 = "https://schema.org/Nonprofit501c1"
    Nonprofit501c10 = "https://schema.org/Nonprofit501c10"
    Nonprofit501c11 = "https://schema.org/Nonprofit501c11"
    Nonprofit501c12 = "https://schema.org/Nonprofit501c12"
    Nonprofit501c13 = "https://schema.org/Nonprofit501c13"
    Nonprofit501c14 = "https://schema.org/Nonprofit501c14"
    Nonprofit501c15 = "https://schema.org/Nonprofit501c15"
    Nonprofit501c16 = "https://schema.org/Nonprofit501c16"
    Nonprofit501c17 = "https://schema.org/Nonprofit501c17"
    Nonprofit501c18 = "https://schema.org/Nonprofit501c18"
    Nonprofit501c19 = "https://schema.org/Nonprofit501c19"
    Nonprofit501c2 = "https://schema.org/Nonprofit501c2"
    Nonprofit501c20 = "https://schema.org/Nonprofit501c20"
    Nonprofit501c21 = "https://schema.org/Nonprofit501c21"
    Nonprofit501c22 = "https://schema.org/Nonprofit501c22"
    Nonprofit501c23 = "https://schema.org/Nonprofit501c23"
    Nonprofit501c24 = "https://schema.org/Nonprofit501c24"
    Nonprofit501c25 = "https://schema.org/Nonprofit501c25"
    Nonprofit501c26 = "https://schema.org/Nonprofit501c26"
    Nonprofit501c27 = "https://schema.org/Nonprofit501c27"
    Nonprofit501c28 = "https://schema.org/Nonprofit501c28"
    Nonprofit501c3 = "https://schema.org/Nonprofit501c3"
    Nonprofit501c4 = "https://schema.org/Nonprofit501c4"
    Nonprofit501c5 = "https://schema.org/Nonprofit501c5"
    Nonprofit501c6 = "https://schema.org/Nonprofit501c6"
    Nonprofit501c7 = "https://schema.org/Nonprofit501c7"
    Nonprofit501c8 = "https://schema.org/Nonprofit501c8"
    Nonprofit501c9 = "https://schema.org/Nonprofit501c9"
    Nonprofit501d = "https://schema.org/Nonprofit501d"
    Nonprofit501e = "https://schema.org/Nonprofit501e"
    Nonprofit501f = "https://schema.org/Nonprofit501f"
    Nonprofit501k = "https://schema.org/Nonprofit501k"
    Nonprofit501n = "https://schema.org/Nonprofit501n"
    Nonprofit501q = "https://schema.org/Nonprofit501q"
    Nonprofit527 = "https://schema.org/Nonprofit527"


class WearableMeasurementTypeEnumeration(SchemaEnumeration):
    """Enumerates common types of measurement for wearables products.

    https://schema.org/WearableMeasurementTypeEnumeration
    """

    WearableMeasurementBack = "https://schema.org/WearableMeasurementBack"
    WearableMeasurementChestOrBust = "https://schema.org/WearableMeasurementChestOrBust"
    WearableMeasurementCollar = "https://schema.org/WearableMeasurementCollar"
    WearableMeasurementCup = "https://schema.org/WearableMeasurementCup"
    WearableMeasurementHeight = "https://schema.org/WearableMeasurementHeight"
    WearableMeasurementHips = "https://schema.org/WearableMeasurementHips"
    WearableMeasurementInseam = "https://schema.org/WearableMeasurementInseam"
    WearableMeasurementLength = "https://schema.org/WearableMeasurementLength"
    WearableMeasurementOutsideLeg = "https://schema.org/WearableMeasurementOutsideLeg"
    WearableMeasurementSleeve = "https://schema.org/WearableMeasurementSleeve"
    WearableMeasurementWaist = "https://schema.org/WearableMeasurementWaist"
    WearableMeasurementWidth = "https://schema.org/WearableMeasurementWidth"


class WearableSizeGroupEnumeration(SchemaEnumeration):
    """Enumerates common size groups (also known as "size types") for wearable products.

    https://schema.org/WearableSizeGroupEnumeration
    """

    WearableSizeGroupBig = "https://schema.org/WearableSizeGroupBig"
    WearableSizeGroupBoys = "https://schema.org/WearableSizeGroupBoys"
    WearableSizeGroupExtraShort = "https://schema.org/WearableSizeGroupExtraShort"
    WearableSizeGroupExtraTall = "https://schema.org/WearableSizeGroupExtraTall"
    WearableSizeGroupGirls = "https://schema.org/WearableSizeGroupGirls"
    WearableSizeGroupHusky = "https://schema.org/WearableSizeGroupHusky"
    WearableSizeGroupInfants = "https://schema.org/WearableSizeGroupInfants"
    WearableSizeGroupJuniors = "https://schema.org/WearableSizeGroupJuniors"
    WearableSizeGroupMaternity = "https://schema.org/WearableSizeGroupMaternity"
    WearableSizeGroupMens = "https://schema.org/WearableSizeGroupMens"
    WearableSizeGroupMisses = "https://schema.org/WearableSizeGroupMisses"
    WearableSizeGroupPetite = "https://schema.org/WearableSizeGroupPetite"
    WearableSizeGroupPlus = "https://schema.org/WearableSizeGroupPlus"
    WearableSizeGroupRegular = "https://schema.org/WearableSizeGroupRegular"
    WearableSizeGroupShort = "https://schema.org/WearableSizeGroupShort"
    WearableSizeGroupTall = "https://schema.org/WearableSizeGroupTall"
    WearableSizeGroupWomens = "https://schema.org/WearableSizeGroupWomens"


class WearableSizeSystemEnumeration(SchemaEnumeration):
    """Enumerates common size systems specific for wearable products.

    https://schema.org/WearableSizeSystemEnumeration
    """

    WearableSizeSystemAU = "https://schema.org/WearableSizeSystemAU"
    WearableSizeSystemBR = "https://schema.org/WearableSizeSystemBR"
    WearableSizeSystemCN = "https://schema.org/WearableSizeSystemCN"
    WearableSizeSystemContinental = "https://schema.org/WearableSizeSystemContinental"
    WearableSizeSystemDE = "https://schema.org/WearableSizeSystemDE"
    WearableSizeSystemEN13402 = "https://schema.org/WearableSizeSystemEN13402"
    WearableSizeSystemEurope = "https://schema.org/WearableSizeSystemEurope"
    WearableSizeSystemFR = "https://schema.org/WearableSizeSystemFR"
    WearableSizeSystemGS1 = "https://schema.org/WearableSizeSystemGS1"
    WearableSizeSystemIT = "https://schema.org/WearableSizeSystemIT"
    WearableSizeSystemJP = "https://schema.org/WearableSizeSystemJP"
    WearableSizeSystemMX = "https://schema.org/WearableSizeSystemMX"
    WearableSizeSystemUK = "https://schema.org/WearableSizeSystemUK"
    WearableSizeSystemUS = "https://schema.org/WearableSizeSystemUS"
