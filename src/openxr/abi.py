# This is free and unencumbered software released into the public domain.

from ctypes import *

# Scalars:

XrVersion = c_uint64
XrFlags64 = c_uint64
XrSystemId = c_uint64
XrBool32 = c_uint32
XrPath = c_uint64
XrTime = c_int64
XrDuration = c_int64

# Handles:

class XrInstance(Structure):
    _fields_ = [('handle', c_void_p)]

class XrSession(Structure):
    _fields_ = [('handle', c_void_p)]

class XrSpace(Structure):
    _fields_ = [('handle', c_void_p)]

class XrAction(Structure):
    _fields_ = [('handle', c_void_p)]

class XrSwapchain(Structure):
    _fields_ = [('handle', c_void_p)]

class XrActionSet(Structure):
    _fields_ = [('handle', c_void_p)]

# Constants:

XR_TRUE = 1
XR_FALSE = 0
XR_MAX_EXTENSION_NAME_SIZE = 128
XR_MAX_API_LAYER_NAME_SIZE = 256
XR_MAX_API_LAYER_DESCRIPTION_SIZE = 256
XR_MAX_SYSTEM_NAME_SIZE = 256
XR_MAX_APPLICATION_NAME_SIZE = 128
XR_MAX_ENGINE_NAME_SIZE = 128
XR_MAX_RUNTIME_NAME_SIZE = 128
XR_MAX_PATH_LENGTH = 256
XR_MAX_STRUCTURE_NAME_SIZE = 64
XR_MAX_RESULT_STRING_SIZE = 64
XR_MIN_COMPOSITION_LAYERS_SUPPORTED = 16
XR_MAX_ACTION_SET_NAME_SIZE = 64
XR_MAX_LOCALIZED_ACTION_SET_NAME_SIZE = 128
XR_MAX_ACTION_NAME_SIZE = 64
XR_MAX_LOCALIZED_ACTION_NAME_SIZE = 128

# Enums:

XrActionType = c_int
XR_ACTION_TYPE_BOOLEAN_INPUT = 1
XR_ACTION_TYPE_FLOAT_INPUT = 2
XR_ACTION_TYPE_VECTOR2F_INPUT = 3
XR_ACTION_TYPE_POSE_INPUT = 4
XR_ACTION_TYPE_VIBRATION_OUTPUT = 100

XrAndroidThreadTypeKHR = c_int
XR_ANDROID_THREAD_TYPE_APPLICATION_MAIN_KHR = 1
XR_ANDROID_THREAD_TYPE_APPLICATION_WORKER_KHR = 2
XR_ANDROID_THREAD_TYPE_RENDERER_MAIN_KHR = 3
XR_ANDROID_THREAD_TYPE_RENDERER_WORKER_KHR = 4

XrCompositionLayerFlagBits = c_int
XR_COMPOSITION_LAYER_CORRECT_CHROMATIC_ABERRATION_BIT = 1
XR_COMPOSITION_LAYER_BLEND_TEXTURE_SOURCE_ALPHA_BIT = 2
XR_COMPOSITION_LAYER_UNPREMULTIPLIED_ALPHA_BIT = 4

XrDebugUtilsMessageSeverityFlagBitsEXT = c_int
XR_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT = 1
XR_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT = 16
XR_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT = 256
XR_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT = 4096

XrDebugUtilsMessageTypeFlagBitsEXT = c_int
XR_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT = 1
XR_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT = 2
XR_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT = 4
XR_DEBUG_UTILS_MESSAGE_TYPE_CONFORMANCE_BIT_EXT = 8

XrEnvironmentBlendMode = c_int
XR_ENVIRONMENT_BLEND_MODE_OPAQUE = 1
XR_ENVIRONMENT_BLEND_MODE_ADDITIVE = 2
XR_ENVIRONMENT_BLEND_MODE_ALPHA_BLEND = 3

XrEyeVisibility = c_int
XR_EYE_VISIBILITY_BOTH = 0
XR_EYE_VISIBILITY_LEFT = 1
XR_EYE_VISIBILITY_RIGHT = 2

XrFormFactor = c_int
XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY = 1
XR_FORM_FACTOR_HANDHELD_DISPLAY = 2
XR_FORM_FACTOR_MAX_ENUM = 0x7FFFFFFF

