# This is free and unencumbered software released into the public domain.

from ctypes import *

XrVersion  = c_uint64
XrFlags64  = c_uint64
XrSystemId = c_uint64
XrBool32   = c_uint32
XrPath     = c_uint64
XrTime     = c_int64
XrDuration = c_int64

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

XR_TRUE                               = 1
XR_FALSE                              = 0
XR_MAX_EXTENSION_NAME_SIZE            = 128
XR_MAX_API_LAYER_NAME_SIZE            = 256
XR_MAX_API_LAYER_DESCRIPTION_SIZE     = 256
XR_MAX_SYSTEM_NAME_SIZE               = 256
XR_MAX_APPLICATION_NAME_SIZE          = 128
XR_MAX_ENGINE_NAME_SIZE               = 128
XR_MAX_RUNTIME_NAME_SIZE              = 128
XR_MAX_PATH_LENGTH                    = 256
XR_MAX_STRUCTURE_NAME_SIZE            = 64
XR_MAX_RESULT_STRING_SIZE             = 64
XR_MIN_COMPOSITION_LAYERS_SUPPORTED   = 16
XR_MAX_ACTION_SET_NAME_SIZE           = 64
XR_MAX_LOCALIZED_ACTION_SET_NAME_SIZE = 128
XR_MAX_ACTION_NAME_SIZE               = 64
XR_MAX_LOCALIZED_ACTION_NAME_SIZE     = 128

XrResult                              = c_int # enum
XR_SUCCESS                            = 0
XR_ERROR_VALIDATION_FAILURE           = -1
XR_ERROR_RUNTIME_FAILURE              = -2
XR_ERROR_HANDLE_INVALID               = -12

XrStructureType                       = c_int # enum
XR_TYPE_UNKNOWN                       = 0
XR_TYPE_API_LAYER_PROPERTIES          = 1
XR_TYPE_EXTENSION_PROPERTIES          = 2
XR_TYPE_INSTANCE_CREATE_INFO          = 3
XR_TYPE_SYSTEM_GET_INFO               = 4
XR_TYPE_SYSTEM_PROPERTIES             = 5
XR_TYPE_VIEW_LOCATE_INFO              = 6
XR_TYPE_VIEW                          = 7
XR_TYPE_SESSION_CREATE_INFO           = 8

XrFormFactor                          = c_int # enum
XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY   = 1
XR_FORM_FACTOR_HANDHELD_DISPLAY       = 2
XR_FORM_FACTOR_MAX_ENUM               = 0x7FFFFFFF

XrInstanceCreateFlags = XrFlags64
XrSessionCreateFlags  = XrFlags64

class XrBaseStructure(Structure):
    _fields_ = [('type', XrStructureType), ('next', c_void_p)]

class XrApiLayerProperties(Structure):
    pass  # TODO

class XrExtensionProperties(Structure):
    pass  # TODO

class XrApplicationInfo(Structure):
    pass  # TODO

class XrInstanceCreateInfo(Structure):
    pass  # TODO

class XrInstanceProperties(Structure):
    pass  # TODO

class XrEventDataBuffer(Structure):
    pass  # TODO

class XrSystemGetInfo(Structure):
    pass  # TODO

class XrSystemGraphicsProperties(Structure):
    pass  # TODO

class XrSystemTrackingProperties(Structure):
    pass  # TODO

class XrSystemProperties(Structure):
    pass  # TODO

class XrSessionCreateInfo(Structure):
    pass  # TODO

class XrVector3f(Structure):
    pass  # TODO

class XrSpaceVelocity(Structure):
    pass  # TODO

class XrQuaternionf(Structure):
    pass  # TODO

class XrPosef(Structure):
    pass  # TODO

class XrReferenceSpaceCreateInfo(Structure):
    pass  # TODO

class XrExtent2Df(Structure):
    pass  # TODO

class XrActionSpaceCreateInfo(Structure):
    pass  # TODO

class XrSpaceLocation(Structure):
    pass  # TODO

class XrViewConfigurationProperties(Structure):
    pass  # TODO

class XrViewConfigurationView(Structure):
    pass  # TODO

class XrSwapchainCreateInfo(Structure):
    pass  # TODO

class XrSwapchainImageBaseHeader(Structure):
    pass  # TODO

class XrSwapchainImageAcquireInfo(Structure):
    pass  # TODO

class XrSwapchainImageWaitInfo(Structure):
    pass  # TODO

class XrSwapchainImageReleaseInfo(Structure):
    pass  # TODO

class XrSessionBeginInfo(Structure):
    pass  # TODO

class XrFrameWaitInfo(Structure):
    pass  # TODO

class XrFrameState(Structure):
    pass  # TODO

