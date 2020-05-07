# This is free and unencumbered software released into the public domain.

import ctypes, ctypes.util

openxr = ctypes.CDLL(
    ctypes.util.find_library("libopenxr_loader.so.1")
    or ctypes.util.find_library("openxr_loader")
    or "openxr_loader"
)

xrAcquireSwapchainImage = openxr.xrAcquireSwapchainImage
xrAcquireSwapchainImage.restype = ctypes.c_int
xrAcquireSwapchainImage.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrApplyHapticFeedback = openxr.xrApplyHapticFeedback
xrApplyHapticFeedback.restype = ctypes.c_int
xrApplyHapticFeedback.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrAttachSessionActionSets = openxr.xrAttachSessionActionSets
xrAttachSessionActionSets.restype = ctypes.c_int
xrAttachSessionActionSets.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrBeginFrame = openxr.xrBeginFrame
xrBeginFrame.restype = ctypes.c_int
xrBeginFrame.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrBeginSession = openxr.xrBeginSession
xrBeginSession.restype = ctypes.c_int
xrBeginSession.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrCreateAction = openxr.xrCreateAction
xrCreateAction.restype = ctypes.c_int
xrCreateAction.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrCreateActionSet = openxr.xrCreateActionSet
xrCreateActionSet.restype = ctypes.c_int
xrCreateActionSet.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrCreateActionSpace = openxr.xrCreateActionSpace
xrCreateActionSpace.restype = ctypes.c_int
xrCreateActionSpace.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

#xrCreateDebugUtilsMessengerEXT = openxr.xrCreateDebugUtilsMessengerEXT
#xrCreateDebugUtilsMessengerEXT.restype = ctypes.c_int
#xrCreateDebugUtilsMessengerEXT.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrCreateInstance = openxr.xrCreateInstance
xrCreateInstance.restype = ctypes.c_int
xrCreateInstance.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrCreateReferenceSpace = openxr.xrCreateReferenceSpace
xrCreateReferenceSpace.restype = ctypes.c_int
xrCreateReferenceSpace.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrCreateSession = openxr.xrCreateSession
xrCreateSession.restype = ctypes.c_int
xrCreateSession.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

#xrCreateSpatialAnchorMSFT = openxr.xrCreateSpatialAnchorMSFT
#xrCreateSpatialAnchorMSFT.restype = ctypes.c_int
#xrCreateSpatialAnchorMSFT.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

#xrCreateSpatialAnchorSpaceMSFT = openxr.xrCreateSpatialAnchorSpaceMSFT
#xrCreateSpatialAnchorSpaceMSFT.restype = ctypes.c_int
#xrCreateSpatialAnchorSpaceMSFT.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrCreateSwapchain = openxr.xrCreateSwapchain
xrCreateSwapchain.restype = ctypes.c_int
xrCreateSwapchain.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrDestroyAction = openxr.xrDestroyAction
xrDestroyAction.restype = ctypes.c_int
xrDestroyAction.argtypes = [ctypes.c_void_p]

xrDestroyActionSet = openxr.xrDestroyActionSet
xrDestroyActionSet.restype = ctypes.c_int
xrDestroyActionSet.argtypes = [ctypes.c_void_p]

#xrDestroyDebugUtilsMessengerEXT = openxr.xrDestroyDebugUtilsMessengerEXT
#xrDestroyDebugUtilsMessengerEXT.restype = ctypes.c_int
#xrDestroyDebugUtilsMessengerEXT.argtypes = [ctypes.c_void_p]

xrDestroyInstance = openxr.xrDestroyInstance
xrDestroyInstance.restype = ctypes.c_int
xrDestroyInstance.argtypes = [ctypes.c_void_p]

xrDestroySession = openxr.xrDestroySession
xrDestroySession.restype = ctypes.c_int
xrDestroySession.argtypes = [ctypes.c_void_p]

xrDestroySpace = openxr.xrDestroySpace
xrDestroySpace.restype = ctypes.c_int
xrDestroySpace.argtypes = [ctypes.c_void_p]

#xrDestroySpatialAnchorMSFT = openxr.xrDestroySpatialAnchorMSFT
#xrDestroySpatialAnchorMSFT.restype = ctypes.c_int
#xrDestroySpatialAnchorMSFT.argtypes = [ctypes.c_void_p]

xrDestroySwapchain = openxr.xrDestroySwapchain
xrDestroySwapchain.restype = ctypes.c_int
xrDestroySwapchain.argtypes = [ctypes.c_void_p]

xrEndFrame = openxr.xrEndFrame
xrEndFrame.restype = ctypes.c_int
xrEndFrame.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrEndSession = openxr.xrEndSession
xrEndSession.restype = ctypes.c_int
xrEndSession.argtypes = [ctypes.c_void_p]