XrInputSourceLocalizedNameFlagBits = c_int
XR_INPUT_SOURCE_LOCALIZED_NAME_USER_PATH_BIT = 1
XR_INPUT_SOURCE_LOCALIZED_NAME_INTERACTION_PROFILE_BIT = 2
XR_INPUT_SOURCE_LOCALIZED_NAME_COMPONENT_BIT = 4

XrInstanceCreateFlagBits = c_int

XrObjectType = c_int
XR_OBJECT_TYPE_UNKNOWN = 0
XR_OBJECT_TYPE_INSTANCE = 1
XR_OBJECT_TYPE_SESSION = 2
XR_OBJECT_TYPE_SWAPCHAIN = 3
XR_OBJECT_TYPE_SPACE = 4
XR_OBJECT_TYPE_ACTION_SET = 5
XR_OBJECT_TYPE_ACTION = 6

XrOverlayMainSessionFlagBitsEXTX = c_int
XR_OVERLAY_MAIN_SESSION_ENABLED_COMPOSITION_LAYER_INFO_DEPTH_BIT_EXTX = 1

XrOverlaySessionCreateFlagBitsEXTX = c_int
XR_OVERLAY_SESSION_CREATE_RELAXED_DISPLAY_TIME_BIT_EXTX = 1

XrPerfSettingsDomainEXT = c_int
XR_PERF_SETTINGS_DOMAIN_CPU_EXT = 1
XR_PERF_SETTINGS_DOMAIN_GPU_EXT = 2

XrPerfSettingsLevelEXT = c_int
XR_PERF_SETTINGS_LEVEL_POWER_SAVINGS_EXT = 0
XR_PERF_SETTINGS_LEVEL_SUSTAINED_LOW_EXT = 25
XR_PERF_SETTINGS_LEVEL_SUSTAINED_HIGH_EXT = 50
XR_PERF_SETTINGS_LEVEL_BOOST_EXT = 75

XrPerfSettingsNotificationLevelEXT = c_int
XR_PERF_SETTINGS_NOTIF_LEVEL_NORMAL_EXT = 0
XR_PERF_SETTINGS_NOTIF_LEVEL_WARNING_EXT = 25
XR_PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED_EXT = 75

XrPerfSettingsSubDomainEXT = c_int
XR_PERF_SETTINGS_SUB_DOMAIN_COMPOSITING_EXT = 1
XR_PERF_SETTINGS_SUB_DOMAIN_RENDERING_EXT = 2
XR_PERF_SETTINGS_SUB_DOMAIN_THERMAL_EXT = 3

XrReferenceSpaceType = c_int
XR_REFERENCE_SPACE_TYPE_VIEW = 1
XR_REFERENCE_SPACE_TYPE_LOCAL = 2
XR_REFERENCE_SPACE_TYPE_STAGE = 3