class XrFrameBeginInfo(Structure):
    pass  # TODO

class XrCompositionLayerBaseHeader(Structure):
    pass  # TODO

class XrFrameEndInfo(Structure):
    pass  # TODO

class XrViewLocateInfo(Structure):
    pass  # TODO

class XrViewState(Structure):
    pass  # TODO

class XrFovf(Structure):
    pass  # TODO

class XrView(Structure):
    pass  # TODO

class XrActionSetCreateInfo(Structure):
    pass  # TODO

class XrActionCreateInfo(Structure):
    pass  # TODO

class XrActionSuggestedBinding(Structure):
    pass  # TODO

class XrInteractionProfileSuggestedBinding(Structure):
    pass  # TODO

class XrSessionActionSetsAttachInfo(Structure):
    pass  # TODO

class XrInteractionProfileState(Structure):
    pass  # TODO

class XrActionStateGetInfo(Structure):
    pass  # TODO

class XrActionStateBoolean(Structure):
    pass  # TODO

class XrActionStateFloat(Structure):
    pass  # TODO

class XrVector2f(Structure):
    pass  # TODO

class XrActionStateVector2f(Structure):
    pass  # TODO

class XrActionStatePose(Structure):
    pass  # TODO

class XrActiveActionSet(Structure):
    pass  # TODO

class XrActionsSyncInfo(Structure):
    pass  # TODO

class XrBoundSourcesForActionEnumerateInfo(Structure):
    pass  # TODO

class XrInputSourceLocalizedNameGetInfo(Structure):
    pass  # TODO

class XrHapticActionInfo(Structure):
    pass  # TODO

class XrHapticBaseHeader(Structure):
    pass  # TODO

XrBaseInStructure  = XrBaseStructure
XrBaseOutStructure = XrBaseStructure

class XrOffset2Di(Structure):
    pass  # TODO

class XrExtent2Di(Structure):
    pass  # TODO

class XrRect2Di(Structure):
    pass  # TODO

class XrSwapchainSubImage(Structure):
    pass  # TODO

class XrCompositionLayerProjectionView(Structure):
    pass  # TODO

class XrCompositionLayerProjection(Structure):
    pass  # TODO

class XrCompositionLayerQuad(Structure):
    pass  # TODO

class XrEventDataBaseHeader(Structure):
    pass  # TODO

class XrEventDataEventsLost(Structure):
    pass  # TODO

class XrEventDataInstanceLossPending(Structure):
    pass  # TODO

class XrEventDataSessionStateChanged(Structure):
    pass  # TODO

class XrEventDataReferenceSpaceChangePending(Structure):
    pass  # TODO

class XrEventDataInteractionProfileChanged(Structure):
    pass  # TODO

class XrHapticVibration(Structure):
    pass  # TODO

class XrOffset2Df(Structure):
    pass  # TODO

class XrRect2Df(Structure):
    pass  # TODO

class XrVector4f(Structure):
    pass  # TODO

class XrColor4f(Structure):
    pass  # TODO

class XrCompositionLayerCubeKHR(Structure):
    pass  # TODO

class XrCompositionLayerDepthInfoKHR(Structure):
    pass  # TODO

class XrCompositionLayerCylinderKHR(Structure):
    pass  # TODO

class XrCompositionLayerEquirectKHR(Structure):
    pass  # TODO

class XrVisibilityMaskKHR(Structure):
    pass  # TODO

class XrEventDataVisibilityMaskChangedKHR(Structure):
    pass  # TODO

class XrEventDataPerfSettingsEXT(Structure):
    pass  # TODO

class XrDebugUtilsObjectNameInfoEXT(Structure):
    pass  # TODO

class XrDebugUtilsLabelEXT(Structure):
    pass  # TODO

class XrDebugUtilsMessengerCallbackDataEXT(Structure):
    pass  # TODO

class XrDebugUtilsMessengerCreateInfoEXT(Structure):
    pass  # TODO

class XrSystemEyeGazeInteractionPropertiesEXT(Structure):
    pass  # TODO

class XrEyeGazeSampleTimeEXT(Structure):
    pass  # TODO

class XrSessionCreateInfoOverlayEXTX(Structure):
    pass  # TODO

class XrEventDataMainSessionVisibilityChangedEXTX(Structure):
    pass  # TODO

class XrSpatialAnchorCreateInfoMSFT(Structure):
    pass  # TODO

class XrSpatialAnchorSpaceCreateInfoMSFT(Structure):
    pass  # TODO

class XrViewConfigurationDepthRangeEXT(Structure):
    pass  # TODO

class XrViewConfigurationViewFovEPIC(Structure):
    pass  # TODO