xrEnumerateApiLayerProperties = openxr.xrEnumerateApiLayerProperties
xrEnumerateApiLayerProperties.restype = ctypes.c_int
xrEnumerateApiLayerProperties.argtypes = [ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateBoundSourcesForAction = openxr.xrEnumerateBoundSourcesForAction
xrEnumerateBoundSourcesForAction.restype = ctypes.c_int
xrEnumerateBoundSourcesForAction.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateEnvironmentBlendModes = openxr.xrEnumerateEnvironmentBlendModes
xrEnumerateEnvironmentBlendModes.restype = ctypes.c_int
xrEnumerateEnvironmentBlendModes.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_int, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int]

xrEnumerateInstanceExtensionProperties = openxr.xrEnumerateInstanceExtensionProperties
xrEnumerateInstanceExtensionProperties.restype = ctypes.c_int
xrEnumerateInstanceExtensionProperties.argtypes = [ctypes.c_char_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateReferenceSpaces = openxr.xrEnumerateReferenceSpaces
xrEnumerateReferenceSpaces.restype = ctypes.c_int
xrEnumerateReferenceSpaces.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int]

xrEnumerateSwapchainFormats = openxr.xrEnumerateSwapchainFormats
xrEnumerateSwapchainFormats.restype = ctypes.c_int
xrEnumerateSwapchainFormats.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateSwapchainImages = openxr.xrEnumerateSwapchainImages
xrEnumerateSwapchainImages.restype = ctypes.c_int
xrEnumerateSwapchainImages.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateViewConfigurationViews = openxr.xrEnumerateViewConfigurationViews
xrEnumerateViewConfigurationViews.restype = ctypes.c_int
xrEnumerateViewConfigurationViews.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_int, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrEnumerateViewConfigurations = openxr.xrEnumerateViewConfigurations
xrEnumerateViewConfigurations.restype = ctypes.c_int
xrEnumerateViewConfigurations.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int]

xrGetActionStateBoolean = openxr.xrGetActionStateBoolean
xrGetActionStateBoolean.restype = ctypes.c_int
xrGetActionStateBoolean.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrGetActionStateFloat = openxr.xrGetActionStateFloat
xrGetActionStateFloat.restype = ctypes.c_int
xrGetActionStateFloat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrGetActionStatePose = openxr.xrGetActionStatePose
xrGetActionStatePose.restype = ctypes.c_int
xrGetActionStatePose.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrGetActionStateVector2f = openxr.xrGetActionStateVector2f
xrGetActionStateVector2f.restype = ctypes.c_int
xrGetActionStateVector2f.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrGetCurrentInteractionProfile = openxr.xrGetCurrentInteractionProfile
xrGetCurrentInteractionProfile.restype = ctypes.c_int
xrGetCurrentInteractionProfile.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p]

xrGetInputSourceLocalizedName = openxr.xrGetInputSourceLocalizedName
xrGetInputSourceLocalizedName.restype = ctypes.c_int
xrGetInputSourceLocalizedName.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_char_p]

xrGetInstanceProcAddr = openxr.xrGetInstanceProcAddr
xrGetInstanceProcAddr.restype = ctypes.c_int
xrGetInstanceProcAddr.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

xrGetInstanceProperties = openxr.xrGetInstanceProperties
xrGetInstanceProperties.restype = ctypes.c_int
xrGetInstanceProperties.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrGetReferenceSpaceBoundsRect = openxr.xrGetReferenceSpaceBoundsRect
xrGetReferenceSpaceBoundsRect.restype = ctypes.c_int
xrGetReferenceSpaceBoundsRect.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

xrGetSystem = openxr.xrGetSystem
xrGetSystem.restype = ctypes.c_int
xrGetSystem.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrGetSystemProperties = openxr.xrGetSystemProperties
xrGetSystemProperties.restype = ctypes.c_int
xrGetSystemProperties.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p]

xrGetViewConfigurationProperties = openxr.xrGetViewConfigurationProperties
xrGetViewConfigurationProperties.restype = ctypes.c_int
xrGetViewConfigurationProperties.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_int, ctypes.c_void_p]

#xrGetVisibilityMaskKHR = openxr.xrGetVisibilityMaskKHR
#xrGetVisibilityMaskKHR.restype = ctypes.c_int
#xrGetVisibilityMaskKHR.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.c_int, ctypes.c_void_p]

xrLocateSpace = openxr.xrLocateSpace
xrLocateSpace.restype = ctypes.c_int
xrLocateSpace.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p]

xrLocateViews = openxr.xrLocateViews
xrLocateViews.restype = ctypes.c_int
xrLocateViews.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

xrPathToString = openxr.xrPathToString
xrPathToString.restype = ctypes.c_int
xrPathToString.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_char_p]