XrResult = c_int
XR_SUCCESS = 0
XR_TIMEOUT_EXPIRED = 1
XR_SESSION_LOSS_PENDING = 3
XR_EVENT_UNAVAILABLE = 4
XR_SPACE_BOUNDS_UNAVAILABLE = 7
XR_SESSION_NOT_FOCUSED = 8
XR_FRAME_DISCARDED = 9
XR_ERROR_VALIDATION_FAILURE = -1
XR_ERROR_RUNTIME_FAILURE = -2
XR_ERROR_OUT_OF_MEMORY = -3
XR_ERROR_API_VERSION_UNSUPPORTED = -4
XR_ERROR_INITIALIZATION_FAILED = -6
XR_ERROR_FUNCTION_UNSUPPORTED = -7
XR_ERROR_FEATURE_UNSUPPORTED = -8
XR_ERROR_EXTENSION_NOT_PRESENT = -9
XR_ERROR_LIMIT_REACHED = -10
XR_ERROR_SIZE_INSUFFICIENT = -11
XR_ERROR_HANDLE_INVALID = -12
XR_ERROR_INSTANCE_LOST = -13
XR_ERROR_SESSION_RUNNING = -14
XR_ERROR_SESSION_NOT_RUNNING = -16
XR_ERROR_SESSION_LOST = -17
XR_ERROR_SYSTEM_INVALID = -18
XR_ERROR_PATH_INVALID = -19
XR_ERROR_PATH_COUNT_EXCEEDED = -20
XR_ERROR_PATH_FORMAT_INVALID = -21
XR_ERROR_PATH_UNSUPPORTED = -22
XR_ERROR_LAYER_INVALID = -23
XR_ERROR_LAYER_LIMIT_EXCEEDED = -24
XR_ERROR_SWAPCHAIN_RECT_INVALID = -25
XR_ERROR_SWAPCHAIN_FORMAT_UNSUPPORTED = -26
XR_ERROR_ACTION_TYPE_MISMATCH = -27
XR_ERROR_SESSION_NOT_READY = -28
XR_ERROR_SESSION_NOT_STOPPING = -29
XR_ERROR_TIME_INVALID = -30
XR_ERROR_REFERENCE_SPACE_UNSUPPORTED = -31
XR_ERROR_FILE_ACCESS_ERROR = -32
XR_ERROR_FILE_CONTENTS_INVALID = -33
XR_ERROR_FORM_FACTOR_UNSUPPORTED = -34
XR_ERROR_FORM_FACTOR_UNAVAILABLE = -35
XR_ERROR_API_LAYER_NOT_PRESENT = -36
XR_ERROR_CALL_ORDER_INVALID = -37
XR_ERROR_GRAPHICS_DEVICE_INVALID = -38
XR_ERROR_POSE_INVALID = -39
XR_ERROR_INDEX_OUT_OF_RANGE = -40
XR_ERROR_VIEW_CONFIGURATION_TYPE_UNSUPPORTED = -41
XR_ERROR_ENVIRONMENT_BLEND_MODE_UNSUPPORTED = -42
XR_ERROR_NAME_DUPLICATED = -44
XR_ERROR_NAME_INVALID = -45
XR_ERROR_ACTIONSET_NOT_ATTACHED = -46
XR_ERROR_ACTIONSETS_ALREADY_ATTACHED = -47
XR_ERROR_LOCALIZED_NAME_DUPLICATED = -48
XR_ERROR_LOCALIZED_NAME_INVALID = -49
XR_ERROR_ANDROID_THREAD_SETTINGS_ID_INVALID_KHR = -1000003000
XR_ERROR_ANDROID_THREAD_SETTINGS_FAILURE_KHR = -1000003001
XR_ERROR_CREATE_SPATIAL_ANCHOR_FAILED_MSFT = -1000039001
XR_RESULT_MAX_ENUM = 0x7FFFFFFF

XrSessionCreateFlagBits = c_int

XrSessionState = c_int
XR_SESSION_STATE_UNKNOWN = 0
XR_SESSION_STATE_IDLE = 1
XR_SESSION_STATE_READY = 2
XR_SESSION_STATE_SYNCHRONIZED = 3
XR_SESSION_STATE_VISIBLE = 4
XR_SESSION_STATE_FOCUSED = 5
XR_SESSION_STATE_STOPPING = 6
XR_SESSION_STATE_LOSS_PENDING = 7
XR_SESSION_STATE_EXITING = 8

XrSpaceLocationFlagBits = c_int
XR_SPACE_LOCATION_ORIENTATION_VALID_BIT = 1
XR_SPACE_LOCATION_POSITION_VALID_BIT = 2
XR_SPACE_LOCATION_ORIENTATION_TRACKED_BIT = 4
XR_SPACE_LOCATION_POSITION_TRACKED_BIT = 8

XrSpaceVelocityFlagBits = c_int
XR_SPACE_VELOCITY_LINEAR_VALID_BIT = 1
XR_SPACE_VELOCITY_ANGULAR_VALID_BIT = 2

XrStructureType = c_int
XR_TYPE_UNKNOWN = 0
XR_TYPE_API_LAYER_PROPERTIES = 1
XR_TYPE_EXTENSION_PROPERTIES = 2
XR_TYPE_INSTANCE_CREATE_INFO = 3
XR_TYPE_SYSTEM_GET_INFO = 4
XR_TYPE_SYSTEM_PROPERTIES = 5
XR_TYPE_VIEW_LOCATE_INFO = 6
XR_TYPE_VIEW = 7
XR_TYPE_SESSION_CREATE_INFO = 8
XR_TYPE_SWAPCHAIN_CREATE_INFO = 9
XR_TYPE_SESSION_BEGIN_INFO = 10
XR_TYPE_VIEW_STATE = 11
XR_TYPE_FRAME_END_INFO = 12
XR_TYPE_HAPTIC_VIBRATION = 13
XR_TYPE_EVENT_DATA_BUFFER = 16
XR_TYPE_EVENT_DATA_INSTANCE_LOSS_PENDING = 17
XR_TYPE_EVENT_DATA_SESSION_STATE_CHANGED = 18
XR_TYPE_ACTION_STATE_BOOLEAN = 23
XR_TYPE_ACTION_STATE_FLOAT = 24
XR_TYPE_ACTION_STATE_VECTOR2F = 25
XR_TYPE_ACTION_STATE_POSE = 27
XR_TYPE_ACTION_SET_CREATE_INFO = 28
XR_TYPE_ACTION_CREATE_INFO = 29
XR_TYPE_INSTANCE_PROPERTIES = 32
XR_TYPE_FRAME_WAIT_INFO = 33
XR_TYPE_COMPOSITION_LAYER_PROJECTION = 35
XR_TYPE_COMPOSITION_LAYER_QUAD = 36
XR_TYPE_REFERENCE_SPACE_CREATE_INFO = 37
XR_TYPE_ACTION_SPACE_CREATE_INFO = 38
XR_TYPE_EVENT_DATA_REFERENCE_SPACE_CHANGE_PENDING = 40
XR_TYPE_VIEW_CONFIGURATION_VIEW = 41
XR_TYPE_SPACE_LOCATION = 42
XR_TYPE_SPACE_VELOCITY = 43
XR_TYPE_FRAME_STATE = 44
XR_TYPE_VIEW_CONFIGURATION_PROPERTIES = 45
XR_TYPE_FRAME_BEGIN_INFO = 46
XR_TYPE_COMPOSITION_LAYER_PROJECTION_VIEW = 48
XR_TYPE_EVENT_DATA_EVENTS_LOST = 49
XR_TYPE_INTERACTION_PROFILE_SUGGESTED_BINDING = 51
XR_TYPE_EVENT_DATA_INTERACTION_PROFILE_CHANGED = 52
XR_TYPE_INTERACTION_PROFILE_STATE = 53
XR_TYPE_SWAPCHAIN_IMAGE_ACQUIRE_INFO = 55
XR_TYPE_SWAPCHAIN_IMAGE_WAIT_INFO = 56
XR_TYPE_SWAPCHAIN_IMAGE_RELEASE_INFO = 57
XR_TYPE_ACTION_STATE_GET_INFO = 58
XR_TYPE_HAPTIC_ACTION_INFO = 59
XR_TYPE_SESSION_ACTION_SETS_ATTACH_INFO = 60
XR_TYPE_ACTIONS_SYNC_INFO = 61
XR_TYPE_BOUND_SOURCES_FOR_ACTION_ENUMERATE_INFO = 62
XR_TYPE_INPUT_SOURCE_LOCALIZED_NAME_GET_INFO = 63
XR_TYPE_COMPOSITION_LAYER_CUBE_KHR = 1000006000
XR_TYPE_INSTANCE_CREATE_INFO_ANDROID_KHR = 1000008000
XR_TYPE_COMPOSITION_LAYER_DEPTH_INFO_KHR = 1000010000
XR_TYPE_VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR = 1000014000
XR_TYPE_EVENT_DATA_PERF_SETTINGS_EXT = 1000015000
XR_TYPE_COMPOSITION_LAYER_CYLINDER_KHR = 1000017000
XR_TYPE_COMPOSITION_LAYER_EQUIRECT_KHR = 1000018000
XR_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT = 1000019000
XR_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT = 1000019001
XR_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT = 1000019002
XR_TYPE_DEBUG_UTILS_LABEL_EXT = 1000019003
XR_TYPE_GRAPHICS_BINDING_OPENGL_WIN32_KHR = 1000023000
XR_TYPE_GRAPHICS_BINDING_OPENGL_XLIB_KHR = 1000023001
XR_TYPE_GRAPHICS_BINDING_OPENGL_XCB_KHR = 1000023002
XR_TYPE_GRAPHICS_BINDING_OPENGL_WAYLAND_KHR = 1000023003
XR_TYPE_SWAPCHAIN_IMAGE_OPENGL_KHR = 1000023004
XR_TYPE_GRAPHICS_REQUIREMENTS_OPENGL_KHR = 1000023005
XR_TYPE_GRAPHICS_BINDING_OPENGL_ES_ANDROID_KHR = 1000024001
XR_TYPE_SWAPCHAIN_IMAGE_OPENGL_ES_KHR = 1000024002
XR_TYPE_GRAPHICS_REQUIREMENTS_OPENGL_ES_KHR = 1000024003
XR_TYPE_GRAPHICS_BINDING_VULKAN_KHR = 1000025000
XR_TYPE_SWAPCHAIN_IMAGE_VULKAN_KHR = 1000025001
XR_TYPE_GRAPHICS_REQUIREMENTS_VULKAN_KHR = 1000025002
XR_TYPE_GRAPHICS_BINDING_D3D11_KHR = 1000027000
XR_TYPE_SWAPCHAIN_IMAGE_D3D11_KHR = 1000027001
XR_TYPE_GRAPHICS_REQUIREMENTS_D3D11_KHR = 1000027002
XR_TYPE_GRAPHICS_BINDING_D3D12_KHR = 1000028000
XR_TYPE_SWAPCHAIN_IMAGE_D3D12_KHR = 1000028001
XR_TYPE_GRAPHICS_REQUIREMENTS_D3D12_KHR = 1000028002
XR_TYPE_SYSTEM_EYE_GAZE_INTERACTION_PROPERTIES_EXT = 1000030000
XR_TYPE_EYE_GAZE_SAMPLE_TIME_EXT = 1000030001
XR_TYPE_VISIBILITY_MASK_KHR = 1000031000
XR_TYPE_EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR = 1000031001
XR_TYPE_SESSION_CREATE_INFO_OVERLAY_EXTX = 1000033000
XR_TYPE_EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX = 1000033003
XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_MSFT = 1000039000
XR_TYPE_SPATIAL_ANCHOR_SPACE_CREATE_INFO_MSFT = 1000039001
XR_TYPE_VIEW_CONFIGURATION_DEPTH_RANGE_EXT = 1000046000
XR_TYPE_VIEW_CONFIGURATION_VIEW_FOV_EPIC = 1000059000
XR_STRUCTURE_TYPE_MAX_ENUM = 0x7FFFFFFF