#xrPerfSettingsSetPerformanceLevelEXT = openxr.xrPerfSettingsSetPerformanceLevelEXT
#xrPerfSettingsSetPerformanceLevelEXT.restype = ctypes.c_int
#xrPerfSettingsSetPerformanceLevelEXT.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

xrPollEvent = openxr.xrPollEvent
xrPollEvent.restype = ctypes.c_int
xrPollEvent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrReleaseSwapchainImage = openxr.xrReleaseSwapchainImage
xrReleaseSwapchainImage.restype = ctypes.c_int
xrReleaseSwapchainImage.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrRequestExitSession = openxr.xrRequestExitSession
xrRequestExitSession.restype = ctypes.c_int
xrRequestExitSession.argtypes = [ctypes.c_void_p]

xrResultToString = openxr.xrResultToString
xrResultToString.restype = ctypes.c_int
xrResultToString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

#xrSessionBeginDebugUtilsLabelRegionEXT = openxr.xrSessionBeginDebugUtilsLabelRegionEXT
#xrSessionBeginDebugUtilsLabelRegionEXT.restype = ctypes.c_int
#xrSessionBeginDebugUtilsLabelRegionEXT.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

#xrSessionEndDebugUtilsLabelRegionEXT = openxr.xrSessionEndDebugUtilsLabelRegionEXT
#xrSessionEndDebugUtilsLabelRegionEXT.restype = ctypes.c_int
#xrSessionEndDebugUtilsLabelRegionEXT.argtypes = [ctypes.c_void_p]

#xrSessionInsertDebugUtilsLabelEXT = openxr.xrSessionInsertDebugUtilsLabelEXT
#xrSessionInsertDebugUtilsLabelEXT.restype = ctypes.c_int
#xrSessionInsertDebugUtilsLabelEXT.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

#xrSetDebugUtilsObjectNameEXT = openxr.xrSetDebugUtilsObjectNameEXT
#xrSetDebugUtilsObjectNameEXT.restype = ctypes.c_int
#xrSetDebugUtilsObjectNameEXT.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

#xrSetInputDeviceActiveEXT = openxr.xrSetInputDeviceActiveEXT
#xrSetInputDeviceActiveEXT.restype = ctypes.c_int
#xrSetInputDeviceActiveEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_uint]

#xrSetInputDeviceLocationEXT = openxr.xrSetInputDeviceLocationEXT
#xrSetInputDeviceLocationEXT.restype = ctypes.c_int
#xrSetInputDeviceLocationEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p]

#xrSetInputDeviceStateBoolEXT = openxr.xrSetInputDeviceStateBoolEXT
#xrSetInputDeviceStateBoolEXT.restype = ctypes.c_int
#xrSetInputDeviceStateBoolEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_uint]

#xrSetInputDeviceStateFloatEXT = openxr.xrSetInputDeviceStateFloatEXT
#xrSetInputDeviceStateFloatEXT.restype = ctypes.c_int
#xrSetInputDeviceStateFloatEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_float]

#xrSetInputDeviceStateVector2fEXT = openxr.xrSetInputDeviceStateVector2fEXT
#xrSetInputDeviceStateVector2fEXT.restype = ctypes.c_int
#xrSetInputDeviceStateVector2fEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_void_p]

xrStopHapticFeedback = openxr.xrStopHapticFeedback
xrStopHapticFeedback.restype = ctypes.c_int
xrStopHapticFeedback.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrStringToPath = openxr.xrStringToPath
xrStringToPath.restype = ctypes.c_int
xrStringToPath.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

xrStructureTypeToString = openxr.xrStructureTypeToString
xrStructureTypeToString.restype = ctypes.c_int
xrStructureTypeToString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

#xrSubmitDebugUtilsMessageEXT = openxr.xrSubmitDebugUtilsMessageEXT
#xrSubmitDebugUtilsMessageEXT.restype = ctypes.c_int
#xrSubmitDebugUtilsMessageEXT.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_void_p]

xrSuggestInteractionProfileBindings = openxr.xrSuggestInteractionProfileBindings
xrSuggestInteractionProfileBindings.restype = ctypes.c_int
xrSuggestInteractionProfileBindings.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

xrSyncActions = openxr.xrSyncActions
xrSyncActions.restype = ctypes.c_int
xrSyncActions.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

#xrThermalGetTemperatureTrendEXT = openxr.xrThermalGetTemperatureTrendEXT
#xrThermalGetTemperatureTrendEXT.restype = ctypes.c_int
#xrThermalGetTemperatureTrendEXT.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

xrWaitFrame = openxr.xrWaitFrame
xrWaitFrame.restype = ctypes.c_int
xrWaitFrame.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

xrWaitSwapchainImage = openxr.xrWaitSwapchainImage
xrWaitSwapchainImage.restype = ctypes.c_int
xrWaitSwapchainImage.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