XrSwapchainCreateFlagBits = c_int
XR_SWAPCHAIN_CREATE_PROTECTED_CONTENT_BIT = 1
XR_SWAPCHAIN_CREATE_STATIC_IMAGE_BIT = 2

XrSwapchainUsageFlagBits = c_int
XR_SWAPCHAIN_USAGE_COLOR_ATTACHMENT_BIT = 1
XR_SWAPCHAIN_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT = 2
XR_SWAPCHAIN_USAGE_UNORDERED_ACCESS_BIT = 4
XR_SWAPCHAIN_USAGE_TRANSFER_SRC_BIT = 8
XR_SWAPCHAIN_USAGE_TRANSFER_DST_BIT = 16
XR_SWAPCHAIN_USAGE_SAMPLED_BIT = 32
XR_SWAPCHAIN_USAGE_MUTABLE_FORMAT_BIT = 64

XrViewConfigurationType = c_int
XR_VIEW_CONFIGURATION_TYPE_PRIMARY_MONO = 1
XR_VIEW_CONFIGURATION_TYPE_PRIMARY_STEREO = 2

XrViewStateFlagBits = c_int
XR_VIEW_STATE_ORIENTATION_VALID_BIT = 1
XR_VIEW_STATE_POSITION_VALID_BIT = 2
XR_VIEW_STATE_ORIENTATION_TRACKED_BIT = 4
XR_VIEW_STATE_POSITION_TRACKED_BIT = 8

XrVisibilityMaskTypeKHR = c_int
XR_VISIBILITY_MASK_TYPE_HIDDEN_TRIANGLE_MESH_KHR = 1
XR_VISIBILITY_MASK_TYPE_VISIBLE_TRIANGLE_MESH_KHR = 2
XR_VISIBILITY_MASK_TYPE_LINE_LOOP_KHR = 3

# Flags:

XrInstanceCreateFlags = XrFlags64
XrSessionCreateFlags = XrFlags64

# Structs:

class XrBaseStructure(Structure):
    _fields_ = [('type', XrStructureType), ('next', c_void_p)]

class XrActionCreateInfo(Structure):
    pass  # TODO

class XrActionSetCreateInfo(Structure):
    pass  # TODO

class XrActionSpaceCreateInfo(Structure):
    pass  # TODO

class XrActionStateBoolean(Structure):
    pass  # TODO

class XrActionStateFloat(Structure):
    pass  # TODO

class XrActionStateGetInfo(Structure):
    pass  # TODO

class XrActionStatePose(Structure):
    pass  # TODO

class XrActionStateVector2f(Structure):
    pass  # TODO

class XrActionSuggestedBinding(Structure):
    pass  # TODO

class XrActionsSyncInfo(Structure):
    pass  # TODO

class XrActiveActionSet(Structure):
    pass  # TODO

class XrApiLayerProperties(Structure):
    pass  # TODO

class XrApplicationInfo(Structure):
    pass  # TODO

XrBaseInStructure = XrBaseStructure

XrBaseOutStructure = XrBaseStructure

class XrBoundSourcesForActionEnumerateInfo(Structure):
    pass  # TODO

class XrColor4f(Structure):
    pass  # TODO

class XrCompositionLayerBaseHeader(Structure):
    pass  # TODO

class XrCompositionLayerCubeKHR(Structure):
    pass  # TODO

class XrCompositionLayerCylinderKHR(Structure):
    pass  # TODO

class XrCompositionLayerDepthInfoKHR(Structure):
    pass  # TODO

class XrCompositionLayerEquirectKHR(Structure):
    pass  # TODO

class XrCompositionLayerProjection(Structure):
    pass  # TODO

class XrCompositionLayerProjectionView(Structure):
    pass  # TODO

class XrCompositionLayerQuad(Structure):
    pass  # TODO

class XrDebugUtilsLabelEXT(Structure):
    pass  # TODO

class XrDebugUtilsMessengerCallbackDataEXT(Structure):
    pass  # TODO

class XrDebugUtilsMessengerCreateInfoEXT(Structure):
    pass  # TODO

class XrDebugUtilsObjectNameInfoEXT(Structure):
    pass  # TODO

class XrEventDataBaseHeader(Structure):
    pass  # TODO

class XrEventDataBuffer(Structure):
    pass  # TODO

class XrEventDataEventsLost(Structure):
    pass  # TODO

class XrEventDataInstanceLossPending(Structure):
    pass  # TODO

class XrEventDataInteractionProfileChanged(Structure):
    pass  # TODO

class XrEventDataMainSessionVisibilityChangedEXTX(Structure):
    pass  # TODO

class XrEventDataPerfSettingsEXT(Structure):
    pass  # TODO

class XrEventDataReferenceSpaceChangePending(Structure):
    pass  # TODO

class XrEventDataSessionStateChanged(Structure):
    pass  # TODO

class XrEventDataVisibilityMaskChangedKHR(Structure):
    pass  # TODO

class XrExtensionProperties(Structure):
    pass  # TODO

class XrExtent2Df(Structure):
    pass  # TODO

class XrExtent2Di(Structure):
    pass  # TODO

class XrEyeGazeSampleTimeEXT(Structure):
    pass  # TODO

class XrFovf(Structure):
    pass  # TODO

class XrFrameBeginInfo(Structure):
    pass  # TODO

class XrFrameEndInfo(Structure):
    pass  # TODO

class XrFrameState(Structure):
    pass  # TODO

class XrFrameWaitInfo(Structure):
    pass  # TODO

class XrGraphicsBindingD3D11KHR(Structure):
    pass  # TODO

class XrGraphicsBindingD3D12KHR(Structure):
    pass  # TODO

class XrGraphicsBindingOpenGLESAndroidKHR(Structure):
    pass  # TODO

class XrGraphicsBindingOpenGLWaylandKHR(Structure):
    pass  # TODO

class XrGraphicsBindingOpenGLWin32KHR(Structure):
    pass  # TODO

class XrGraphicsBindingOpenGLXcbKHR(Structure):
    pass  # TODO

class XrGraphicsBindingOpenGLXlibKHR(Structure):
    pass  # TODO

class XrGraphicsBindingVulkanKHR(Structure):
    pass  # TODO

class XrGraphicsRequirementsD3D11KHR(Structure):
    pass  # TODO

class XrGraphicsRequirementsD3D12KHR(Structure):
    pass  # TODO

class XrGraphicsRequirementsOpenGLESKHR(Structure):
    pass  # TODO

class XrGraphicsRequirementsOpenGLKHR(Structure):
    pass  # TODO

class XrGraphicsRequirementsVulkanKHR(Structure):
    pass  # TODO

class XrHapticActionInfo(Structure):
    pass  # TODO

class XrHapticBaseHeader(Structure):
    pass  # TODO

class XrHapticVibration(Structure):
    pass  # TODO

class XrInputSourceLocalizedNameGetInfo(Structure):
    pass  # TODO

class XrInstanceCreateInfo(Structure):
    pass  # TODO

class XrInstanceCreateInfoAndroidKHR(Structure):
    pass  # TODO

class XrInstanceProperties(Structure):
    pass  # TODO

class XrInteractionProfileState(Structure):
    pass  # TODO

class XrInteractionProfileSuggestedBinding(Structure):
    pass  # TODO

class XrOffset2Df(Structure):
    pass  # TODO

class XrOffset2Di(Structure):
    pass  # TODO

class XrPosef(Structure):
    pass  # TODO

class XrQuaternionf(Structure):
    pass  # TODO

class XrRect2Df(Structure):
    pass  # TODO

class XrRect2Di(Structure):
    pass  # TODO

class XrReferenceSpaceCreateInfo(Structure):
    pass  # TODO

class XrSessionActionSetsAttachInfo(Structure):
    pass  # TODO

class XrSessionBeginInfo(Structure):
    pass  # TODO

class XrSessionCreateInfo(Structure):
    pass  # TODO

class XrSessionCreateInfoOverlayEXTX(Structure):
    pass  # TODO

class XrSpaceLocation(Structure):
    pass  # TODO

class XrSpaceVelocity(Structure):
    pass  # TODO

class XrSpatialAnchorCreateInfoMSFT(Structure):
    pass  # TODO

class XrSpatialAnchorSpaceCreateInfoMSFT(Structure):
    pass  # TODO

class XrSwapchainCreateInfo(Structure):
    pass  # TODO

class XrSwapchainImageAcquireInfo(Structure):
    pass  # TODO

class XrSwapchainImageBaseHeader(Structure):
    pass  # TODO

class XrSwapchainImageD3D11KHR(Structure):
    pass  # TODO

class XrSwapchainImageD3D12KHR(Structure):
    pass  # TODO

class XrSwapchainImageOpenGLESKHR(Structure):
    pass  # TODO

class XrSwapchainImageOpenGLKHR(Structure):
    pass  # TODO

class XrSwapchainImageReleaseInfo(Structure):
    pass  # TODO

class XrSwapchainImageVulkanKHR(Structure):
    pass  # TODO

class XrSwapchainImageWaitInfo(Structure):
    pass  # TODO

class XrSwapchainSubImage(Structure):
    pass  # TODO

class XrSystemEyeGazeInteractionPropertiesEXT(Structure):
    pass  # TODO

class XrSystemGetInfo(Structure):
    pass  # TODO

class XrSystemGraphicsProperties(Structure):
    pass  # TODO

class XrSystemProperties(Structure):
    pass  # TODO

class XrSystemTrackingProperties(Structure):
    pass  # TODO

class XrVector2f(Structure):
    pass  # TODO

class XrVector3f(Structure):
    pass  # TODO

class XrVector4f(Structure):
    pass  # TODO

class XrView(Structure):
    pass  # TODO

class XrViewConfigurationDepthRangeEXT(Structure):
    pass  # TODO

class XrViewConfigurationProperties(Structure):
    pass  # TODO

class XrViewConfigurationView(Structure):
    pass  # TODO

class XrViewConfigurationViewFovEPIC(Structure):
    pass  # TODO

class XrViewLocateInfo(Structure):
    pass  # TODO

class XrViewState(Structure):
    pass  # TODO

class XrVisibilityMaskKHR(Structure):
    pass  # TODO

class XrVulkanSwapchainFormatListCreateInfoKHR(Structure):
    pass  # TODO
