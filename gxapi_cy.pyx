
# cython: c_string_type=unicode, c_string_encoding=utf8

from libc.stdint cimport int32_t, int16_t
from libc.stdlib cimport malloc, free

import threading
from threading import current_thread

thread_local = threading.local()

from geosoft.gxapi import GXCancel, GXExit, GXAPIError, GXError



# Class 3DN


cdef extern void Copy_3DN(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_3DN(void*);


cdef extern void Destroy_3DN(void*, const int32_t*);


cdef extern void GetPointOfView_3DN(void*, const int32_t*, double*, double*, double*);


cdef extern void GetScale_3DN(void*, const int32_t*, double*, double*, double*);


cdef extern int32_t iGetAxisColor_3DN(void*, const int32_t*);


cdef extern void IGetAxisFont_3DN(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetBackgroundColor_3DN(void*, const int32_t*);


cdef extern void IGetRenderControls_3DN(void*, const int32_t*, int32_t*, int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetShading_3DN(void*, const int32_t*);


cdef extern void _SetAxisColor_3DN(void*, const int32_t*, const int32_t*);


cdef extern void _SetAxisFont_3DN(void*, const int32_t*, const void*);


cdef extern void _SetBackgroundColor_3DN(void*, const int32_t*, const int32_t*);


cdef extern void SetPointOfView_3DN(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void SetRenderControls_3DN(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void SetScale_3DN(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void SetShading_3DN(void*, const int32_t*, const int32_t*);



# Class 3DV


cdef extern int32_t OpenMVIEW_3DV(void*, const int32_t*, const int32_t*);


cdef extern void ICopyToMAP_3DV(void*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t CreateNew_3DV(void*, const void*, const int32_t*);


cdef extern int32_t Open_3DV(void*, const void*);


cdef extern int32_t FromMap_3DV(void*, const int32_t*);


cdef extern void CRC3DV_3DV(void*, const int32_t*, int32_t*, const void*);



# Class AGG


cdef extern void _SetModel_AGG(void*, const int32_t*, const int32_t*);


cdef extern void ChangeBrightness_AGG(void*, const int32_t*, const double*);


cdef extern int32_t Create_AGG(void*);


cdef extern int32_t CreateMap_AGG(void*, const int32_t*, const void*);


cdef extern void Destroy_AGG(void*, const int32_t*);


cdef extern void GetLayerITR_AGG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iListImg_AGG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iNumLayers_AGG(void*, const int32_t*);


cdef extern void LayerIMG_AGG(void*, const int32_t*, const void*, const int32_t*, const void*, const double*);


cdef extern void LayerIMGEx_AGG(void*, const int32_t*, const void*, const int32_t*, const void*, const double*, const double*, const double*);


cdef extern void LayerShadeIMG_AGG(void*, const int32_t*, const void*, const void*, const double*, const double*, double*);


cdef extern double rGetBrightness_AGG(void*, const int32_t*);


cdef extern void SetLayerITR_AGG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetRenderMethod_AGG(void*, const int32_t*, const int32_t*);



# Class BF


cdef extern void ReadBuff_BF(void*, const int32_t*, const int32_t*, int32_t);


cdef extern void WriteBuff_BF(void*, const int32_t*, const int32_t*, int32_t);


cdef extern void _ChSize_BF(void*, const int32_t*, const int32_t*);


cdef extern void _Seek_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Copy_BF(void*, const int32_t*, const int32_t*);


cdef extern int32_t CRC_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_BF(void*, const void*, const int32_t*);


cdef extern int32_t CreateSBF_BF(void*, const int32_t*, const void*, const int32_t*);


cdef extern void Destroy_BF(void*, const int32_t*, const int32_t*);


cdef extern void DestroyEx_BF(void*, const int32_t*);


cdef extern int32_t iEOF_BF(void*, const int32_t*);


cdef extern int32_t iQueryWrite_BF(void*, const int32_t*);


cdef extern void IReadBinaryString_BF(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iSize_BF(void*, const int32_t*);


cdef extern int32_t iTell_BF(void*, const int32_t*);


cdef extern void ReadInt_BF(void*, const int32_t*, const int32_t*, int32_t*);


cdef extern void ReadReal_BF(void*, const int32_t*, const int32_t*, double*);


cdef extern void ReadVM_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadVV_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetDestroyStatus_BF(void*, const int32_t*, const int32_t*);


cdef extern void WriteBinaryString_BF(void*, const int32_t*, const int32_t*, const void*);


cdef extern void WriteDataNull_BF(void*, const int32_t*);


cdef extern void WriteInt_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteReal_BF(void*, const int32_t*, const int32_t*, const double*);


cdef extern void WriteVM_BF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteVV_BF(void*, const int32_t*, const int32_t*, const int32_t*);



# Class DAT


cdef extern int32_t CreateDB_DAT(void*, const int32_t*, const void*, const void*, const void*);


cdef extern int32_t CreateXGD_DAT(void*, const void*, const int32_t*);


cdef extern void Destroy_DAT(void*, const int32_t*);


cdef extern void GetLST_DAT(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void RangeXYZ_DAT(void*, const int32_t*, double*, double*, double*, double*, double*, double*, int32_t*);



# Class DATALINKD


cdef extern int32_t CreateArcLYR_DATALINKD(void*, const void*);


cdef extern int32_t CreateArcLYREx_DATALINKD(void*, const void*, const int32_t*);


cdef extern int32_t CreateArcLYRFromTMP_DATALINKD(void*, const void*);


cdef extern int32_t CreateArcLYRFromTMPEx_DATALINKD(void*, const void*, const int32_t*);


cdef extern int32_t CreateBING_DATALINKD(void*, const int32_t*);


cdef extern void Destroy_DATALINKD(void*, const int32_t*);


cdef extern void GetExtents_DATALINKD(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void GetIPJ_DATALINKD(void*, const int32_t*, const int32_t*);



# Class DATAMINE


cdef extern void CreateVoxel_DATAMINE(void*, const void*, const void*, const int32_t*, const int32_t*, const void*);


cdef extern void NumericFieldLST_DATAMINE(void*, const void*, const int32_t*);



# Class DB

# Channel




cdef extern void CreateDup_DB(void*, const int32_t*, const void*);


cdef extern void CreateDupComp_DB(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t DupSymbAcross_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void EasyMakerSymb_DB(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void GetChanStr_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void GetChanVV_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetChanVVExpanded_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetIPJ_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetITR_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetRegSymb_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetRegSymbSetting_DB(void*, const int32_t*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void GetVaChanVV_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iBlobsMax_DB(void*, const int32_t*);


cdef extern int32_t iChansMax_DB(void*, const int32_t*);


cdef extern void IFormatChan_DB(void*, const int32_t*, const int32_t*, const double*, void*, const int32_t*);


cdef extern int32_t iGetChanArraySize_DB(void*, const int32_t*, const int32_t*);


cdef extern void IGetChanClass_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetChanDecimal_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetChanFormat_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetChanInt_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IGetChanLabel_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IGetChanName_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetChanProtect_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetChanType_DB(void*, const int32_t*, const int32_t*);


cdef extern void IGetChanUnit_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetChanWidth_DB(void*, const int32_t*, const int32_t*);


cdef extern void IGetName_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetRegSymbSetting_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void IGetSymbName_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iHaveITR_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t IiCoordPair_DB(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern int32_t iLinesMax_DB(void*, const int32_t*);


cdef extern int32_t iUsersMax_DB(void*, const int32_t*);


cdef extern void MakerSymb_DB(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void PutChanVV_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PutVaChanVV_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadBlobBF_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetChanReal_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetRegSymbSetting_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetAllChanProtect_DB(void*, const int32_t*, const int32_t*);


cdef extern void SetChanClass_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetChanDecimal_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetChanFormat_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetChanInt_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetChanLabel_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetChanName_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetChanProtect_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetChanReal_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetChanStr_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void SetChanUnit_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetChanWidth_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetITR_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetRegSymb_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetRegSymbSetting_DB(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void WriteBlobBF_DB(void*, const int32_t*, const int32_t*, const int32_t*);


# Control




cdef extern void Commit_DB(void*, const int32_t*);


cdef extern void Compact_DB(void*, const int32_t*);


cdef extern void Create_DB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void CreateComp_DB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void CreateEx_DB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void DelLine0_DB(void*, const int32_t*);


cdef extern void Destroy_DB(void*, const int32_t*);


cdef extern void Discard_DB(void*, const int32_t*);


cdef extern void Grow_DB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCanOpen_DB(void*, const void*, const void*, const void*);


cdef extern int32_t iCanOpenReadOnly_DB(void*, const void*, const void*, const void*);


cdef extern int32_t iCheck_DB(void*, const int32_t*);


cdef extern int32_t iIsEmpty_DB(void*, const int32_t*);


cdef extern int32_t iIsLineEmpty_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t Open_DB(void*, const void*, const void*, const void*);


cdef extern int32_t OpenReadOnly_DB(void*, const void*, const void*, const void*);


cdef extern void Repair_DB(void*, const void*);


cdef extern void Sync_DB(void*, const int32_t*);


# Data




cdef extern void CopyData_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGetColVA_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetChannelLength_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetFidIncr_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetFidStart_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetFid_DB(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void WindowVACh_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WindowVACh2_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# Line




cdef extern void SetLineSelection_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGetLineSelection_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t FirstSelLine_DB(void*, const int32_t*);


cdef extern void GetLineMapFid_DB(void*, const int32_t*, const int32_t*, double*, double*);


cdef extern int32_t GetSelect_DB(void*, const int32_t*);


cdef extern int32_t iCountSelLines_DB(void*, const int32_t*);


cdef extern int32_t iIsChanName_DB(void*, const void*);


cdef extern int32_t iIsChanValid_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iIsLineName_DB(void*, const void*);


cdef extern int32_t iIsLineValid_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iLineCategory_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iLineFlight_DB(void*, const int32_t*, const int32_t*);


cdef extern void ILineLabel_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*, const int32_t*);


cdef extern int32_t iLineNumber_DB(void*, const int32_t*, const int32_t*);


cdef extern void ILineNumber2_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iLineType_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iLineVersion_DB(void*, const int32_t*, const int32_t*);


cdef extern void ISetLineName_DB(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void ISetLineName2_DB(void*, const void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void LoadSelect_DB(void*, const int32_t*, const void*);


cdef extern int32_t NextSelLine_DB(void*, const int32_t*, const int32_t*);


cdef extern double rLineBearing_DB(void*, const int32_t*, const int32_t*);


cdef extern double rLineDate_DB(void*, const int32_t*, const int32_t*);


cdef extern void SaveSelect_DB(void*, const int32_t*, const void*);


cdef extern void Select_DB(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SetLineBearing_DB(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetLineDate_DB(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetLineFlight_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetLineMapFid_DB(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void SetLineNum_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetLineType_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetLineVer_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetSelect_DB(void*, const int32_t*, const int32_t*);


# META




cdef extern void GetMETA_DB(void*, const int32_t*, const int32_t*);


cdef extern void SetMETA_DB(void*, const int32_t*, const int32_t*);


# Symbols




cdef extern void ArrayLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void ArraySizeLST_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ChanLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void NormalChanLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void ClassChanLST_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ClassGroupLST_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t CreateSymb_DB(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateSymbEx_DB(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CSVChanLST_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void DeleteSymb_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t DupLineSymb_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t DupSymb_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t DupSymbNoLock_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t FindChan_DB(void*, const int32_t*, const void*);


cdef extern int32_t FindSymb_DB(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetChanOrderLST_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetXYZChanSymb_DB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iClassChanList_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t iExistChan_DB(void*, const int32_t*, const void*);


cdef extern int32_t iExistSymb_DB(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iValidSymb_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGetSymbLock_DB(void*, const int32_t*, const int32_t*);


cdef extern void IGetXYZChan_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iSymbList_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LineLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void LockSymb_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MaskChanLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void SelectedLineLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void SetChanOrderLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void SetXYZChan_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void StringChanLST_DB(void*, const int32_t*, const int32_t*);


cdef extern void SymbLST_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void UnLockAllSymb_DB(void*, const int32_t*);


cdef extern void UnLockSymb_DB(void*, const int32_t*, const int32_t*);


# VA Channels




cdef extern void AddAssociatedLoad_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AddComment_DB(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void AddIntComment_DB(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void AddRealComment_DB(void*, const int32_t*, const void*, const double*, const int32_t*);


cdef extern void AddTimeComment_DB(void*, const int32_t*, const void*, const int32_t*);


cdef extern void Associate_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AssociateAll_DB(void*, const int32_t*, const int32_t*);


cdef extern void AssociateClass_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void GenValidChanSymb_DB(void*, const void*, void*, const int32_t*);


cdef extern void GenValidLineSymb_DB(void*, const void*, void*, const int32_t*);


cdef extern void GetChanVA_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetVAScaling_DB(void*, const int32_t*, const int32_t*, double*, double*);


cdef extern void GetVAWindows_DB(void*, const int32_t*, const int32_t*, int32_t*, int32_t*);


cdef extern void SetVABaseCoordinateInfo_DB(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const void*, const int32_t*);


cdef extern void GetVABaseCoordinateInfo_DB(void*, const int32_t*, const int32_t*, int32_t*, double*, const int32_t*, void*, const int32_t*);


cdef extern void IGetGroupClass_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetInfo_DB(void*, const int32_t*, const int32_t*);


cdef extern void IGetVAProfColorFile_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IGetVAProfSectOption_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IGetVASectColorFile_DB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iIsAssociated_DB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iIsWholeplot_DB(void*, const int32_t*);


cdef extern void PutChanVA_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetGroupClass_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetVAProfColorFile_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetVAProfSectOption_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetVAScaling_DB(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void SetVASectColorFile_DB(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetVAWindows_DB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);




# Class DBREAD

# Create Methods




cdef extern int32_t Create_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateXY_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateXYZ_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_DBREAD(void*, const int32_t*);


cdef extern int32_t iAddChannel_DBREAD(void*, const int32_t*, const int32_t*);


# Data Access Methods




cdef extern int32_t GetVV_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetVA_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetVVx_DBREAD(void*, const int32_t*);


cdef extern int32_t GetVVy_DBREAD(void*, const int32_t*);


cdef extern int32_t GetVVz_DBREAD(void*, const int32_t*);


cdef extern int32_t iGetChanArraySize_DBREAD(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetNumberOfBlocksToProcess_DBREAD(void*, const int32_t*);


# Processing




cdef extern int32_t iGetNextBlock_DBREAD(void*, const int32_t*, int32_t*, int32_t*, int32_t*);




# Class DBWRITE

# Create Methods




cdef extern int32_t Create_DBWRITE(void*, const int32_t*);


cdef extern int32_t CreateXY_DBWRITE(void*, const int32_t*);


cdef extern int32_t CreateXYZ_DBWRITE(void*, const int32_t*);


cdef extern void Destroy_DBWRITE(void*, const int32_t*);


cdef extern int32_t iAddChannel_DBWRITE(void*, const int32_t*, const int32_t*);


# Data Access Methods




cdef extern int32_t GetDB_DBWRITE(void*, const int32_t*);


cdef extern int32_t GetVV_DBWRITE(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetVA_DBWRITE(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetVVx_DBWRITE(void*, const int32_t*);


cdef extern int32_t GetVVy_DBWRITE(void*, const int32_t*);


cdef extern int32_t GetVVz_DBWRITE(void*, const int32_t*);


cdef extern int32_t iGetChanArraySize_DBWRITE(void*, const int32_t*, const int32_t*);


# Processing




cdef extern void AddBlock_DBWRITE(void*, const int32_t*, const int32_t*);


cdef extern void Commit_DBWRITE(void*, const int32_t*);


cdef extern void TestFunc_DBWRITE(void*, const int32_t*, const int32_t*);




# Class DSEL


cdef extern int32_t Create_DSEL(void*);


cdef extern void DataSignificantFigures_DSEL(void*, const int32_t*, const double*);


cdef extern void Destroy_DSEL(void*, const int32_t*);


cdef extern void MetaQuery_DSEL(void*, const int32_t*, const void*);


cdef extern void PictureQuality_DSEL(void*, const int32_t*, const int32_t*);


cdef extern void RequestAllInfo_DSEL(void*, const int32_t*, const int32_t*);


cdef extern void SelectArea_DSEL(void*, const int32_t*, const int32_t*);


cdef extern void SelectRect_DSEL(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void SelectResolution_DSEL(void*, const int32_t*, const double*, const int32_t*);


cdef extern void SelectSize_DSEL(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetExtractAsDocument_DSEL(void*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_DSEL(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SpatialAccuracy_DSEL(void*, const int32_t*, const double*);



# Class EXT


cdef extern void GetInfo_EXT(void*, const void*, double*, double*, double*, double*, const int32_t*);



# Class GEO


cdef extern int32_t iCheckError_SYS(void*);


cdef extern int32_t iCheckTerminate_SYS(void*, int32_t*);


cdef extern void ShowError_GEO(void*);


cdef extern int32_t sGetError_GEO(void*, void*, int32_t, void*, int32_t, int32_t*);


cdef extern int32_t GetPtrVM_GEO(void*, const int32_t*);


cdef extern int32_t GetPtrVV_GEO(void*, const int32_t*);


cdef extern int32_t pGetInternalGXXPointer_GEO(void*, const int32_t*);


cdef extern int32_t sCheckTerminate_GEO(void*);


cdef extern void RegisterResourceTracking_GEO(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void UnregisterResourceTracking_GEO(void*, const int32_t*, const int32_t*, const int32_t*);



# Class GEOSOFT



# Class GEOSTRING


cdef extern int32_t Open_GEOSTRING(void*, const void*, const int32_t*);


cdef extern void Destroy_GEOSTRING(void*, const int32_t*);


cdef extern void GetIPJ_GEOSTRING(void*, const int32_t*, const int32_t*);


cdef extern void GetFeatures_GEOSTRING(void*, const int32_t*, const int32_t*);


cdef extern void GetSections_GEOSTRING(void*, const int32_t*, const int32_t*);


cdef extern void GetAllShapes_GEOSTRING(void*, const int32_t*, const int32_t*);


cdef extern void GetShapesForFeature_GEOSTRING(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetShapesForSection_GEOSTRING(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetShapesForFeatureAndSection_GEOSTRING(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void GetFeatureProperties_GEOSTRING(void*, const int32_t*, const void*, void*, const int32_t*, void*, const int32_t*, int32_t*, int32_t*, double*, double*, double*, int32_t*, int32_t*, int32_t*, double*, double*, int32_t*);


cdef extern void GetSectionProperties_GEOSTRING(void*, const int32_t*, const void*, void*, const int32_t*, void*, const int32_t*, int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetShapeProperties_GEOSTRING(void*, const int32_t*, const void*, void*, const int32_t*, void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class GIS


cdef extern int32_t Create_GIS(void*, const void*, const void*, const int32_t*);


cdef extern void CreateMap2D_GIS(void*, const int32_t*, const void*, const double*, const int32_t*, const int32_t*);


cdef extern void Destroy_GIS(void*, const int32_t*);


cdef extern void GetBPRModelsLST_GIS(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t GetIPJ_GIS(void*, const int32_t*);


cdef extern void GetMETA_GIS(void*, const int32_t*, const int32_t*);


cdef extern void GetRange_GIS(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t iDatamineType_GIS(void*, const void*);


cdef extern void IGetFileName_GIS(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iIsMIMapFile_GIS(void*, const void*);


cdef extern int32_t iIsMIRasterTabFile_GIS(void*, const void*);


cdef extern int32_t iIsMIRotatedRasterTabFile_GIS(void*, const void*);


cdef extern int32_t iIsSHPFile3D_GIS(void*, const int32_t*);


cdef extern int32_t iIsSHPFilePoint_GIS(void*, const int32_t*);


cdef extern int32_t iNumAttribs_GIS(void*, const int32_t*);


cdef extern int32_t iNumShapes_GIS(void*, const int32_t*);


cdef extern void IScanMIRasterTabFile_GIS(void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void LoadASCII_GIS(void*, const int32_t*, const int32_t*);


cdef extern void LoadGDB_GIS(void*, const int32_t*, const int32_t*);


cdef extern void LoadMAP_GIS(void*, const int32_t*, const int32_t*);


cdef extern void LoadMAPEx_GIS(void*, const int32_t*, const int32_t*, const void*);


cdef extern void LoadMetaGroupsMAP_GIS(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void LoadPLY_GIS(void*, const int32_t*, const int32_t*);


cdef extern void LoadShapesGDB_GIS(void*, const int32_t*, const int32_t*);


cdef extern void SetDmWireframePtFile_GIS(void*, const int32_t*, const void*);


cdef extern void SetIPJ_GIS(void*, const int32_t*, const int32_t*);


cdef extern void SetLST_GIS(void*, const int32_t*, const int32_t*);


cdef extern void SetMETA_GIS(void*, const int32_t*, const int32_t*);


cdef extern void SetTriangulationObjectIndex_GIS(void*, const int32_t*, const int32_t*);



# Class HGD


cdef extern int32_t Create_HGD(void*, const void*);


cdef extern void Destroy_HGD(void*, const int32_t*);


cdef extern void ExportIMG_HGD(void*, const int32_t*, const void*);


cdef extern void GetMETA_HGD(void*, const int32_t*, const int32_t*);


cdef extern int32_t hCreateIMG_HGD(void*, const int32_t*, const void*);


cdef extern void SetMETA_HGD(void*, const int32_t*, const int32_t*);



# Class HXYZ


cdef extern int32_t Create_HXYZ(void*, const void*);


cdef extern void Destroy_HXYZ(void*, const int32_t*);


cdef extern void GetMETA_HXYZ(void*, const int32_t*, const int32_t*);


cdef extern int32_t hCreateDB_HXYZ(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t hCreateSQL_HXYZ(void*, const void*, const void*, const void*, const void*, const int32_t*, const void*);


cdef extern void SetMETA_HXYZ(void*, const int32_t*, const int32_t*);



# Class IGRF


cdef extern void Calc_IGRF(void*, const int32_t*, const double*, const double*, const double*, double*, double*, double*);


cdef extern void CalcVV_IGRF(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_IGRF(void*, const double*, const int32_t*, const void*);


cdef extern void DateRange_IGRF(void*, const void*, double*, double*);


cdef extern void Destroy_IGRF(void*, const int32_t*);



# Class IMG


cdef extern void Average2_IMG(void*, const void*, const void*);


cdef extern void Copy_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateFile_IMG(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t CreateMem_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateNewFile_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t CreateOutFile_IMG(void*, const int32_t*, const void*, const int32_t*);


cdef extern void CreateProjected_IMG(void*, const int32_t*, const int32_t*);


cdef extern void CreateProjected2_IMG(void*, const int32_t*, const int32_t*, const double*);


cdef extern void CreateProjected3_IMG(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void Destroy_IMG(void*, const int32_t*);


cdef extern int32_t GethPG_IMG(void*, const int32_t*);


cdef extern void GetInfo_IMG(void*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern void GetIPJ_IMG(void*, const int32_t*, const int32_t*);


cdef extern void GetMETA_IMG(void*, const int32_t*, const int32_t*);


cdef extern void GetPG_IMG(void*, const int32_t*, const int32_t*);


cdef extern void GetProjectedCellSize_IMG(void*, const int32_t*, const int32_t*, double*);


cdef extern void GetTR_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iElementType_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iEType_IMG(void*, const int32_t*);


cdef extern int32_t iGetDefITR_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iIsColour_IMG(void*, const int32_t*);


cdef extern int32_t iIsValidIMGFile_IMG(void*, const void*);


cdef extern int32_t iIsValidIMGFileEx_IMG(void*, const void*, void*, const int32_t*);


cdef extern int32_t iNE_IMG(void*, const int32_t*);


cdef extern void Inherit_IMG(void*, const int32_t*, const int32_t*, const double*);


cdef extern void InheritIMG_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iNV_IMG(void*, const int32_t*);


cdef extern int32_t iNX_IMG(void*, const int32_t*);


cdef extern int32_t iNY_IMG(void*, const int32_t*);


cdef extern int32_t iQuery_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iQueryKX_IMG(void*, const int32_t*);


cdef extern int32_t iSetDefITR_IMG(void*, const int32_t*, const int32_t*);


cdef extern int32_t iUserPreferenceToPlotAsColourShadedGrid_IMG(void*);


cdef extern void LoadIMG_IMG(void*, const int32_t*, const int32_t*);


cdef extern void LoadIntoPager_IMG(void*, const int32_t*);


cdef extern void OptKX_IMG(void*, const int32_t*, const int32_t*);


cdef extern void ReadV_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadX_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadY_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RefreshGI_IMG(void*, const void*);


cdef extern void Relocate_IMG(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void Report_IMG(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void ReportCSV_IMG(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetZ_IMG(void*, const int32_t*, const double*, const double*);


cdef extern double rQuery_IMG(void*, const int32_t*, const int32_t*);


cdef extern void SetGridUnchanged_IMG(void*, const int32_t*);


cdef extern void SetInfo_IMG(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetIPJ_IMG(void*, const int32_t*, const int32_t*);


cdef extern void SetMETA_IMG(void*, const int32_t*, const int32_t*);


cdef extern void SetPG_IMG(void*, const int32_t*, const int32_t*);


cdef extern void SetTR_IMG(void*, const int32_t*, const int32_t*);


cdef extern void Sync_IMG(void*, const void*);


cdef extern void WriteV_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteX_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteY_IMG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetRealParameter_IMG(void*, const int32_t*, const void*, const double*);


cdef extern double rGetRealParameter_IMG(void*, const int32_t*, const void*);



# Class IMU


cdef extern void AggToGeoColor_IMU(void*, const int32_t*, const void*, const int32_t*, const double*);


cdef extern int32_t CRC_IMU(void*, const int32_t*, const int32_t*);


cdef extern int32_t CRCGrid_IMU(void*, const void*, const int32_t*);


cdef extern int32_t CRCGridInexact_IMU(void*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CRCInexact_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExportGridWithoutDataSectionXML_IMU(void*, const void*, int32_t*, const void*);


cdef extern void ExportGridXML_IMU(void*, const void*, int32_t*, const void*);


cdef extern void ExportRawXML_IMU(void*, const int32_t*, int32_t*, const void*);


cdef extern void ExportXML_IMU(void*, const int32_t*, int32_t*, const void*);


cdef extern void GetZVV_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetZPeaksVV_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridAdd_IMU(void*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*);


cdef extern void GridAGC_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void GridBool_IMU(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridEdge_IMU(void*, const void*, const int32_t*, const int32_t*);


cdef extern void GridEdgePLY_IMU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridExpand_IMU(void*, const int32_t*, const void*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridExpFill_IMU(void*, const void*, const void*, const double*, const int32_t*);


cdef extern void GridFill_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void GridFilt_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void GridHead_IMU(void*, const void*, const double*, const double*, const double*, const double*, const double*);


cdef extern void GridInFill_IMU(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void GridMask_IMU(void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void GridPeak_IMU(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridPLY_IMU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridPLYEx_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridReprojectAndWindow_IMU(void*, const void*, const void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void GridResample_IMU(void*, const void*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void GridResize_IMU(void*, const void*, const void*);


cdef extern void GridShad_IMU(void*, const void*, const void*, double*, double*, double*);


cdef extern void GridST_IMU(void*, const void*, const int32_t*);


cdef extern void GridStat_IMU(void*, const void*, int32_t*, int32_t*, int32_t*, double*, double*, int32_t*, double*, double*, double*, double*, double*);


cdef extern void GridStatComp_IMU(void*, const void*, int32_t*, int32_t*, int32_t*, double*, double*, int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GridStatExt_IMU(void*, const void*, const int32_t*, int32_t*, int32_t*, double*, double*, double*, double*);


cdef extern void GridStatTrend_IMU(void*, const void*, int32_t*, double*, double*, double*);


cdef extern void GridStatTrendExt_IMU(void*, const void*, int32_t*, int32_t*, double*, double*, const int32_t*);


cdef extern double rSlopeStandardDeviation_IMU(void*, const int32_t*);


cdef extern void GridStitch_IMU(void*, const void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void GridStitchCtl_IMU(void*, const void*);


cdef extern void GridTiff_IMU(void*, const void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*);


cdef extern void GridTrnd_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridTrns_IMU(void*, const void*, const int32_t*);


cdef extern void GridVD_IMU(void*, const int32_t*, const int32_t*);


cdef extern void GridVol_IMU(void*, const int32_t*, const double*, const double*, double*, double*, double*);


cdef extern void GridWind_IMU(void*, const int32_t*, const void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void GridWind2_IMU(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void GridXYZ_IMU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGridType_IMU(void*, const void*);


cdef extern void MakeMITabFile_IMU(void*, const void*);


cdef extern void MakeMITabfromGrid_IMU(void*, const void*);


cdef extern void MakeMITabfromMap_IMU(void*, const void*);


cdef extern int32_t Mosaic_IMU(void*, const void*, const void*, const int32_t*, const double*);


cdef extern void PeakSize_IMU(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void PeakSize2_IMU(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PigeonHole_IMU(void*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern void Profile_IMU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ProfileVV_IMU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RangeGrids_IMU(void*, const void*, const int32_t*, double*, double*, double*, double*);


cdef extern void RangeLL_IMU(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void StatWindow_IMU(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void UpdatePLY_IMU(void*, const int32_t*, const int32_t*);



# Class IPJ


cdef extern void _ClearWarp_IPJ(void*, const int32_t*);


cdef extern void _MakeGeographic_IPJ(void*, const int32_t*);


cdef extern void _MakeWGS84_IPJ(void*, const int32_t*);


cdef extern void _SetUnits_IPJ(void*, const int32_t*, const double*, const void*);


cdef extern void AddExaggWarp_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void AddLogWarp_IPJ(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AddMatrixWarp_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void AddWarp_IPJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ClearCoordinateSystem_IPJ(void*, const int32_t*);


cdef extern void ClearOrientation_IPJ(void*, const int32_t*);


cdef extern void ConvertOrientationWarpVV_IPJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Copy_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void CopyProjection_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_IPJ(void*);


cdef extern int32_t CreateS_IPJ(void*, const int32_t*);


cdef extern int32_t CreateXML_IPJ(void*, const void*);


cdef extern void Destroy_IPJ(void*, const int32_t*);


cdef extern void Get3DView_IPJ(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void Get3DViewEx_IPJ(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*, int32_t*, int32_t*);


cdef extern void GetCrookedSectionViewVVs_IPJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern void GetList_IPJ(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetOrientationInfo_IPJ(void*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern void GetPlaneEquation_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetPlaneEquation2_IPJ(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t iCompareDatums_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iConvertWarp_IPJ(void*, const int32_t*, double*, double*, double*, const int32_t*);


cdef extern int32_t iConvertWarpVV_IPJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCoordinateSystemsAreTheSame_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iCoordinateSystemsAreTheSameWithinASmallTolerance_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void IGetDisplayName_IPJ(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetESRI_IPJ(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetGXF_IPJ(void*, const int32_t*, void*, void*, void*, void*, void*, const int32_t*);


cdef extern void IGetMICoordSys_IPJ(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetName_IPJ(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetOrientation_IPJ(void*, const int32_t*);


cdef extern void IGetOrientationName_IPJ(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetUnits_IPJ(void*, const int32_t*, double*, void*, const int32_t*);


cdef extern void IGetXML_IPJ(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iHasProjection_IPJ(void*, const int32_t*);


cdef extern int32_t iIs3DInverted_IPJ(void*, const int32_t*);


cdef extern int32_t iIs3DInvertedAngles_IPJ(void*, const int32_t*);


cdef extern int32_t iIsGeographic_IPJ(void*, const int32_t*);


cdef extern int32_t iOrientationsAreTheSame_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iOrientationsAreTheSameWithinASmallTolerance_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iHasSectionOrientation_IPJ(void*, const int32_t*);


cdef extern int32_t iProjectionTypeIsFullySupported_IPJ(void*, const int32_t*);


cdef extern int32_t iSetGXF_IPJ(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*);


cdef extern int32_t iSourceType_IPJ(void*, const int32_t*);


cdef extern int32_t iSupportDatumTransform_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void IUnitName_IPJ(void*, const double*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iWarped_IPJ(void*, const int32_t*);


cdef extern int32_t iWarpsAreTheSame_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iWarpsAreTheSameWithinASmallTolerance_IPJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t iWarpType_IPJ(void*, const int32_t*);


cdef extern void MakeProjected_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void NewBoxResolution_IPJ(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, double*, double*, double*);


cdef extern void Read_IPJ(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern double rGetMethodParm_IPJ(void*, const int32_t*, const int32_t*);


cdef extern double rGetNorthAzimuth_IPJ(void*, const int32_t*, const double*, const double*);


cdef extern double rUnitScale_IPJ(void*, const void*, const double*);


cdef extern void Serial_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void SerialFGDCXML_IPJ(void*, const int32_t*, const void*);


cdef extern void SerialISOXML_IPJ(void*, const int32_t*, const void*);


cdef extern void SerialXML_IPJ(void*, const int32_t*, const void*);


cdef extern void Set3DInverted_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void Set3DInvertedAngles_IPJ(void*, const int32_t*, const int32_t*);


cdef extern void Set3DView_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Set3DViewEx_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void Set3DViewFromAxes_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetCrookedSectionView_IPJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetDepthSectionView_IPJ(void*, const int32_t*, const double*);


cdef extern void SetESRI_IPJ(void*, const int32_t*, const void*);


cdef extern void SetGXF_IPJ(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*);


cdef extern void SetMethodParm_IPJ(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetMICoordSys_IPJ(void*, const int32_t*, const void*, const void*);


cdef extern void SetNormalSectionView_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetPlanView_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void SetSectionView_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetWMSCoordSys_IPJ(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*);


cdef extern void SetXML_IPJ(void*, const int32_t*, const void*);


cdef extern void Get3DMatrixOrientation_IPJ(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void Set3DMatrixOrientation_IPJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ReprojectSectionGrid_IPJ(void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*);



# Class ITR


cdef extern void ChangeBrightness_ITR(void*, const int32_t*, const double*);


cdef extern void ColorVV_ITR(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Copy_ITR(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_ITR(void*);


cdef extern int32_t CreateFile_ITR(void*, const void*);


cdef extern int32_t CreateIMG_ITR(void*, const int32_t*, const void*, const int32_t*, const double*);


cdef extern int32_t CreateMap_ITR(void*, const int32_t*, const void*);


cdef extern int32_t CreateS_ITR(void*, const int32_t*);


cdef extern void Destroy_ITR(void*, const int32_t*);


cdef extern void EqualArea_ITR(void*, const int32_t*, const int32_t*, const double*);


cdef extern void GetDataLimits_ITR(void*, const int32_t*, double*, double*);


cdef extern int32_t GetREG_ITR(void*, const int32_t*);


cdef extern void GetZoneColor_ITR(void*, const int32_t*, const int32_t*, int32_t*);


cdef extern int32_t iColorValue_ITR(void*, const int32_t*, const double*);


cdef extern int32_t iGetSize_ITR(void*, const int32_t*);


cdef extern int32_t iGetZoneModelType_ITR(void*, const int32_t*);


cdef extern void Linear_ITR(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void LoadA_ITR(void*, const int32_t*, const void*);


cdef extern void LogLinear_ITR(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void Normal_ITR(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void PowerZone_ITR(void*, const int32_t*, const int32_t*);


cdef extern double rGetBrightness_ITR(void*, const int32_t*);


cdef extern double rGetZoneValue_ITR(void*, const int32_t*, const int32_t*);


cdef extern void SaveA_ITR(void*, const int32_t*, const void*);


cdef extern void SaveFile_ITR(void*, const int32_t*, const void*);


cdef extern void Serial_ITR(void*, const int32_t*, const int32_t*);


cdef extern void SetAggMap_ITR(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SetBrightContrast_ITR(void*, const int32_t*, const double*, const double*);


cdef extern void SetColorModel_ITR(void*, const int32_t*, const int32_t*);


cdef extern void SetDataLimits_ITR(void*, const int32_t*, const double*, const double*);


cdef extern void SetSize_ITR(void*, const int32_t*, const int32_t*);


cdef extern void SetZoneColor_ITR(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetZoneValue_ITR(void*, const int32_t*, const int32_t*, const double*);



# Class LAYOUT


cdef extern void CalculateRects_LAYOUT(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void ClearAll_LAYOUT(void*, const int32_t*);


cdef extern void ClearConstraints_LAYOUT(void*, const int32_t*);


cdef extern int32_t Create_LAYOUT(void*, const int32_t*, const void*);


cdef extern void Destroy_LAYOUT(void*, const int32_t*);


cdef extern void GetRectangle_LAYOUT(void*, const int32_t*, const int32_t*, double*, double*, double*, double*);


cdef extern void GetRectName_LAYOUT(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iAddConstraint_LAYOUT(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern int32_t iAddRectangle_LAYOUT(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern int32_t iNumRectangles_LAYOUT(void*, const int32_t*);


cdef extern void SetRectangle_LAYOUT(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void SetRectangleName_LAYOUT(void*, const int32_t*, const int32_t*, const void*);



# Class LL2


cdef extern int32_t Create_LL2(void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Destroy_LL2(void*, const int32_t*);


cdef extern void Save_LL2(void*, const int32_t*, const void*);


cdef extern void SetRow_LL2(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class LPT


cdef extern int32_t Create_LPT(void*);


cdef extern void Destroy_LPT(void*, const int32_t*);


cdef extern void GetLST_LPT(void*, const int32_t*, const int32_t*);


cdef extern void GetStandardLST_LPT(void*, const int32_t*, const int32_t*);



# Class LST


cdef extern void AddItem_LST(void*, const int32_t*, const void*, const void*);


cdef extern void AddSymbItem_LST(void*, const int32_t*, const void*, const int32_t*);


cdef extern void AddUniqueItem_LST(void*, const int32_t*, const void*, const void*);


cdef extern void Append_LST(void*, const int32_t*, const int32_t*);


cdef extern int32_t AssayChannel_LST(void*);


cdef extern void Clear_LST(void*, const int32_t*);


cdef extern void ConvertFromCSVString_LST(void*, const int32_t*, const void*);


cdef extern void Copy_LST(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_LST(void*, const int32_t*);


cdef extern int32_t CreateS_LST(void*, const int32_t*);


cdef extern void DelItem_LST(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_LST(void*, const int32_t*);


cdef extern void FindItems_LST(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GtItem_LST(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void GtSymbItem_LST(void*, const int32_t*, const int32_t*, void*, const int32_t*, int32_t*);


cdef extern void IConvertToCSVString_LST(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iFindItem_LST(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t iFindItemMask_LST(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t iGetInt_LST(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void InsertItem_LST(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern int32_t iSize_LST(void*, const int32_t*);


cdef extern void LoadCSV_LST(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void LoadFile_LST(void*, const int32_t*, const void*);


cdef extern void Resource_LST(void*, const int32_t*, const void*);


cdef extern double rGetReal_LST(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SaveFile_LST(void*, const int32_t*, const void*);


cdef extern void SelectCSVStringItems_LST(void*, const int32_t*, const void*, const int32_t*);


cdef extern void Serial_LST(void*, const int32_t*, const int32_t*);


cdef extern void SetItem_LST(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void Sort_LST(void*, const int32_t*, const int32_t*, const int32_t*);



# Class LTB


cdef extern void AddRecord_LTB(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t Contract_LTB(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_LTB(void*, const void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t CreateCrypt_LTB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern int32_t CreateEx_LTB(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void DeleteRecord_LTB(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_LTB(void*, const int32_t*);


cdef extern void GetConLST_LTB(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void GetLST_LTB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetLST2_LTB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iFields_LTB(void*, const int32_t*);


cdef extern int32_t iFindField_LTB(void*, const int32_t*, const void*);


cdef extern int32_t iFindKey_LTB(void*, const int32_t*, const void*);


cdef extern void IGetField_LTB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetInt_LTB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IGetString_LTB(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IGetEnglishString_LTB(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iRecords_LTB(void*, const int32_t*);


cdef extern int32_t iSearch_LTB(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t Merge_LTB(void*, const int32_t*, const int32_t*);


cdef extern double rGetReal_LTB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Save_LTB(void*, const int32_t*, const void*);


cdef extern void SaveCrypt_LTB(void*, const int32_t*, const void*, const void*);


cdef extern void SetInt_LTB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetReal_LTB(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_LTB(void*, const int32_t*, const int32_t*, const int32_t*, const void*);



# Class MAP

# Export




cdef extern void ExportAllInView_MAP(void*, const int32_t*, const void*, const void*, const double*, const double*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ExportAllRaster_MAP(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ExportAreaInView_MAP(void*, const int32_t*, const void*, const void*, const double*, const double*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const void*, const void*);


cdef extern void ExportAreaRaster_MAP(void*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void RenderBitmap_MAP(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const void*, const int32_t*);


# Miscellaneous




cdef extern void AGGList_MAP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AGGListEx_MAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Clean_MAP(void*, const int32_t*);


cdef extern void Commit_MAP(void*, const int32_t*);


cdef extern void CopyMapToView_MAP(void*, const int32_t*, const void*, const void*);


cdef extern void CRCMap_MAP(void*, const int32_t*, int32_t*, const void*);


cdef extern int32_t Create_MAP(void*, const void*, const int32_t*);


cdef extern int32_t App_Current_MAP(void*);


cdef extern void DeleteView_MAP(void*, const int32_t*, const void*);


cdef extern void Destroy_MAP(void*, const int32_t*);


cdef extern void Discard_MAP(void*, const int32_t*);


cdef extern void DupMap_MAP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GetLPT_MAP(void*, const int32_t*);


cdef extern void GetMapSize_MAP(void*, const int32_t*, double*, double*, double*, double*);


cdef extern int32_t GetMETA_MAP(void*, const int32_t*);


cdef extern int32_t GetREG_MAP(void*, const int32_t*);


cdef extern void GroupList_MAP(void*, const int32_t*, const int32_t*);


cdef extern void GroupListEx_MAP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDuplicateView_MAP(void*, const int32_t*, const void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t iExistView_MAP(void*, const int32_t*, const void*);


cdef extern void IGetClassName_MAP(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void IGetFileName_MAP(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetMapName_MAP(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iPackedFiles_MAP(void*, const int32_t*);


cdef extern void IUnPackFilesEx_MAP(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IUnPackFilesToFolder_MAP(void*, const int32_t*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void PackFiles_MAP(void*, const int32_t*);


cdef extern void Render_MAP(void*, const int32_t*, const void*);


cdef extern void ResizeAll_MAP(void*, const int32_t*);


cdef extern void ResizeAllEx_MAP(void*, const int32_t*, const int32_t*);


cdef extern double rGetMapScale_MAP(void*, const int32_t*);


cdef extern void SaveAsMXD_MAP(void*, const int32_t*, const void*);


cdef extern void SetClassName_MAP(void*, const int32_t*, const void*, const void*);


cdef extern void App_SetCurrent_MAP(void*, const int32_t*);


cdef extern void SetMapName_MAP(void*, const int32_t*, const void*);


cdef extern void SetMapScale_MAP(void*, const int32_t*, const double*);


cdef extern void SetMapSize_MAP(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void SetMETA_MAP(void*, const int32_t*, const int32_t*);


cdef extern void SetREG_MAP(void*, const int32_t*, const int32_t*);


cdef extern void Sync_MAP(void*, const void*);


cdef extern void UnPackFiles_MAP(void*, const int32_t*);


cdef extern void ViewList_MAP(void*, const int32_t*, const int32_t*);


cdef extern void ViewListEx_MAP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GetDataProj_MAP(void*, const int32_t*);




# Class MAPL


cdef extern int32_t Create_MAPL(void*, const void*, const void*, const int32_t*);


cdef extern int32_t CreateREG_MAPL(void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void Destroy_MAPL(void*, const int32_t*);


cdef extern void Process_MAPL(void*, const int32_t*, const int32_t*);


cdef extern void ReplaceString_MAPL(void*, const int32_t*, const void*, const void*);



# Class MAPTEMPLATE

# Content Manipulation Methods




cdef extern void GetTmpCopy_MAPTEMPLATE(void*, const int32_t*, void*, const int32_t*);


cdef extern void UpdateFromTmpCopy_MAPTEMPLATE(void*, const int32_t*, const void*);


# File Methods




cdef extern void Commit_MAPTEMPLATE(void*, const int32_t*);


cdef extern int32_t Create_MAPTEMPLATE(void*, const void*, const void*, const int32_t*);


cdef extern void Destroy_MAPTEMPLATE(void*, const int32_t*);


cdef extern void Discard_MAPTEMPLATE(void*, const int32_t*);


cdef extern void GetFileName_MAPTEMPLATE(void*, const int32_t*, void*, const int32_t*);


# Map Making




cdef extern void CreateMap_MAPTEMPLATE(void*, const int32_t*, const void*, const void*);


# Render/Preview




cdef extern void Refresh_MAPTEMPLATE(void*, const int32_t*);


cdef extern void RenderPreview_MAPTEMPLATE(void*, const int32_t*, int32_t, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RenderPreviewMapProduction_MAPTEMPLATE(void*, const int32_t*, int32_t, int32_t*, int32_t*, int32_t*, int32_t*);




# Class MATH


cdef extern void CrossProduct_MATH(void*, const double*, const double*, const double*, const double*, const double*, const double*, double*, double*, double*);


cdef extern int32_t iAbs_MATH(void*, const int32_t*);


cdef extern int32_t iAnd_MATH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iMod_MATH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iOr_MATH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iRound_MATH(void*, const double*);


cdef extern int32_t iXor_MATH(void*, const int32_t*, const int32_t*);


cdef extern void NicerLogScale_MATH(void*, double*, double*, const int32_t*);


cdef extern void NicerScale_MATH(void*, double*, double*, double*, int32_t*);


cdef extern void Normalise3D_MATH(void*, double*, double*, double*);


cdef extern double rAbs_MATH(void*, const double*);


cdef extern double rArcCos_MATH(void*, const double*);


cdef extern double rArcSin_MATH(void*, const double*);


cdef extern double rArcTan_MATH(void*, const double*);


cdef extern double rArcTan2_MATH(void*, const double*, const double*);


cdef extern double rCeil_MATH(void*, const double*);


cdef extern double rCos_MATH(void*, const double*);


cdef extern double rDotProduct3D_MATH(void*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern double rExp_MATH(void*, const double*);


cdef extern double rFloor_MATH(void*, const double*);


cdef extern double rHypot_MATH(void*, const double*, const double*);


cdef extern double rLambdaTrans_MATH(void*, const double*, const double*);


cdef extern double rLambdaTransRev_MATH(void*, const double*, const double*);


cdef extern double rLog_MATH(void*, const double*);


cdef extern double rLog10_MATH(void*, const double*);


cdef extern double rLogZ_MATH(void*, const double*, const int32_t*, const double*);


cdef extern double rMod_MATH(void*, const double*, const double*);


cdef extern void RotateVector_MATH(void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, double*, double*, double*);


cdef extern double rPow_MATH(void*, const double*, const double*);


cdef extern double rRand_MATH(void*);


cdef extern double rRound_MATH(void*, const double*, const int32_t*);


cdef extern double rSign_MATH(void*, const double*, const double*);


cdef extern double rSin_MATH(void*, const double*);


cdef extern double rSqrt_MATH(void*, const double*);


cdef extern double rTan_MATH(void*, const double*);


cdef extern double rUnLogZ_MATH(void*, const double*, const int32_t*, const double*);


cdef extern void SRand_MATH(void*);



# Class META

# Attribute




cdef extern int32_t CreateAttrib_META(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void DeleteAttrib_META(void*, const int32_t*, const int32_t*);


# Browser




cdef extern void SetAttributeEditable_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAttributeVisible_META(void*, const int32_t*, const int32_t*, const int32_t*);


# Class




cdef extern int32_t CreateClass_META(void*, const int32_t*, const void*, const int32_t*);


cdef extern void DeleteClass_META(void*, const int32_t*, const int32_t*);


# Core




cdef extern void Copy_META(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_META(void*);


cdef extern int32_t CreateS_META(void*, const int32_t*);


cdef extern void Destroy_META(void*, const int32_t*);


cdef extern void Serial_META(void*, const int32_t*, const int32_t*);


# Get Data




cdef extern int32_t FindData_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetAttribBool_META(void*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern void GetAttribEnum_META(void*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern void GetAttribInt_META(void*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern void GetAttribReal_META(void*, const int32_t*, const int32_t*, const int32_t*, double*);


cdef extern void IGetAttribString_META(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iHasValue_META(void*, const int32_t*, const int32_t*, const int32_t*);


# Import/Export




cdef extern void ExportTableCSV_META(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportTableCSV_META(void*, const int32_t*, const int32_t*, const void*);


cdef extern void WriteText_META(void*, const int32_t*, const int32_t*);


# Item




cdef extern void DeleteAllItems_META(void*, const int32_t*, const int32_t*);


cdef extern void DeleteItem_META(void*, const int32_t*, const int32_t*);


cdef extern int32_t hCreatItem_META(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t hGetNextItem_META(void*, const int32_t*, const int32_t*, const int32_t*);


# Object




cdef extern void GetAttribOBJ_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAttribOBJ_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# Set Data




cdef extern void SetAttribBool_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAttribEnum_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAttribInt_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAttribReal_META(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetAttribString_META(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void SetEmptyAttrib_META(void*, const int32_t*, const int32_t*, const int32_t*);


# Transfer




cdef extern int32_t hCopyAcrossAttribute_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t hCopyAcrossClass_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t hCopyAcrossData_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t hCopyAcrossItem_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t hCopyAcrossType_META(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MoveDatasAcross_META(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# Type




cdef extern int32_t CreateType_META(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void DeleteData_META(void*, const int32_t*, const int32_t*);


cdef extern void DeleteType_META(void*, const int32_t*, const int32_t*);


# UMN




cdef extern void IGetObjName_META(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t ResolveUMN_META(void*, const int32_t*, const void*);




# Class MVIEW

# 3D Entity




cdef extern void Box3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void CRCView_MVIEW(void*, const int32_t*, int32_t*, const void*);


cdef extern void CRCViewGroup_MVIEW(void*, const int32_t*, const void*, int32_t*, const void*);


cdef extern void Cylinder3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void DrawObject3D_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DrawSurface3DEx_MVIEW(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DrawSurface3DFromFile_MVIEW(void*, const int32_t*, const void*, const void*);


cdef extern void FontWeightLST_MVIEW(void*, const int32_t*);


cdef extern void GetAGGFileNames_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t IGetMeta_MVIEW(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void MeasureText_MVIEW(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern void Point3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void PolyLine3D_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RelocateGroup_MVIEW(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void SetMeta_MVIEW(void*, const int32_t*, const void*, const int32_t*, const void*);


cdef extern void Sphere3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void UpdateMETAfromGroup_MVIEW(void*, const int32_t*, const void*, const int32_t*);


# 3D Plane




cdef extern void DeletePlane_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetPlaneClipPLY_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetPlaneEquation_MVIEW(void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetViewPlaneEquation_MVIEW(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t iCreatePlane_MVIEW(void*, const int32_t*, const void*);


cdef extern int32_t iFindPlane_MVIEW(void*, const int32_t*, const void*);


cdef extern void IGetDefPlane_MVIEW(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iIsView3D_MVIEW(void*, const int32_t*);


cdef extern int32_t iIsSection_MVIEW(void*, const int32_t*);


cdef extern void ListPlaneGroups_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ListPlanes_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetAllGroupsToPlane_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetAllNewGroupsToPlane_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetDefPlane_MVIEW(void*, const int32_t*, const void*);


cdef extern void SetGroupToPlane_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetH3DN_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetPlaneClipPLY_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetPlaneEquation_MVIEW(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetPlaneSurface_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetPlaneSurfInfo_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


# 3D Rendering 2D




cdef extern void DefinePlane3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void DefineViewerAxis3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void DefineViewerPlane3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*);


# Clipping




cdef extern void _ClipPolyEx_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void _ClipRectEx_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void ClipClear_MVIEW(void*, const int32_t*);


cdef extern void ClipGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void ClipMarkedGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void ClipPoly_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ClipRect_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void DeleteExtClipPLY_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void ExtClipPLYList_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void GetClipPLY_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void GetExtClipPLY_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetGroupExtClipPLY_MVIEW(void*, const int32_t*, const void*, int32_t*);


cdef extern void GetPLY_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void GroupClipMode_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void IGetNameExtClipPLY_MVIEW(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iNumExtClipPLY_MVIEW(void*, const int32_t*);


cdef extern int32_t iSetExtClipPLY_MVIEW(void*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void SetClipPLY_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetGroupExtClipPLY_MVIEW(void*, const int32_t*, const void*, const int32_t*);


# Color




cdef extern void Color2RGB_MVIEW(void*, const int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void ColorDescr_MVIEW(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iColor_MVIEW(void*, const void*);


cdef extern int32_t iColorCMY_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iColorHSV_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iColorRGB_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


# Drawing Attribute




cdef extern void ClipMode_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void FillColor_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void LineColor_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void LineSmooth_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void LineStyle_MVIEW(void*, const int32_t*, const int32_t*, const double*);


cdef extern void LineThick_MVIEW(void*, const int32_t*, const double*);


cdef extern void PatAngle_MVIEW(void*, const int32_t*, const double*);


cdef extern void PatDensity_MVIEW(void*, const int32_t*, const double*);


cdef extern void PatNumber_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void PatSize_MVIEW(void*, const int32_t*, const double*);


cdef extern void PatStyle_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void PatThick_MVIEW(void*, const int32_t*, const double*);


cdef extern void SymbAngle_MVIEW(void*, const int32_t*, const double*);


cdef extern void SymbColor_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SymbFillColor_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SymbFont_MVIEW(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SymbNumber_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SymbSize_MVIEW(void*, const int32_t*, const double*);


cdef extern void TextAngle_MVIEW(void*, const int32_t*, const double*);


cdef extern void TextColor_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void TextFont_MVIEW(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TextRef_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void TextSize_MVIEW(void*, const int32_t*, const double*);


cdef extern void Transparency_MVIEW(void*, const int32_t*, const double*);


cdef extern void ZValue_MVIEW(void*, const int32_t*, const double*);


# Drawing Entity




cdef extern void Arc_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Chord_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ClassifiedSymbols_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const void*, const void*, const void*);


cdef extern void ComplexPolygon_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Ellipse_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Line_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void LineVV_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void PolygonDm_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolygonPLY_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void PolyLine_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyLineDm_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyWrap_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Rectangle_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void Segment_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SizeSymbols_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Symbol_MVIEW(void*, const int32_t*, const double*, const double*);


cdef extern void Symbols_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SymbolsITR_MVIEW(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Text_MVIEW(void*, const int32_t*, const void*, const double*, const double*);


# Drawing Object




cdef extern void Aggregate_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ChangeLineMessage_MVIEW(void*, const int32_t*, const void*);


cdef extern void ColSymbol_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern void DATALINKD_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void EasyMaker_MVIEW(void*, const int32_t*, const void*, const void*);


cdef extern void EMFObject_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const void*);


cdef extern void ExternalStringObject_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const void*, const void*, const void*);


cdef extern void Link_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void Maker_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const void*, const void*);


cdef extern void Meta_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern void VOXD_MVIEW(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t GetVOXD_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void DrawVectorVoxelVectors_MVIEW(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void DrawVectors3D_MVIEW(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


# Group Methods




cdef extern void CopyMarkedGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void CopyRawMarkedGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern int32_t CRCGroup_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern void DeleteGroup_MVIEW(void*, const int32_t*, const void*);


cdef extern void DelMarkedGroups_MVIEW(void*, const int32_t*);


cdef extern void GetGroupExtent_MVIEW(void*, const int32_t*, const void*, double*, double*, double*, double*, const int32_t*);


cdef extern void GetGroupTransparency_MVIEW(void*, const int32_t*, const void*, double*);


cdef extern void GroupToPLY_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern void HideMarkedGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void HideShadow2DInterpretations_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern int32_t iExistGroup_MVIEW(void*, const int32_t*, const void*);


cdef extern void IGenNewGroupName_MVIEW(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern int32_t iIsGroup_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iIsGroupEmpty_MVIEW(void*, const int32_t*, const void*);


cdef extern int32_t iIsMovable_MVIEW(void*, const int32_t*);


cdef extern int32_t iIsVisible_MVIEW(void*, const int32_t*);


cdef extern int32_t iListGroups_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iRenderOrder_MVIEW(void*, const int32_t*);


cdef extern void MarkAllGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void MarkEmptyGroups_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void MarkGroup_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern void MoveGroupBackward_MVIEW(void*, const int32_t*, const void*);


cdef extern void MoveGroupForward_MVIEW(void*, const int32_t*, const void*);


cdef extern void MoveGroupToBack_MVIEW(void*, const int32_t*, const void*);


cdef extern void MoveGroupToFront_MVIEW(void*, const int32_t*, const void*);


cdef extern void RenameGroup_MVIEW(void*, const int32_t*, const void*, const void*);


cdef extern void SetGroupMoveable_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SetGroupTransparency_MVIEW(void*, const int32_t*, const void*, const double*);


cdef extern void SetMarkMoveable_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetMovability_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetRenderOrder_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetVisibility_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void StartGroup_MVIEW(void*, const int32_t*, const void*, const int32_t*);


# Projection




cdef extern void _SetWorkingIPJ_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void ClearESRILDTs_MVIEW(void*, const int32_t*);


cdef extern int32_t iIsProjectionEmpty_MVIEW(void*, const int32_t*);


cdef extern void GetIPJ_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void GetUserIPJ_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void ModePJ_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern double rNorth_MVIEW(void*, const int32_t*);


cdef extern void SetIPJ_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void SetUserIPJ_MVIEW(void*, const int32_t*, const int32_t*);


# Render




cdef extern int32_t iGet3DGroupFlags_MVIEW(void*, const int32_t*, const int32_t*);


cdef extern void Set3DGroupFlags_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void _GetGroupFreezeScale_MVIEW(void*, const int32_t*, const int32_t*, double*);


cdef extern void _SetFreezeScale_MVIEW(void*, const int32_t*, const double*);


cdef extern void _SetGroupFreezeScale_MVIEW(void*, const int32_t*, const int32_t*, const double*);


cdef extern int32_t iFindGroup_MVIEW(void*, const int32_t*, const void*);


cdef extern void IGroupName_MVIEW(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void Render_MVIEW(void*, const int32_t*, int32_t, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


# Utility Drawing




cdef extern void _SetUFac_MVIEW(void*, const int32_t*, const double*);


cdef extern void AxisX_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void AxisY_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Grid_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void LabelFid_MVIEW(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void LabelX_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LabelY_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void OptimumTick_MVIEW(void*, const double*, const double*, double*);


# View




cdef extern int32_t Create_MVIEW(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t CreateCrookedSection_MVIEW(void*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateCrookedSectionDataProfile_MVIEW(void*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Destroy_MVIEW(void*, const int32_t*);


cdef extern void Extent_MVIEW(void*, const int32_t*, const int32_t*, const int32_t*, double*, double*, double*, double*);


cdef extern int32_t GetMAP_MVIEW(void*, const int32_t*);


cdef extern int32_t GetREG_MVIEW(void*, const int32_t*);


cdef extern void IGetName_MVIEW(void*, const int32_t*, void*, const int32_t*);


# View Control




cdef extern void _PlotToView_MVIEW(void*, const int32_t*, double*, double*);


cdef extern void _SetThinRes_MVIEW(void*, const int32_t*, const double*);


cdef extern void _ViewToPlot_MVIEW(void*, const int32_t*, double*, double*);


cdef extern void BestFitWindow_MVIEW(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, const int32_t*);


cdef extern void FitMapWindow3D_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void FitWindow_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void IGetClassName_MVIEW(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void MapOrigin_MVIEW(void*, const int32_t*, double*, double*);


cdef extern void ReScale_MVIEW(void*, const int32_t*, const double*);


cdef extern double rGetMapScale_MVIEW(void*, const int32_t*);


cdef extern double rScaleMM_MVIEW(void*, const int32_t*);


cdef extern double rScalePjMM_MVIEW(void*, const int32_t*);


cdef extern double rScaleYMM_MVIEW(void*, const int32_t*);


cdef extern void ScaleAllGroup_MVIEW(void*, const int32_t*, const double*, const double*);


cdef extern void ScaleWindow_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetClassName_MVIEW(void*, const int32_t*, const void*, const void*);


cdef extern void SetWindow_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void TranScale_MVIEW(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void UserToView_MVIEW(void*, const int32_t*, double*, double*);


cdef extern void ViewToUser_MVIEW(void*, const int32_t*, double*, double*);




# Class MVU


cdef extern void Arrow_MVU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ArrowVectorVV_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void BarChart_MVU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const double*, const void*, const double*, const void*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void CDIPixelPlot_MVU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CDIPixelPlot3D_MVU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ColorBar_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ColorBar2_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ColorBar2Style_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ColorBarHor_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ColorBarHor2_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ColorBarHor2Style_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void ColorBarHorStyle_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void ColorBarStyle_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ColorBarREG_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Contour_MVU(void*, const int32_t*, const void*, const void*);


cdef extern void ContourPLY_MVU(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void CSymbLegend_MVU(void*, const int32_t*, const double*, const double*, const double*, const double*, const void*, const void*, const void*);


cdef extern void DecayCurve_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const void*);


cdef extern void DirectionPlot_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void EMForward_MVU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExportDatamineString_MVU(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ExportDXF3D_MVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExportSurpacSTR_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FlightPlot_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const int32_t*, const double*, const double*);


cdef extern void GenAreas_MVU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const double*);


cdef extern void GetRangeGOCADSurface_MVU(void*, const void*, double*, double*, double*, double*, double*, double*);


cdef extern void Histogram_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Histogram2_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const double*, const void*, const double*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void Histogram3_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Histogram4_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Histogram5_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iExportableDXF3DGroupsLST_MVU(void*, const int32_t*, const int32_t*);


cdef extern int32_t iMapsetTest_MVU(void*, const double*, const double*, const double*, const double*, const void*, const int32_t*, const int32_t*, double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern int32_t iMapset2Test_MVU(void*, const double*, const double*, const double*, const double*, const void*, const int32_t*, const int32_t*, double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ImportGOCADSurface_MVU(void*, const int32_t*, const void*, const int32_t*);


cdef extern void LoadPlot_MVU(void*, const int32_t*, const void*);


cdef extern void MapFromPLT_MVU(void*, const int32_t*, const void*, const void*, const void*, const double*, const double*);


cdef extern void MapMDF_MVU(void*, const int32_t*, const void*, const void*);


cdef extern void Mapset_MVU(void*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const void*, const int32_t*, const int32_t*, double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Mapset2_MVU(void*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*, const void*, const int32_t*, const int32_t*, double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void MDF_MVU(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void PathPlot_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*);


cdef extern void PathPlotEx_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*);


cdef extern void PathPlotEx2_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern void PlotVoxelSurface_MVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*);


cdef extern void PlotVoxelSurface2_MVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const double*, const void*);


cdef extern void GenerateSurfaceFromVoxel_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const double*, const double*, const void*);


cdef extern void Post_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void PostEx_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*);


cdef extern void Probability_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ProfilePlot_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern void ProfilePlotEx_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*, const double*, const int32_t*, const void*, const void*);


cdef extern void PropSymbLegend_MVU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const double*, const void*, const void*);


cdef extern void ReGenAreas_MVU(void*, const int32_t*, const void*);


cdef extern void SymbOff_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void TextBox_MVU(void*, const int32_t*, const double*, const double*, const double*, const double*, const void*, const double*, const int32_t*);


cdef extern void Tick_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void TickEx_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*);


cdef extern void TrndPath_MVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);



# Class MXD


cdef extern void CreateMetadata_MXD(void*, const void*);


cdef extern void ConvertToMap_MXD(void*, const void*, const void*);


cdef extern void Sync_MXD(void*, const void*);



# Class PAT


cdef extern int32_t Create_PAT(void*);


cdef extern void Destroy_PAT(void*, const int32_t*);


cdef extern void GetLST_PAT(void*, const int32_t*, const void*, const int32_t*);



# Class PG

# 2D Methods




cdef extern void Copy_PG(void*, const int32_t*, const int32_t*);


cdef extern void CopySubset_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_PG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateS_PG(void*, const int32_t*);


cdef extern void Destroy_PG(void*, const int32_t*);


cdef extern void Dummy_PG(void*, const int32_t*);


cdef extern int32_t iEType_PG(void*, const int32_t*);


cdef extern int32_t iNCols_PG(void*, const int32_t*);


cdef extern int32_t iNRows_PG(void*, const int32_t*);


cdef extern int32_t iNSlices_PG(void*, const int32_t*);


cdef extern void Range_PG(void*, const int32_t*, double*, double*);


cdef extern double rGet_PG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadCol_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadRow_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReAllocate_PG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Serial_PG(void*, const int32_t*, const int32_t*);


cdef extern void Statistics_PG(void*, const int32_t*, const int32_t*);


cdef extern void WriteCol_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteRow_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# 3D Methods




cdef extern void CopySubset3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadCol3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadRow3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadTrace3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReAllocate3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteCol3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteRow3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteTrace3D_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# Utility Methods




cdef extern void ReadBF_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadRA_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void WriteBF_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void WriteWA_PG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);




# Class PJ


cdef extern void ClipPLY_PJ(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void ConvertVV_PJ(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ConvertVV3_PJ(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ConvertXY_PJ(void*, const int32_t*, double*, double*);


cdef extern void ConvertXYFromXYZ_PJ(void*, const int32_t*, double*, double*, const double*);


cdef extern void ConvertXYZ_PJ(void*, const int32_t*, double*, double*, double*);


cdef extern int32_t Create_PJ(void*, const void*, const void*);


cdef extern int32_t CreateIPJ_PJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateRectified_PJ(void*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void Destroy_PJ(void*, const int32_t*);


cdef extern int32_t iElevation_PJ(void*, const int32_t*);


cdef extern int32_t iIsInputLL_PJ(void*, const int32_t*);


cdef extern int32_t iIsOutputLL_PJ(void*, const int32_t*);


cdef extern void ProjectBoundingRectangle_PJ(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void ProjectBoundingRectangle2_PJ(void*, const int32_t*, double*, double*, double*, double*, const double*);


cdef extern void ProjectBoundingRectangleRes_PJ(void*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern void ProjectBoundingRectangleRes2_PJ(void*, const int32_t*, double*, double*, double*, double*, double*, const double*);


cdef extern void ProjectLimitedBoundingRectangle_PJ(void*, const int32_t*, const double*, const double*, const double*, const double*, double*, double*, double*, double*);


cdef extern void SetupLDT_PJ(void*, const int32_t*);



# Class PLY


cdef extern void AddPolygon_PLY(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AddPolygonEx_PLY(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ChangeIPJ_PLY(void*, const int32_t*, const int32_t*);


cdef extern void Clear_PLY(void*, const int32_t*);


cdef extern void Copy_PLY(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_PLY(void*);


cdef extern int32_t CreateS_PLY(void*, const int32_t*);


cdef extern void Destroy_PLY(void*, const int32_t*);


cdef extern void Extent_PLY(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void GetIPJ_PLY(void*, const int32_t*, const int32_t*);


cdef extern void GetPolygon_PLY(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetPolygonEx_PLY(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, int32_t*);


cdef extern int32_t iClipArea_PLY(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern int32_t iClipLineInt_PLY(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const double*, int32_t*);


cdef extern int32_t iClipPLY_PLY(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IGetDescription_PLY(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iNumPoly_PLY(void*, const int32_t*);


cdef extern void LoadTable_PLY(void*, const int32_t*, const void*);


cdef extern double rArea_PLY(void*, const int32_t*);


cdef extern void Rectangle_PLY(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void Rotate_PLY(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void SaveTable_PLY(void*, const int32_t*, const void*);


cdef extern void Serial_PLY(void*, const int32_t*, const int32_t*);


cdef extern void SetDescription_PLY(void*, const int32_t*, const void*);


cdef extern void SetIPJ_PLY(void*, const int32_t*, const int32_t*);


cdef extern void Thin_PLY(void*, const int32_t*, const double*);



# Class RA


cdef extern int32_t Create_RA(void*, const void*);


cdef extern int32_t CreateSBF_RA(void*, const int32_t*, const void*);


cdef extern void Destroy_RA(void*, const int32_t*);


cdef extern int32_t IiGets_RA(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iLen_RA(void*, const int32_t*);


cdef extern int32_t iLine_RA(void*, const int32_t*);


cdef extern int32_t iSeek_RA(void*, const int32_t*, const int32_t*);



# Class REG


cdef extern void Clear_REG(void*, const int32_t*);


cdef extern void Copy_REG(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_REG(void*, const int32_t*);


cdef extern int32_t CreateS_REG(void*, const int32_t*);


cdef extern void Destroy_REG(void*, const int32_t*);


cdef extern void Get_REG(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void GetInt_REG(void*, const int32_t*, const void*, int32_t*);


cdef extern void GetOne_REG(void*, const int32_t*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern void GetReal_REG(void*, const int32_t*, const void*, double*);


cdef extern int32_t iEntries_REG(void*, const int32_t*);


cdef extern void LoadINI_REG(void*, const int32_t*, const void*);


cdef extern void MatchString_REG(void*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void Merge_REG(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SaveINI_REG(void*, const int32_t*, const void*);


cdef extern void Serial_REG(void*, const int32_t*, const int32_t*);


cdef extern void Set_REG(void*, const int32_t*, const void*, const void*);


cdef extern void SetInt_REG(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SetReal_REG(void*, const int32_t*, const void*, const double*);



# Class SBF


cdef extern int32_t Create_SBF(void*, const int32_t*, const void*, const int32_t*);


cdef extern void CreateObjList_SBF(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DelDir_SBF(void*, const int32_t*, const void*);


cdef extern void DelFile_SBF(void*, const int32_t*, const void*);


cdef extern void Destroy_SBF(void*, const int32_t*);


cdef extern int32_t hGetDB_SBF(void*, const int32_t*);


cdef extern int32_t hGetMAP_SBF(void*, const int32_t*);


cdef extern int32_t hGetSYS_SBF(void*);


cdef extern int32_t iExistDir_SBF(void*, const int32_t*, const void*);


cdef extern int32_t iExistFile_SBF(void*, const int32_t*, const void*);


cdef extern void SaveLog_SBF(void*, const int32_t*, const void*, const void*, const void*, const int32_t*);



# Class ST


cdef extern int32_t Create_ST(void*);


cdef extern int32_t CreateExact_ST(void*);


cdef extern void Data_ST(void*, const int32_t*, const double*);


cdef extern void DataVV_ST(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_ST(void*, const int32_t*);


cdef extern void GetHistogramBins_ST(void*, const int32_t*, const int32_t*);


cdef extern void GetHistogramInfo_ST(void*, const int32_t*, int32_t*, double*, double*);


cdef extern void Histogram_ST(void*, const int32_t*, const int32_t*);


cdef extern void Histogram2_ST(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern double rEquivalentPercentile_ST(void*, const int32_t*, const double*);


cdef extern double rEquivalentValue_ST(void*, const int32_t*, const double*);


cdef extern void Reset_ST(void*, const int32_t*);


cdef extern double rGetInfo_ST(void*, const int32_t*, const int32_t*);


cdef extern double rGetNormProb_ST(void*, const double*);


cdef extern double rGetNormProbX_ST(void*, const double*);


cdef extern double rNormalTest_ST(void*, const int32_t*);



# Class ST2


cdef extern int32_t Create_ST2(void*);


cdef extern void DataVV_ST2(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Destroy_ST2(void*, const int32_t*);


cdef extern int32_t iItems_ST2(void*, const int32_t*);


cdef extern void Reset_ST2(void*, const int32_t*);


cdef extern double rGet_ST2(void*, const int32_t*, const int32_t*);



# Class STR

# Data Input




cdef extern int32_t iScanI_STR(void*, const void*);


cdef extern double rScanDate_STR(void*, const void*, const int32_t*);


cdef extern double rScanForm_STR(void*, const void*, const int32_t*);


cdef extern double rScanR_STR(void*, const void*);


cdef extern double rScanTime_STR(void*, const void*, const int32_t*);


# File Name




cdef extern void IFileCombineParts_STR(void*, const void*, const void*, const void*, const void*, const void*, void*, const int32_t*);


cdef extern void IFileExt_STR(void*, const void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void IFileNamePart_STR(void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void IGetMFile_STR(void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void IRemoveQualifiers_STR(void*, const void*, void*, const int32_t*);


# Formating




cdef extern void IFormatCRC_STR(void*, const int32_t*, void*, const int32_t*, const int32_t*);


cdef extern void IFormatDate_STR(void*, const double*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IFormatI_STR(void*, const int32_t*, void*, const int32_t*, const int32_t*);


cdef extern void IFormatR_STR(void*, const double*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IFormatR2_STR(void*, const double*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IFormatReal_STR(void*, const double*, void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IFormatTime_STR(void*, const double*, void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# General




cdef extern void _Escape_STR(void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t iChar_STR(void*, const void*);


cdef extern int32_t IiCharN_STR(void*, const void*, const int32_t*, const int32_t*);


cdef extern void IJustify_STR(void*, const void*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IReplaceiMatchString_STR(void*, void*, const void*, const void*, const int32_t*);


cdef extern void IReplaceMatchString_STR(void*, void*, const void*, const void*, const int32_t*);


cdef extern void ISetCharN_STR(void*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ISplitString_STR(void*, void*, const void*, void*, const int32_t*);


cdef extern void IStrcat_STR(void*, void*, const void*, const int32_t*);


cdef extern int32_t iStrcmp_STR(void*, const void*, const void*, const int32_t*);


cdef extern void IStrcpy_STR(void*, void*, const void*, const int32_t*);


cdef extern int32_t iStriMask_STR(void*, const void*, const void*);


cdef extern void IStrins_STR(void*, void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iStrlen_STR(void*, const void*);


cdef extern int32_t iStrMask_STR(void*, const void*, const void*);


cdef extern int32_t iStrMin_STR(void*, void*);


cdef extern int32_t iStrMin2_STR(void*, const void*);


cdef extern int32_t iStrncmp_STR(void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t iStrStr_STR(void*, const void*, const void*, const int32_t*);


cdef extern void ISubstr_STR(void*, void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void IToLower_STR(void*, void*, const int32_t*);


cdef extern void IToUpper_STR(void*, void*, const int32_t*);


cdef extern void IXYZLine_STR(void*, const void*, void*, const int32_t*);


cdef extern void MakeAlpha_STR(void*, void*);


cdef extern void Printf_STR(void*, void*, const int32_t*, const void*);


cdef extern void ReplaceChar_STR(void*, void*, const void*, const void*);


cdef extern void ReplaceChar2_STR(void*, void*, const void*, const void*);


cdef extern void ReplaceMultiChar_STR(void*, void*, const void*, const void*);


cdef extern void ReplaceNonASCII_STR(void*, void*, const void*);


cdef extern void SetChar_STR(void*, void*, const int32_t*);


cdef extern void TrimQuotes_STR(void*, void*);


cdef extern void TrimSpace_STR(void*, void*, const int32_t*);


cdef extern void UnQuote_STR(void*, void*);


# Misc




cdef extern void IGenGroupName_STR(void*, const void*, const void*, const void*, void*, const int32_t*);


# Tokenizing




cdef extern int32_t iCountTokens_STR(void*, const void*, const void*);


cdef extern void IGetToken_STR(void*, void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iTokenize_STR(void*, void*, const void*, const void*, const void*, const void*);


cdef extern int32_t iTokens_STR(void*, void*, const void*);


cdef extern int32_t iTokens2_STR(void*, void*, const void*, const void*, const void*, const void*);


cdef extern void ParseList_STR(void*, const void*, const int32_t*);




# Class SURFACE


cdef extern int32_t Create_SURFACE(void*, const void*, const int32_t*);


cdef extern int32_t Open_SURFACE(void*, const void*, const int32_t*);


cdef extern void Destroy_SURFACE(void*, const int32_t*);


cdef extern void GetIPJ_SURFACE(void*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_SURFACE(void*, const int32_t*, const int32_t*);


cdef extern void GetSurfaceItems_SURFACE(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetSurfaceItem_SURFACE(void*, const int32_t*, const void*);


cdef extern void AddSurfaceItem_SURFACE(void*, const int32_t*, const int32_t*);


cdef extern void GetSurfaceNames_SURFACE(void*, const void*, const int32_t*);


cdef extern void GetClosedSurfaceNames_SURFACE(void*, const void*, const int32_t*);


cdef extern void GetExtents_SURFACE(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t CRC_SURFACE(void*, const void*, const void*, int32_t*);


cdef extern void Sync_SURFACE(void*, const void*);


cdef extern void CreateFromDXF_SURFACE(void*, const int32_t*, const void*, const void*);


cdef extern void CreateFromVulcanTriangulation_SURFACE(void*, const void*, const int32_t*, const void*);


cdef extern void AppendVulcanTriangulation_SURFACE(void*, const void*, const int32_t*, const void*);



# Class SURFACEITEM


cdef extern int32_t Create_SURFACEITEM(void*, const void*, const void*);


cdef extern void Destroy_SURFACEITEM(void*, const int32_t*);


cdef extern void GetGUID_SURFACEITEM(void*, const int32_t*, void*, const int32_t*);


cdef extern void SetProperties_SURFACEITEM(void*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const void*, const void*, const double*);


cdef extern void SetPropertiesEx_SURFACEITEM(void*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const void*, const void*, const int32_t*, const double*, const double*);


cdef extern void GetProperties_SURFACEITEM(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, double*, void*, const int32_t*, void*, const int32_t*, double*);


cdef extern void GetPropertiesEx_SURFACEITEM(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, double*, void*, const int32_t*, void*, const int32_t*, int32_t*, double*, double*);


cdef extern void SetDefaultRenderProperties_SURFACEITEM(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void GetDefaultRenderProperties_SURFACEITEM(void*, const int32_t*, int32_t*, double*, int32_t*);


cdef extern int32_t iNumComponents_SURFACEITEM(void*, const int32_t*);


cdef extern int32_t iAddMesh_SURFACEITEM(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetMesh_SURFACEITEM(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetExtents_SURFACEITEM(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GetMeshInfo_SURFACEITEM(void*, const int32_t*, const int32_t*, int32_t*, int32_t*, double*, double*, double*);


cdef extern void GetInfo_SURFACEITEM(void*, const int32_t*, int32_t*, double*, double*, double*);


cdef extern void GetGeometryInfo_SURFACEITEM(void*, const int32_t*, int32_t*, int32_t*);


cdef extern void ComputeExtendedInfo_SURFACEITEM(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);



# Class SYS

# Date/Time




cdef extern void BreakDate_SYS(void*, const double*, int32_t*, int32_t*, int32_t*);


cdef extern int32_t iDatetoLong_SYS(void*, const double*);


cdef extern int32_t iTimetoLong_SYS(void*, const double*);


cdef extern double rDate_SYS(void*);


cdef extern double rLongtoDate_SYS(void*, const int32_t*);


cdef extern double rLongtoTime_SYS(void*, const int32_t*);


cdef extern double rMakeDate_SYS(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rSecondstoTime_SYS(void*, const double*);


cdef extern double rTime_SYS(void*);


cdef extern double rTimetoSeconds_SYS(void*, const double*);


cdef extern double rUTCDate_SYS(void*);


cdef extern double rUTCTime_SYS(void*);


# Environment




cdef extern int32_t iExistEnv_SYS(void*, const void*);


cdef extern void IGetEnv_SYS(void*, const void*, void*, const int32_t*);


cdef extern void SetEnv_SYS(void*, const void*, const void*);


# Error Handling




cdef extern int32_t iClearErrAP_SYS(void*);


cdef extern int32_t iGetTopErrorAP_SYS(void*);


cdef extern void IGetErrorMessageAP_SYS(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iNumErrorsAP_SYS(void*);


cdef extern void SetServerMessagesAP_SYS(void*, const int32_t*);


# Execution




cdef extern int32_t iRun_SYS(void*, const void*, const void*, const int32_t*);


cdef extern int32_t iRunGS_SYS(void*, const void*);


cdef extern int32_t iRunGX_SYS(void*, const void*);


cdef extern int32_t iRunGXEx_SYS(void*, const void*, int32_t*);


cdef extern int32_t App_iRunPDF_SYS(void*, const void*, const void*);


cdef extern int32_t iShellExecute_SYS(void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void SetReturn_SYS(void*, const int32_t*);


# External DLL




cdef extern void App_DoCommand_SYS(void*, const void*);


cdef extern void Error_SYS(void*, const void*, const void*, const int32_t*);


cdef extern void ErrorTag_SYS(void*, const void*, const void*);


cdef extern int32_t iAssertGX_SYS(void*, const int32_t*, const void*, const void*);


cdef extern int32_t App_iOLEAutomation_SYS(void*, const void*, const void*, const int32_t*);


cdef extern void App_SaveLog_SYS(void*, const void*);


cdef extern void App_ShowError_SYS(void*);


cdef extern void Terminate_SYS(void*, const void*);


# File System




cdef extern int32_t CRCFile_SYS(void*, const void*);


cdef extern int32_t CRCFileOffset_SYS(void*, const void*, const int32_t*);


cdef extern void FileRen_SYS(void*, const void*, const void*);


cdef extern void FindFilesVV_SYS(void*, const int32_t*, const void*);


cdef extern void IAbsoluteFileName_SYS(void*, const void*, void*, const int32_t*);


cdef extern int32_t iCopyFile_SYS(void*, const void*, const void*);


cdef extern int32_t iDeleteFile_SYS(void*, const void*);


cdef extern int32_t iDeleteGIFile_SYS(void*, const void*);


cdef extern int32_t iDeleteGridFile_SYS(void*, const void*);


cdef extern int32_t iDirExist_SYS(void*, const void*);


cdef extern int32_t iFileExist_SYS(void*, const void*);


cdef extern int32_t iFileSize_SYS(void*, const void*);


cdef extern int32_t iFileWritable_SYS(void*, const void*);


cdef extern int32_t iFindPath_SYS(void*, const void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iFindPathEx_SYS(void*, const void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void IGetDirectory_SYS(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetPath_SYS(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetWindowsDir_SYS(void*, void*, const int32_t*);


cdef extern int32_t iMakeDir_SYS(void*, const void*);


cdef extern int32_t iMakeFileReadonly_SYS(void*, const void*);


cdef extern int32_t iMakeFileWritable_SYS(void*, const void*);


cdef extern void IRelativeFileName_SYS(void*, const void*, void*, const int32_t*);


cdef extern void IShortPathFileName_SYS(void*, const void*, void*, const int32_t*);


cdef extern void ITempFileExt_SYS(void*, const void*, void*, const int32_t*);


cdef extern void ITempFileName_SYS(void*, const void*, void*, const int32_t*);


cdef extern void ITransferPath_SYS(void*, const void*, void*, const int32_t*);


cdef extern int32_t iValidFileName_SYS(void*, const void*);


cdef extern int32_t iWriteInDir_SYS(void*, const void*);


cdef extern double rFileDate_SYS(void*, const void*);


cdef extern double rFileTime_SYS(void*, const void*);


cdef extern double rUTCFileDate_SYS(void*, const void*);


cdef extern double rUTCFileTime_SYS(void*, const void*);


# Global Parameter




cdef extern void GetSettingsMETA_SYS(void*, const int32_t*);


cdef extern void GlobalReset_SYS(void*, const void*);


cdef extern void GlobalSet_SYS(void*, const void*, const void*);


cdef extern void GlobalWrite_SYS(void*, const void*);


cdef extern int32_t IiGlobal_SYS(void*, const void*, void*, const int32_t*);


cdef extern void App_ResetSettings_SYS(void*);


cdef extern void SetSettingsMETA_SYS(void*, const int32_t*);


# Licensing




cdef extern int32_t iCheckArcLicense_SYS(void*);


cdef extern int32_t iCheckArcLicenseEx_SYS(void*, void*, const int32_t*);


cdef extern int32_t iCheckIntrinsic_SYS(void*, const int32_t*, const void*);


cdef extern int32_t iGetGeodist_SYS(void*);


cdef extern void IGetLicenseClass_SYS(void*, void*, const int32_t*);


cdef extern void IGetLicensedUser_SYS(void*, void*, const int32_t*, void*, const int32_t*);


# Lineage




cdef extern void AddLineageParameter_SYS(void*, const void*, const void*);


cdef extern void AddLineageSource_SYS(void*, const int32_t*, const void*);


cdef extern void ClearLineageParameters_SYS(void*);


cdef extern void ClearLineageSources_SYS(void*);


cdef extern void CopyGeoFile_SYS(void*, const void*, const void*);


cdef extern void IBackupGeoFile_SYS(void*, const void*, void*, const int32_t*);


cdef extern void RemoveLineageOutput_SYS(void*, const void*);


cdef extern void RemoveLineageParameter_SYS(void*, const void*);


cdef extern void RemoveLineageSource_SYS(void*, const void*);


cdef extern void RestoreGeoFile_SYS(void*, const void*, const void*);


cdef extern void SetLineageDescription_SYS(void*, const void*);


cdef extern void SetLineageDisplayName_SYS(void*, const void*);


cdef extern void SetLineageName_SYS(void*, const void*);


# Menus and Toolbar




cdef extern void App_ClearMenus_SYS(void*, const int32_t*);


cdef extern void App_GetLoadedMenus_SYS(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetLoadedMenus_SYS(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetEntitlementRights_SYS(void*, const int32_t*);


# Misc




cdef extern void GenerateGUID_SYS(void*, void*, const int32_t*);


cdef extern void ClipboardToFile_SYS(void*, const void*);


cdef extern int32_t CreateClipboardRA_SYS(void*);


cdef extern int32_t CreateClipboardWA_SYS(void*);


cdef extern void Destr_SYS(void*, const int32_t*);


cdef extern void EMFObjectSize_SYS(void*, const void*, double*, double*);


cdef extern void FileToClipboard_SYS(void*, const void*);


cdef extern void FontLST_SYS(void*, const int32_t*, const int32_t*);


cdef extern int32_t IiGetDotNetGXEntries_SYS(void*, const void*, void*, const int32_t*);


cdef extern void SendGeneralMessage_SYS(void*, const void*, const void*);


cdef extern void WriteDebugLog_SYS(void*, const void*);


# Multithreading




cdef extern int32_t iGetThreadID_SYS(void*);


cdef extern void RunMultiUserScript_SYS(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


# Parameter




cdef extern void ClearGroup_SYS(void*, const void*);


cdef extern void ClearGroupParm_SYS(void*, const void*);


cdef extern void ClearParm_SYS(void*);


cdef extern void DefaultInt_SYS(void*, const void*, const void*, const int32_t*);


cdef extern void DefaultReal_SYS(void*, const void*, const void*, const double*);


cdef extern void DefaultString_SYS(void*, const void*, const void*, const void*);


cdef extern void GetPattern_SYS(void*, const void*, int32_t*, double*, int32_t*, double*, int32_t*, int32_t*);


cdef extern void GetREG_SYS(void*, const int32_t*, const void*);


cdef extern void GtString_SYS(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t iExistInt_SYS(void*, const void*, const void*);


cdef extern int32_t iExistReal_SYS(void*, const void*, const void*);


cdef extern int32_t iExistString_SYS(void*, const void*, const void*);


cdef extern int32_t iGetInt_SYS(void*, const void*, const void*);


cdef extern int32_t iGetYesNo_SYS(void*, const void*, const void*);


cdef extern void IReplaceString_SYS(void*, const void*, void*, const int32_t*, const void*);


cdef extern void LoadParm_SYS(void*, const void*, const void*);


cdef extern double rGetReal_SYS(void*, const void*, const void*);


cdef extern void SaveParm_SYS(void*, const void*, const int32_t*, const void*);


cdef extern void FilterParmGroup_SYS(void*, const void*, const int32_t*);


cdef extern void SetInt_SYS(void*, const void*, const void*, const int32_t*);


cdef extern void SetPattern_SYS(void*, const void*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*, const int32_t*);


cdef extern void SetReal_SYS(void*, const void*, const void*, const double*);


cdef extern void SetREG_SYS(void*, const int32_t*);


cdef extern void SetString_SYS(void*, const void*, const void*, const void*);


# Progress Control




cdef extern int32_t iCheckStop_SYS(void*);


cdef extern int32_t iProgState_SYS(void*);


cdef extern void ProgName_SYS(void*, const void*, const int32_t*);


cdef extern void Progress_SYS(void*, const int32_t*);


cdef extern void ProgUpdate_SYS(void*, const int32_t*);


cdef extern void ProgUpdateL_SYS(void*, const int32_t*, const int32_t*);


# Registry




cdef extern void IGetSysInfo_SYS(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t IiRegistryGetVal_SYS(void*, const int32_t*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t iRegistryDeleteKey_SYS(void*, const int32_t*, const void*);


cdef extern int32_t iRegistryDeleteVal_SYS(void*, const int32_t*, const void*, const void*);


cdef extern void RegistrySetVal_SYS(void*, const int32_t*, const void*, const void*, const void*);


# Temporary File




cdef extern void DestroyPTMP_SYS(void*, const int32_t*);


cdef extern void GetPTMP_SYS(void*, const int32_t*);


cdef extern int32_t SavePTMP_SYS(void*, const void*);


# Termination




cdef extern void _Abort_SYS(void*, const void*);


cdef extern void _Assert_SYS(void*, const int32_t*);


cdef extern void _Exit_SYS(void*);


cdef extern void Cancel_SYS(void*);


# Timing




cdef extern int32_t iDelay_SYS(void*, const double*);


cdef extern int32_t iGetTimer_SYS(void*, const int32_t*, double*, double*);


# User Interaction




cdef extern void App_DisplayHelp_SYS(void*, const void*, const void*);


cdef extern void App_DisplayHelpTopic_SYS(void*, const void*, const void*);


cdef extern void App_DisplayInt_SYS(void*, const void*, const int32_t*);


cdef extern void App_DisplayMessage_SYS(void*, const void*, const void*);


cdef extern void App_DisplayReal_SYS(void*, const void*, const double*);


cdef extern int32_t App_iDisplayQuestion_SYS(void*, const void*, const void*);


cdef extern int32_t App_iDisplayQuestionWithCancel_SYS(void*, const void*, const void*);


cdef extern int32_t iInteractive_SYS(void*);


cdef extern int32_t App_IiPrompt_SYS(void*, const void*, void*, const int32_t*);


cdef extern int32_t iScript_SYS(void*);


cdef extern int32_t iScriptRecord_SYS(void*);


cdef extern void App_SetCursor_SYS(void*, const void*);


cdef extern void App_SetInfoLine_SYS(void*, const void*);


cdef extern void SetInteractive_SYS(void*, const int32_t*);


# Workspace




cdef extern void GetWorkspaceREG_SYS(void*, const int32_t*);


cdef extern void SetWorkspaceREG_SYS(void*, const int32_t*);


# String Encryption




cdef extern void EncryptString_SYS(void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void DecryptString_SYS(void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t IsEncryptedString_SYS(void*, const void*);


# GX Debugger




cdef extern void DisableGXDebugger_SYS(void*);


cdef extern void EnableGXDebugger_SYS(void*, const void*, const void*);




# Class TB


cdef extern void _SetSearchMode_TB(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_TB(void*, const void*);


cdef extern int32_t CreateDB_TB(void*, const int32_t*);


cdef extern int32_t CreateLTB_TB(void*, const int32_t*);


cdef extern void Destroy_TB(void*, const int32_t*);


cdef extern int32_t Field_TB(void*, const int32_t*, const void*);


cdef extern void GetString_TB(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iDataType_TB(void*, const int32_t*, const int32_t*);


cdef extern void IFindColByIndex_TB(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iFindColByName_TB(void*, const int32_t*, const void*);


cdef extern int32_t iFormat_TB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iGetInt_TB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iNumColumns_TB(void*, const int32_t*);


cdef extern int32_t iNumRows_TB(void*, const int32_t*);


cdef extern void LoadDB_TB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rGetReal_TB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Save_TB(void*, const int32_t*, const void*);


cdef extern void SaveDB_TB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SaveToAscii_TB(void*, const int32_t*, const void*);


cdef extern void SetInt_TB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetReal_TB(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_TB(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void Sort_TB(void*, const int32_t*, const int32_t*);



# Class TPAT


cdef extern void AddColor_TPAT(void*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t Create_TPAT(void*);


cdef extern void Destroy_TPAT(void*, const int32_t*);


cdef extern int32_t iCode_TPAT(void*, const int32_t*, const void*);


cdef extern void IGetSolidPattern_TPAT(void*, const int32_t*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, int32_t*);


cdef extern int32_t iSize_TPAT(void*, const int32_t*);


cdef extern void LoadCSV_TPAT(void*, const int32_t*, const void*);


cdef extern void SetupTranslationVV_TPAT(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class TR


cdef extern int32_t Create_TR(void*, const int32_t*);


cdef extern void Destroy_TR(void*, const int32_t*);


cdef extern void Copy_TR(void*, const int32_t*, const int32_t*);



# Class USERMETA


cdef extern int32_t Create_USERMETA(void*, const int32_t*);


cdef extern int32_t CreateS_USERMETA(void*, const void*);


cdef extern void Destroy_USERMETA(void*, const int32_t*);


cdef extern void GetDataCreationDate_USERMETA(void*, const int32_t*, double*);


cdef extern void GetExtents2d_USERMETA(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void GetExtents3d_USERMETA(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GetIPJ_USERMETA(void*, const int32_t*, const int32_t*);


cdef extern void GetMetaCreationDate_USERMETA(void*, const int32_t*, double*);


cdef extern void GetXMLFormat_USERMETA(void*, const int32_t*, int32_t*);


cdef extern int32_t iCompare_USERMETA(void*, const int32_t*, const int32_t*);


cdef extern void IGetDataCreator_USERMETA(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetFormat_USERMETA(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetMetaCreator_USERMETA(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetProject_USERMETA(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetTitle_USERMETA(void*, const int32_t*, void*, const int32_t*);


cdef extern void Serial_USERMETA(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetDataCreationDate_USERMETA(void*, const int32_t*, const double*);


cdef extern void SetDataCreator_USERMETA(void*, const int32_t*, const void*);


cdef extern void SetExtents2d_USERMETA(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void SetExtents3d_USERMETA(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetFormat_USERMETA(void*, const int32_t*, const void*);


cdef extern void SetIPJ_USERMETA(void*, const int32_t*, const int32_t*);


cdef extern void SetMetaCreationDate_USERMETA(void*, const int32_t*, const double*);


cdef extern void SetMetaCreator_USERMETA(void*, const int32_t*, const void*);


cdef extern void SetProject_USERMETA(void*, const int32_t*, const void*);


cdef extern void SetTitle_USERMETA(void*, const int32_t*, const void*);


cdef extern void UpdateExtents2D_USERMETA(void*, const void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void UpdateFileType_USERMETA(void*, const void*, const void*);


cdef extern void SaveFileLineage_USERMETA(void*, const void*, const int32_t*);



# Class VA


cdef extern int32_t iGetArray_VA(void*, const int32_t*, int32_t, int32_t, int32_t, int32_t, const int32_t*, int32_t);


cdef extern int32_t iSetArray_VA(void*, const int32_t*, int32_t, int32_t, int32_t, int32_t, const int32_t*, int32_t);


cdef extern void AddElevationsVVToDepths_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Append_VA(void*, const int32_t*, const int32_t*);


cdef extern void Average_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Copy_VA(void*, const int32_t*, const int32_t*);


cdef extern void Copy2_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateExt_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateVV_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Destroy_VA(void*, const int32_t*);


cdef extern int32_t GetFullVV_VA(void*, const int32_t*);


cdef extern void GetVV_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCol_VA(void*, const int32_t*);


cdef extern int32_t iGetInt_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IGetString_VA(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iLen_VA(void*, const int32_t*);


cdef extern void IndexOrder_VA(void*, const int32_t*, const int32_t*);


cdef extern void LookupIndex_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RangeDouble_VA(void*, const int32_t*, double*, double*);


cdef extern void ReFid_VA(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void Reverse_VA(void*, const int32_t*);


cdef extern double rGetFidIncr_VA(void*, const int32_t*);


cdef extern double rGetFidStart_VA(void*, const int32_t*);


cdef extern double rGetReal_VA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetFidIncr_VA(void*, const int32_t*, const double*);


cdef extern void SetFidStart_VA(void*, const int32_t*, const double*);


cdef extern void SetInt_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetLn_VA(void*, const int32_t*, const int32_t*);


cdef extern void SetReal_VA(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_VA(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void SetVV_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Trans_VA(void*, const int32_t*, const double*, const double*);


cdef extern void Window_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Window2_VA(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern int32_t iCheckForRepeating_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern int32_t iCheckForRepeating2_VA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, int32_t*, int32_t*);



# Class VM


cdef extern int32_t Create_VM(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateExt_VM(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_VM(void*, const int32_t*);


cdef extern int32_t iGetInt_VM(void*, const int32_t*, const int32_t*);


cdef extern void IGetString_VM(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iLength_VM(void*, const int32_t*);


cdef extern void ReSize_VM(void*, const int32_t*, const int32_t*);


cdef extern double rGetReal_VM(void*, const int32_t*, const int32_t*);


cdef extern void SetInt_VM(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetReal_VM(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_VM(void*, const int32_t*, const int32_t*, const void*);



# Class VOX


cdef extern void CalcStats_VOX(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_VOX(void*, const void*);


cdef extern int32_t CreatePG_VOX(void*, const int32_t*);


cdef extern int32_t CreateTypePG_VOX(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_VOX(void*, const int32_t*);


cdef extern void Dump_VOX(void*, const int32_t*, const void*);


cdef extern void ExportDB_VOX(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExportIMG_VOX(void*, const int32_t*, const void*, const int32_t*);


cdef extern void ExportToGrids_VOX(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void ExportXML_VOX(void*, const void*, int32_t*, const void*);


cdef extern void ExportSegY_VOX(void*, const int32_t*, const void*, const double*);


cdef extern void ExportJIGsXML_VOX(void*, const void*, const void*);


cdef extern void ExportXYZ_VOX(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Filter_VOX(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*);


cdef extern void GenerateDB_VOX(void*, const void*, const int32_t*, const int32_t*);


cdef extern void GenerateVectorVoxelFromDB_VOX(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern int32_t GenerateGOCAD_VOX(void*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t GenerateOrientedGOCAD_VOX(void*, const void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t GeneratePG_VOX(void*, const void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern int32_t GenerateConstantValue_VOX(void*, const void*, const double*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GeneratePGVV_VOX(void*, const void*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GenerateConstantValueVV_VOX(void*, const void*, const double*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GenerateUBC_VOX(void*, const void*, const void*, const void*, const double*, const int32_t*);


cdef extern void GenerateXYZ_VOX(void*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t InitGenerateBySubsetPG_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AddGenerateBySubsetPG_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void EndGenerateBySubsetPG_VOX(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void GetArea_VOX(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GetGOCADLocation_VOX(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetGridSectionCellSizes_VOX(void*, const int32_t*, const double*, double*, double*);


cdef extern void GetInfo_VOX(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void GetIPJ_VOX(void*, const int32_t*, const int32_t*);


cdef extern void GetLimits_VOX(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void GetLimitsXYZ_VOX(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GetLocation_VOX(void*, const int32_t*, double*, double*, double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetLocationPoints_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetMETA_VOX(void*, const int32_t*, const int32_t*);


cdef extern void GetRealLocation_VOX(void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetSimpleLocation_VOX(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t GetStats_VOX(void*, const int32_t*);


cdef extern void GetTPAT_VOX(void*, const int32_t*, const int32_t*);


cdef extern int32_t GridPoints_VOX(void*, const void*, const void*, const double*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GridPointsZ_VOX(void*, const void*, const void*, const double*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t GridPointsZEx_VOX(void*, const void*, const void*, const double*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, double*, double*, const double*, double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCanAppendTo_VOX(void*, const int32_t*, const void*);


cdef extern void IGetCellSizeStrings_VOX(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, const double*, const double*, const double*);


cdef extern int32_t iIsThematic_VOX(void*, const int32_t*);


cdef extern int32_t iIsVectorVoxel_VOX(void*, const int32_t*);


cdef extern int32_t iSetCellSizeStrings_VOX(void*, const int32_t*, const void*, const void*, const void*);


cdef extern int32_t ListGOCADProperties_VOX(void*, const void*, const int32_t*);


cdef extern int32_t LogGridPointsZEx_VOX(void*, const void*, const void*, const double*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, double*, double*, const double*, double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Krig_VOX(void*, const void*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Math_VOX(void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void Merge_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t NearestNeighbourGrid_VOX(void*, const void*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rComputeCellSize_VOX(void*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void ReGrid_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t ResamplePG_VOX(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void RescaleCellSizes_VOX(void*, const int32_t*, const double*);


cdef extern void SampleCDI_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void SampleCDIToTopography_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void SampleVV_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_VOX(void*, const int32_t*, const int32_t*);


cdef extern void SetLocation_VOX(void*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetMETA_VOX(void*, const int32_t*, const int32_t*);


cdef extern void SetOrigin_VOX(void*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void SetSimpleLocation_VOX(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetTPAT_VOX(void*, const int32_t*, const int32_t*);


cdef extern void SliceIPJ_VOX(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void SliceMultiLayerIPJ_VOX(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void SubsetToRealExtents_VOX(void*, const int32_t*, const void*);


cdef extern void Sync_VOX(void*, const void*);


cdef extern void WindowPLY_VOX(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const void*, const int32_t*);


cdef extern void WindowXYZ_VOX(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const void*, const int32_t*);


cdef extern void WriteXML_VOX(void*, const int32_t*, const void*);


cdef extern void ConvertNumericToThematic_VOX(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ConvertThematicToNumeric_VOX(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ConvertVelocityToDensity_VOX(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const void*);


cdef extern void ConvertVelocityInRangeToDensity_VOX(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const void*);


cdef extern void ConvertDensityToVelocity_VOX(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const void*);


cdef extern void InvertZ_VOX(void*, const int32_t*, const void*);


cdef extern void IDWGridDB_VOX(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TINGridDB_VOX(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class VOXD


cdef extern int32_t Create_VOXD(void*, const int32_t*, const void*, const int32_t*, const double*);


cdef extern int32_t CreateITR_VOXD(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateThematic_VOXD(void*, const int32_t*);


cdef extern void Destroy_VOXD(void*, const int32_t*);


cdef extern void GetDrawControls_VOXD(void*, const int32_t*, int32_t*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void IGetName_VOXD(void*, const int32_t*, void*, const int32_t*);


cdef extern void GetITR_VOXD(void*, const int32_t*, const int32_t*);


cdef extern void GetShellControls_VOXD(void*, const int32_t*, double*, double*);


cdef extern void SetDrawControls_VOXD(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetITR_VOXD(void*, const int32_t*, const int32_t*);


cdef extern void SetShellControls_VOXD(void*, const int32_t*, const double*, const double*);



# Class VOXE


cdef extern int32_t Create_VOXE(void*, const int32_t*);


cdef extern void Destroy_VOXE(void*, const int32_t*);


cdef extern void Profile_VOXE(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double rValue_VOXE(void*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern void Vector_VOXE(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);



# Class VULCAN


cdef extern int32_t IsValidTriangulationFile_VULCAN(void*, const void*);


cdef extern int32_t IsValidBlockModelFile_VULCAN(void*, const void*);


cdef extern void TriangulationToView_VULCAN(void*, const void*, const int32_t*, const int32_t*, const void*);


cdef extern void GetBlockModelVariableInfo_VULCAN(void*, const void*, const int32_t*, const int32_t*);


cdef extern void GetBlockModelStringVariableValues_VULCAN(void*, const void*, const void*, const int32_t*);


cdef extern void BlockModelToVoxel_VULCAN(void*, const void*, const int32_t*, const void*, const void*, const int32_t*, const void*);



# Class VV


cdef extern int32_t iGetData_VV(void*, const int32_t*, int32_t, int32_t, const int32_t*, int32_t);


cdef extern int32_t iSetData_VV(void*, const int32_t*, int32_t, int32_t, const int32_t*, int32_t);


cdef extern void _Copy_VV(void*, const int32_t*, const int32_t*);


cdef extern void _Copy2_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void _Log_VV(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void _LogLinear_VV(void*, const int32_t*, const double*);


cdef extern void _Mask_VV(void*, const int32_t*, const int32_t*);


cdef extern void _Reverse_VV(void*, const int32_t*);


cdef extern void _Serial_VV(void*, const int32_t*, const int32_t*);


cdef extern void _Trans_VV(void*, const int32_t*, const double*, const double*);


cdef extern void Abs_VV(void*, const int32_t*);


cdef extern void Add_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Add2_VV(void*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*);


cdef extern void Append_VV(void*, const int32_t*, const int32_t*);


cdef extern void CopyVMtoVV_VV(void*, const int32_t*, const int32_t*);


cdef extern void CopyVVtoVM_VV(void*, const int32_t*, const int32_t*);


cdef extern int32_t CRC_VV(void*, const int32_t*, const int32_t*);


cdef extern int32_t CRCInexact_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_VV(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateExt_VV(void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateS_VV(void*, const int32_t*);


cdef extern void Destroy_VV(void*, const int32_t*);


cdef extern void Diff_VV(void*, const int32_t*, const int32_t*);


cdef extern void Divide_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FidNorm_VV(void*, const int32_t*, const int32_t*);


cdef extern void FillInt_VV(void*, const int32_t*, const int32_t*);


cdef extern void FillReal_VV(void*, const int32_t*, const double*);


cdef extern void FillString_VV(void*, const int32_t*, const void*);


cdef extern void GetVM_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCountDummies_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iFindDum_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGetFidExpansion_VV(void*, const int32_t*);


cdef extern int32_t iGetInt_VV(void*, const int32_t*, const int32_t*);


cdef extern void IGetString_VV(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iIndexMax_VV(void*, const int32_t*, double*);


cdef extern int32_t iLength_VV(void*, const int32_t*);


cdef extern void IndexInsert_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IndexOrder_VV(void*, const int32_t*, const int32_t*);


cdef extern void InitIndex_VV(void*, const int32_t*, const int32_t*);


cdef extern void InvLog_VV(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern int32_t iOrder_VV(void*, const int32_t*, int32_t*);


cdef extern void LinesToXY_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LookupIndex_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MakeMemBased_VV(void*, const int32_t*);


cdef extern void MaskAND_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MaskOR_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MaskStr_VV(void*, const int32_t*, const int32_t*, const void*);


cdef extern void Multiply_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Amplitude3D_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolygonMask_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Project_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Project3D_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RangeDouble_VV(void*, const int32_t*, double*, double*);


cdef extern void ReFid_VV(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void ReFidVV_VV(void*, const int32_t*, const int32_t*);


cdef extern void ReSample_VV(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern double rGetFidIncr_VV(void*, const int32_t*);


cdef extern double rGetFidStart_VV(void*, const int32_t*);


cdef extern double rGetReal_VV(void*, const int32_t*, const int32_t*);


cdef extern double rSum_VV(void*, const int32_t*);


cdef extern double rWeightedMean_VV(void*, const int32_t*, const int32_t*);


cdef extern void SetFidExpansion_VV(void*, const int32_t*, const int32_t*);


cdef extern void SetFidIncr_VV(void*, const int32_t*, const double*);


cdef extern void SetFidStart_VV(void*, const int32_t*, const double*);


cdef extern void SetInt_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetIntN_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetLen_VV(void*, const int32_t*, const int32_t*);


cdef extern void SetReal_VV(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetRealN_VV(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_VV(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SetStringN_VV(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void SetupIndex_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SetVM_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Sort_VV(void*, const int32_t*, const int32_t*);


cdef extern void SortIndex_VV(void*, const int32_t*, const int32_t*);


cdef extern void SortIndex1_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SortIndex2_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SortIndex3_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SortIndex4_VV(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Statistics_VV(void*, const int32_t*, const int32_t*);


cdef extern void Subtract_VV(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Swap_VV(void*, const int32_t*);


cdef extern void Window_VV(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void WriteXML_VV(void*, const int32_t*, const void*, const int32_t*, const int32_t*);



# Class WA


cdef extern void _Puts_WA(void*, const int32_t*, const void*);


cdef extern int32_t Create_WA(void*, const void*, const int32_t*);


cdef extern int32_t CreateEx_WA(void*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t CreateSBF_WA(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t CreateSBFEx_WA(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void Destroy_WA(void*, const int32_t*);


cdef extern void NewLine_WA(void*, const int32_t*);



# Class ACQUIRE


cdef extern int32_t Create_ACQUIRE(void*);


cdef extern void DeleteEmptyChan_ACQUIRE(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_ACQUIRE(void*, const int32_t*);


cdef extern int32_t iImportHole_ACQUIRE(void*, const int32_t*, const void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iImportPoint_ACQUIRE(void*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iSelectionTool_ACQUIRE(void*, const int32_t*, const void*, const int32_t*);



# Class ARCDB


cdef extern int32_t CreateDAT_ARCDB(void*, const int32_t*, const void*, const void*, const void*);


cdef extern int32_t CreateDAT3D_ARCDB(void*, const int32_t*, const void*, const void*, const void*, const void*);


cdef extern int32_t Current_ARCDB(void*);


cdef extern void ExportToDB_ARCDB(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void FieldLST_ARCDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t FromIUnknown_ARCDB(void*, const int32_t*);


cdef extern void GetIPJ_ARCDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t iExistField_ARCDB(void*, const int32_t*, const void*);


cdef extern int32_t iGetIUnknown_ARCDB(void*, const int32_t*);


cdef extern int32_t iImportChemDatabaseWizard_ARCDB(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t SelTblExGUI_ARCDB(void*, int32_t*);


cdef extern int32_t SelTblGUI_ARCDB(void*);



# Class ARCDH


cdef extern void CloseProject_ARCDH(void*);


cdef extern void SetProject_ARCDH(void*, const void*, const void*);


cdef extern void SetStringFileGDB_ARCDH(void*, const void*);


cdef extern void StopEditingStringFileGDB_ARCDH(void*);


cdef extern int32_t iHasStringFileGDBEdits_ARCDH(void*);


cdef extern int32_t iGeostringsExtensionAvailable_ARCDH(void*);


cdef extern void GetCurrentStringFileGDB_ARCDH(void*, void*, const int32_t*);


cdef extern int32_t iIsValidFGDBFileName_ARCDH(void*, const void*);


cdef extern int32_t iIsValidFeatureClassName_ARCDH(void*, const void*);


cdef extern void sPromptForESRISymbol_ARCDH(void*, int32_t, const void*, const int32_t*, void*, const int32_t*, int32_t*, int32_t*);



# Class ARCMAP


cdef extern void ChangeSize_ARCMAP(void*, const double*, const double*);


cdef extern void DisplayIn3DView_ARCMAP(void*, const void*);


cdef extern void ExportFeatureLayerByNameTo3DFile_ARCMAP(void*, const void*, const void*, const void*, const void*);


cdef extern void ExportSelectedFeatureLayerTo3DFile_ARCMAP(void*, const void*);


cdef extern void GetCurrentDocumentInfo_ARCMAP(void*, void*, void*, void*, const int32_t*);


cdef extern void GetSelectedLayerInfo_ARCMAP(void*, const int32_t*, void*, void*, const int32_t*);


cdef extern int32_t iGetNumberOfSelectedLayers_ARCMAP(void*);


cdef extern int32_t iLoadMAP_ARCMAP(void*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t iLoadMAPEx_ARCMAP(void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t iLoadShape_ARCMAP(void*, const void*, const int32_t*);


cdef extern int32_t iLoadSPF_ARCMAP(void*, const void*, const int32_t*);


cdef extern void LoadLYR_ARCMAP(void*, const void*);


cdef extern void LoadMap_ARCMAP(void*, const void*, const void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LoadMapView_ARCMAP(void*, const void*, const void*, const void*, const int32_t*);


cdef extern void LoadRaster_ARCMAP(void*, const void*);


cdef extern void LoadShape_ARCMAP(void*, const void*, const void*, const void*);


cdef extern void MapViewToShape_ARCMAP(void*, const void*, const void*, const void*, const int32_t*);


cdef extern void QuerySize_ARCMAP(void*, double*, double*);


cdef extern void ShowLayerByNameIn3D_ARCMAP(void*, const void*, const void*, const void*);


cdef extern void ShowSelectedLayersIn3D_ARCMAP(void*);


cdef extern void GetIPJForPredefinedEsriGCS_ARCMAP(void*, const int32_t*, const int32_t*);


cdef extern void GetIPJForPredefinedEsriPCS_ARCMAP(void*, const int32_t*, const int32_t*);



# Class ARCSYS


cdef extern void IGetBrowseLoc_ARCSYS(void*, void*, const int32_t*);


cdef extern void IGetCurrentDoc_ARCSYS(void*, void*, const int32_t*);


cdef extern void SetBrowseLoc_ARCSYS(void*, const void*);



# Class BIGRID


cdef extern void _Clear_BIGRID(void*, const int32_t*);


cdef extern int32_t Create_BIGRID(void*);


cdef extern void Destroy_BIGRID(void*, const int32_t*);


cdef extern int32_t iLoadParms_BIGRID(void*, const int32_t*, const void*);


cdef extern int32_t iLoadWarp_BIGRID(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void Run_BIGRID(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void Run2_BIGRID(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SaveParms_BIGRID(void*, const int32_t*, const void*);



# Class CHIMERA


cdef extern void BarPlot_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void CategorizeByValue_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CategorizeByValueDetLimit_CHIMERA(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void ClipToDetectLimit_CHIMERA(void*, const int32_t*, const double*, const int32_t*);


cdef extern void DrawCircleOffsetMarkers_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void DrawRectangleOffsetMarkers_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void DuplicateChem_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const void*, const void*, const double*, const double*, const double*, const double*);


cdef extern void DuplicateChemView_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*, double*);


cdef extern void GetExpressionDataVV_CHIMERA(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern void GetLithogeochemData_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetTransform_CHIMERA(void*, const int32_t*, const void*, const int32_t*, int32_t*, double*);


cdef extern int32_t iIsAcquireChan_CHIMERA(void*, const void*, void*, const int32_t*, void*, const int32_t*, double*, int32_t*);


cdef extern int32_t iIsElement_CHIMERA(void*, const void*, const int32_t*);


cdef extern void LaunchHistogram_CHIMERA(void*, const void*, const void*);


cdef extern void LaunchProbability_CHIMERA(void*, const void*, const void*);


cdef extern void LaunchScatter_CHIMERA(void*, const void*);


cdef extern void LaunchTriplot_CHIMERA(void*, const void*);


cdef extern void MaskChanLST_CHIMERA(void*, const int32_t*, const int32_t*);


cdef extern void OrderedChannelLST_CHIMERA(void*, const int32_t*, const int32_t*);


cdef extern void PiePlot_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void PiePlot2_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void PlotStringClassifiedSymbolsLegendFromClassFile_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const void*, const int32_t*);


cdef extern double rAtomicWeight_CHIMERA(void*, const void*);


cdef extern void RosePlot_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void RosePlot2_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void Scatter2_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FixedSymbolScatterPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void ZoneColouredScatterPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void StringClassifiedScatterPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void SetLithogeochemData_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void StackedBarPlot_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void Standard_CHIMERA(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const void*, const void*, const double*, const double*, const double*, const double*);


cdef extern void StandardView_CHIMERA(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const void*, const void*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*, double*);


cdef extern void TriPlot2_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void FixedSymbolTriPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const double*, const void*);


cdef extern void ZoneColouredTriPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const double*, const void*);


cdef extern void StringClassifiedTriPlot_CHIMERA(void*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const double*, const void*);



# Class COM


cdef extern int32_t Create_COM(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateNoTerminate_COM(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Destroy_COM(void*, const int32_t*);


cdef extern int32_t IiReadLineNoTerminate_COM(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iReadCharsNoTerminate_COM(void*, const int32_t*, void*, const int32_t*);


cdef extern void IReadLine_COM(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iWriteCharsNoTerminate_COM(void*, const int32_t*, const void*);


cdef extern void PurgeComm_COM(void*, const int32_t*);


cdef extern void ReadChars_COM(void*, const int32_t*, void*, const int32_t*);


cdef extern void ReadEM61LinesWA_COM(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReadFile2WA_COM(void*, const int32_t*, const int32_t*);


cdef extern void ReadLinesWA_COM(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetTimeOut_COM(void*, const int32_t*, const int32_t*);


cdef extern void WriteChars_COM(void*, const int32_t*, const void*);


cdef extern void WriteLine_COM(void*, const int32_t*, const void*);



# Class CSYMB


cdef extern void _SetAngle_CSYMB(void*, const int32_t*, const double*);


cdef extern void _SetBase_CSYMB(void*, const int32_t*, const double*);


cdef extern void _SetDynamicCol_CSYMB(void*, const int32_t*, const int32_t*);


cdef extern void _SetFixed_CSYMB(void*, const int32_t*, const int32_t*);


cdef extern void _SetNumber_CSYMB(void*, const int32_t*, const int32_t*);


cdef extern void _SetScale_CSYMB(void*, const int32_t*, const double*);


cdef extern void AddData_CSYMB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_CSYMB(void*, const void*);


cdef extern void Destroy_CSYMB(void*, const int32_t*);


cdef extern void SetFont_CSYMB(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetStaticCol_CSYMB(void*, const int32_t*, const int32_t*, const int32_t*);



# Class DGW


cdef extern int32_t App_Create_DGW(void*, const void*);


cdef extern void App_Destroy_DGW(void*, const int32_t*);


cdef extern void App_GetInfoMETA_DGW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_GetInfoSYS_DGW(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern int32_t App_GetList_DGW(void*, const int32_t*, const int32_t*);


cdef extern void App_GtInfo_DGW(void*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iRunDialogue_DGW(void*, const int32_t*);


cdef extern void App_SetInfo_DGW(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void App_SetInfoMETA_DGW(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetInfoSYS_DGW(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void App_SetTitle_DGW(void*, const int32_t*, const void*);



# Class DH

# ArcGIS Target Functions




cdef extern int32_t iIsESRI_DH(void*);


# Data processing/conversion methods




cdef extern void CreatChanLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void DepthDataLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void FromToDataLST_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetGeologyContacts_DH(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetOrientedCoreDipDir_DH(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const void*, const void*);


cdef extern void GetUniqueChannelItems_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void GetUniqueChannelItemsFromCollar_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t iChanType_DH(void*, const int32_t*, const void*);


cdef extern int32_t iFindHoleIntersection_DH(void*, const int32_t*, const int32_t*, const int32_t*, double*, double*, double*);


cdef extern void IGetChanCodeInfo_DH(void*, const int32_t*, const void*, int32_t*, void*, const int32_t*);


cdef extern int32_t iGridIntersection_DH(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const void*, double*, double*, double*);


cdef extern void LithoGrid3D_DH(void*, const int32_t*, const void*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void NumericChanLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void NumericFromToDataLST_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void PunchGridHoles_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void StringChanLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void StringFromToDataLST_DH(void*, const int32_t*, const void*, const int32_t*);


# Miscellaneous




cdef extern int32_t _hAssayDB_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t _hAssaySymb_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t _hCollarDB_DH(void*, const int32_t*);


cdef extern int32_t _hCollarSymb_DH(void*, const int32_t*);


cdef extern int32_t _hDipAzSurveyDB_DH(void*, const int32_t*);


cdef extern int32_t _hDipAzSurveySymb_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t _hENSurveyDB_DH(void*, const int32_t*);


cdef extern int32_t _hENSurveySymb_DH(void*, const int32_t*, const int32_t*);


cdef extern void AddSurveyTable_DH(void*, const int32_t*, const int32_t*);


cdef extern void AssayHoleLST_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AssayLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void AutoSelectHoles_DH(void*, const int32_t*);


cdef extern void Clean_DH(void*, const int32_t*);


cdef extern void CompositeDB_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const void*, const void*, const void*, const double*, const double*, const double*, const int32_t*, const void*);


cdef extern void ComputeHoleXYZ_DH(void*, const int32_t*, const int32_t*);


cdef extern void ComputeSelExtent_DH(void*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void ComputeXYZ_DH(void*, const int32_t*);


cdef extern void ConvertOldLineNames_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_DH(void*, const void*);


cdef extern void CreateDefaultJob_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t CreateExternal_DH(void*, const void*);


cdef extern int32_t Current_DH(void*);


cdef extern void DatamineToCSV_DH(void*, const void*, const void*);


cdef extern void DeleteHoles_DH(void*, const int32_t*, const int32_t*);


cdef extern void Destroy_DH(void*, const int32_t*);


cdef extern void Export_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void ExportGeodatabaseLST_DH(void*, const int32_t*, const int32_t*, const void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern void ExportLAS_DH(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const void*);


cdef extern void ExportLST_DH(void*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void FlushSelect_DH(void*, const int32_t*);


cdef extern void GetDatabasesVV_DH(void*, const int32_t*, const int32_t*);


cdef extern void GetDatabasesSortedVV_DH(void*, const int32_t*, const int32_t*);


cdef extern void GetDataType_DH(void*, const int32_t*, const int32_t*, int32_t*);


cdef extern void GetDefaultSection_DH(void*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern int32_t GetHoleGroup_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void GetHoleSurvey_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetIPJ_DH(void*, const int32_t*, const int32_t*);


cdef extern void GetMapNamesVV_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetMap_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t GetNumMaps_DH(void*, const int32_t*);


cdef extern int32_t GetREG_DH(void*, const int32_t*);


cdef extern void GetSelectedHolesVV_DH(void*, const int32_t*, const int32_t*);


cdef extern void GetTableDefaultChanLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void HoleLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void HoleLST2_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iAddHole_DH(void*, const int32_t*, const void*);


cdef extern int32_t iCleanWillDeleteDB_DH(void*, const int32_t*);


cdef extern int32_t iCompositingToolGUI_DH(void*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void ICreateCollarTable_DH(void*, const void*, const int32_t*, void*, const int32_t*);


cdef extern void ICreateCollarTableDir_DH(void*, const void*, const void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iDeleteWillDeleteDB_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iFindHole_DH(void*, const int32_t*, const void*);


cdef extern void IGetCollarTableDB_DH(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetInfo_DH(void*, const int32_t*, const int32_t*, const void*, void*, const int32_t*);


cdef extern void IGetProjectName_DH(void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetSectionID_DH(void*, const double*, const double*, const double*, void*, const int32_t*);


cdef extern int32_t iGetTemplateBlob_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern void IGetTemplateInfo_DH(void*, const void*, int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetTemplateInfoEx_DH(void*, const void*, int32_t*, void*, const int32_t*, void*, const int32_t*, const int32_t*);


cdef extern void IGetUnits_DH(void*, const int32_t*, void*, const int32_t*, double*);


cdef extern int32_t iHaveCurrent_DH(void*);


cdef extern int32_t IiHaveCurrent2_DH(void*, void*, const int32_t*);


cdef extern int32_t iHoles_DH(void*, const int32_t*);


cdef extern int32_t iHoleSelectFromListGUI_DH(void*, const int32_t*, const int32_t*);


cdef extern int32_t iHoleSelectionToolGUI_DH(void*, const int32_t*);


cdef extern int32_t iModify3dGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyCrookedSectionHolesGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyFenceGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyHoleTraces3DGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyHoleTracesGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyHoleTracesGUI2_DH(void*, const int32_t*, const void*, const int32_t*, int32_t*);


cdef extern int32_t iModifyPlanGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyPlanHolesGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyRockCodesGUI_DH(void*, const void*);


cdef extern int32_t iModifyRockCodesGUI2_DH(void*, const int32_t*, const void*);


cdef extern int32_t iModifySectionGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifySectionHolesGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyStackedSectionGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyStripLogGUI_DH(void*, const int32_t*, const void*, int32_t*);


cdef extern int32_t iModifyStructureCodesGUI_DH(void*, const void*);


cdef extern int32_t iModifyStructureCodesGUI2_DH(void*, const int32_t*, const void*);


cdef extern void Import2_DH(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const void*);


cdef extern void ImportLAS_DH(void*, const int32_t*, const void*, const void*, const double*, const int32_t*, const int32_t*);


cdef extern int32_t iNumAssays_DH(void*, const int32_t*);


cdef extern int32_t iNumSelectedHoles_DH(void*, const int32_t*);


cdef extern int32_t iQADipAzCurvatureLST_DH(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern int32_t iQADipAzSurveyLST_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iQAEastNorthCurvatureLST_DH(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern int32_t iQAEastNorthSurveyLST_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iSliceSelectionToolGUI_DH(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, double*, double*, double*, double*);


cdef extern int32_t iUpdateSurveyFromCollar_DH(void*, const int32_t*, const int32_t*);


cdef extern void LoadDataParametersINI_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void LoadPlotParameters_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void LoadSelect_DH(void*, const int32_t*, const void*);


cdef extern void MaskPLY_DH(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t Open_DH(void*, const void*);


cdef extern void OpenJob_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void PlotHoleTraces_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void PlotHoleTraces3D_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void PlotSymbols3D_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void QACollar_DH(void*, const int32_t*, const int32_t*);


cdef extern void QACollarLST_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void QADipAzCurvature_DH(void*, const int32_t*, const int32_t*, const double*);


cdef extern void QADipAzCurvature2_DH(void*, const int32_t*, const int32_t*, const double*, const void*);


cdef extern void QADipAzSurvey_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void QAEastNorthCurvature_DH(void*, const int32_t*, const int32_t*, const double*);


cdef extern void QAEastNorthCurvature2_DH(void*, const int32_t*, const int32_t*, const double*, const void*);


cdef extern void QAEastNorthSurvey_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void QAFromToData_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void QAPointData_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void QAWriteUnregisteredHoles_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReplotHoles_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void PlotHolesOnSection_DH(void*, const int32_t*, const void*, const int32_t*, const void*);


cdef extern void ReSurveyEastNorth_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, double*);


cdef extern void ReSurveyPolFit_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReSurveyRadCurve_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReSurveyStraight_DH(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReSurveyStraightSeg_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SaveDataParametersINI_DH(void*, const int32_t*, const int32_t*, const void*);


cdef extern void SaveJob_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SaveSelect_DH(void*, const int32_t*, const void*);


cdef extern void SectionWindowSizeMM_DH(void*, const int32_t*, double*, double*);


cdef extern void SelectAllHoles_DH(void*, const int32_t*);


cdef extern void SelectHoles_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SelectName_DH(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void SelectPLY_DH(void*, const int32_t*, const int32_t*);


cdef extern void SelectPLY2_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetCrookedSectionIPJ_DH(void*, const int32_t*, const int32_t*);


cdef extern void SetCurrentViewName_DH(void*, const int32_t*, const void*);


cdef extern void SetInfo_DH(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void SetIPJ_DH(void*, const int32_t*, const int32_t*);


cdef extern void SetMAP_DH(void*, const int32_t*, const int32_t*);


cdef extern void SetNewIPJ_DH(void*, const int32_t*, const void*);


cdef extern void SetSelectedHolesVV_DH(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetTemplateBlob_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SignificantIntersectionsDB_DH(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void TestImportLAS_DH(void*, const int32_t*, const void*, const void*, const double*, const int32_t*, int32_t*);


cdef extern void UnSelectAllHoles_DH(void*, const int32_t*);


cdef extern void UnSelectedHoleLST_DH(void*, const int32_t*, const int32_t*);


cdef extern void UpdateCollarTable_DH(void*, const int32_t*);


cdef extern void UpdateHoleExtent_DH(void*, const int32_t*, const int32_t*);


cdef extern void Wholeplot_DH(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SurfaceIntersections_DH(void*, const int32_t*, const int32_t*, const void*, const int32_t*);




# Class DMPPLY


cdef extern void _Clear_DMPPLY(void*, const int32_t*);


cdef extern void Copy_DMPPLY(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_DMPPLY(void*);


cdef extern void Destroy_DMPPLY(void*, const int32_t*);


cdef extern void GetAzimuth_DMPPLY(void*, const int32_t*, const int32_t*, double*);


cdef extern void GetExtents_DMPPLY(void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern void GetJoins_DMPPLY(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetNormalVectors_DMPPLY(void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void GetPoly_DMPPLY(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetSwing_DMPPLY(void*, const int32_t*, const int32_t*, double*);


cdef extern void GetVertex_DMPPLY(void*, const int32_t*, const int32_t*, const int32_t*, double*, double*, double*);


cdef extern int32_t iNumJoins_DMPPLY(void*, const int32_t*);


cdef extern int32_t iNumPolys_DMPPLY(void*, const int32_t*);


cdef extern int32_t iNumVertices_DMPPLY(void*, const int32_t*, const int32_t*);


cdef extern void Load_DMPPLY(void*, const int32_t*, const void*);


cdef extern void MoveVertex_DMPPLY(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void ProjectPoly_DMPPLY(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReProjectPoly_DMPPLY(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Save_DMPPLY(void*, const int32_t*, const void*);


cdef extern void SetPoly_DMPPLY(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class DOCU


cdef extern void Copy_DOCU(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_DOCU(void*);


cdef extern int32_t CreateS_DOCU(void*, const int32_t*);


cdef extern void Destroy_DOCU(void*, const int32_t*);


cdef extern void GetFile_DOCU(void*, const int32_t*, const void*);


cdef extern void GetFileMeta_DOCU(void*, const int32_t*, const void*);


cdef extern void GetMETA_DOCU(void*, const int32_t*, const int32_t*);


cdef extern void IDocName_DOCU(void*, const int32_t*, void*, const int32_t*);


cdef extern void IFileName_DOCU(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iHaveMETA_DOCU(void*, const int32_t*);


cdef extern int32_t iIsReference_DOCU(void*, const int32_t*);


cdef extern void Open_DOCU(void*, const int32_t*, const int32_t*);


cdef extern void Serial_DOCU(void*, const int32_t*, const int32_t*);


cdef extern void SetFile_DOCU(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void SetFileMeta_DOCU(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void SetMETA_DOCU(void*, const int32_t*, const int32_t*);



# Class DU


cdef extern void _TableLook1_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void _TableLook2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void _TableLookI2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void _TableLookR2_DU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void ADOTableNames_DU(void*, const void*, const int32_t*);


cdef extern void AnSig_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Append_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AvgAzimuth_DU(void*, const int32_t*, const double*, double*);


cdef extern void BaseData_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BaseDataEx_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BoundLine_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BPFilt_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void BreakLine_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BreakLine2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BreakLineToGroups_DU(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void BreakLineToGroups2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void BSpline_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void ClosestPoint_DU(void*, const int32_t*, const double*, const double*, double*, double*, int32_t*, double*);


cdef extern void CopyLine_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CopyLineAcross_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CopyLineChanAcross_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void CopyLineMasked_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DAOTableNames_DU(void*, const void*, const void*, const int32_t*);


cdef extern void Decimate_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Diff_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Distance_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Distance3D_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Distline_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*);


cdef extern void DupChanLocks_DU(void*, const int32_t*, const int32_t*);


cdef extern void DupChans_DU(void*, const int32_t*, const int32_t*);


cdef extern void EditDuplicates_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void Export_DU(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void Export2_DU(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExportAMIRA_DU(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*);


cdef extern void ExportAseg_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ExportAsegProj_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern void ExportChanCRC_DU(void*, const int32_t*, const int32_t*, int32_t*, const void*);


cdef extern void ExportCSV_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void ExportDatabaseCRC_DU(void*, const int32_t*, int32_t*, const void*);


cdef extern void ExportGBN_DU(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ExportMDB_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void ExportGeodatabase_DU(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t GetExistingFeatureClassesInGeodatabase_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void ExportSHP_DU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void ExportXYZ_DU(void*, const int32_t*, const void*, const void*);


cdef extern void ExportXYZ2_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FFT_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Filter_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GenLev_DU(void*, const int32_t*, const void*, const void*, const double*, const int32_t*);


cdef extern void GenLevDB_DU(void*, const int32_t*, const void*, const double*, const int32_t*);


cdef extern void GenXYZTemp_DU(void*, const void*, const void*);


cdef extern void GetXYZNumFields_DU(void*, const void*, int32_t*);


cdef extern void GetChanDataLST_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetChanDataVV_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Gradient_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void GravDrift_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GravTide_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void GridLoad_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GridLoadXYZ_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Head_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void IImportBIN3_DU(void*, const int32_t*, const void*, const void*, void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void ImpCBPly_DU(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void ImportADO_DU(void*, const int32_t*, const void*, const void*, const void*, const void*);


cdef extern void ImportAllADO_DU(void*, const int32_t*, const void*, const int32_t*);


cdef extern void ImportAllDAO_DU(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void ImportAMIRA_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ImportAseg_DU(void*, const int32_t*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void ImportAsegProj_DU(void*, const int32_t*, const void*, const void*, const void*, const void*, const int32_t*, const void*, const void*, const void*);


cdef extern void ImportBIN_DU(void*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*);


cdef extern void ImportBIN2_DU(void*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void ImportBIN4_DU(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*, const int32_t*);


cdef extern void ImportDAARC500Serial_DU(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void ImportDAARC500SerialGPS_DU(void*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void ImportDAO_DU(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*);


cdef extern void ImportESRI_DU(void*, const int32_t*, const void*, const void*, const void*);


cdef extern void ImportGBN_DU(void*, const int32_t*, const void*);


cdef extern void ImportODDF_DU(void*, const int32_t*, const void*);


cdef extern void ImportPico_DU(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void ImportUBCModMsh_DU(void*, const int32_t*, const void*, const void*, const int32_t*, const double*);


cdef extern void ImportUSGSPost_DU(void*, const int32_t*, const void*);


cdef extern void ImportXYZ_DU(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ImportXYZ2_DU(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void ImportIoGAS_DU(void*, const int32_t*, const void*, const void*);


cdef extern void IndexOrder_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Interp_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void InterpGap_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Intersect_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const void*);


cdef extern void IntersectAll_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const void*);


cdef extern void IntersectGDBtoTBL_DU(void*, const void*, const void*);


cdef extern void IntersectOld_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void IntersectTBLtoGDB_DU(void*, const void*, const void*);


cdef extern void LabTemplate_DU(void*, const void*, const void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LoadGravity_DU(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void LoadLTB_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MakeFid_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Mask_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Math_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MergeLine_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ModFidRange_DU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Move_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void NLFilt_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void Normal_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyFill_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyMask_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ProjectData_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ProjectXYZ_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ProjPoints_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void QCInitSeparation_DU(void*, const int32_t*, const double*, const double*);


cdef extern int32_t QCSurveyPlan_DU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern double rDirection_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReFid_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void ReFidAllCh_DU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ReFidCh_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Rotate_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void SampleGD_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SampleIMG_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SampleIMGLineLST_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ScanADO_DU(void*, const void*, const void*, const void*);


cdef extern void ScanAseg_DU(void*, const void*, const void*, const void*, const void*);


cdef extern void ScanDAO_DU(void*, const void*, const void*, const void*, const void*);


cdef extern void ScanPico_DU(void*, const void*, const void*);


cdef extern void Sort_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SortIndex_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SortIndex2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SplitLine_DU(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void SplitLine2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void SplitLineXY_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, int32_t*, const int32_t*);


cdef extern void SplitLineXY2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, int32_t*, const int32_t*, const int32_t*);


cdef extern void SplitLineXY3_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SplitLineByDirection_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, int32_t*, const int32_t*, const int32_t*);


cdef extern void SplitLineByDirection2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Stat_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TableLineFid_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TableSelectedLinesFid_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TimeConstant_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Trend_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void UpdateIntersectDB_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void VoxelSection_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const double*, const int32_t*);


cdef extern void WriteWA_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void XyzLine_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void XyzLine2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void XyzLine3_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void ZMask_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void RangeXY_DU(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void RangeXYZ_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*, double*, int32_t*);


cdef extern void RangeXYZData_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, int32_t*);


cdef extern void CreateDrillholeParameterWeightConstraintDatabase_DU(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void CalculateDrapedSurveyAltitude_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const double*, const double*);


cdef extern void CalculateDrapedSurveyAltitude2_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const double*);


cdef extern void DirectGridDataToVoxel_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern void DirectGridItemCountsToVoxel_DU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*);



# Class DXFI


cdef extern int32_t Create_DXFI(void*, const void*);


cdef extern void Destroy_DXFI(void*, const int32_t*);


cdef extern void DXF2PLY_DXFI(void*, const int32_t*, const int32_t*);


cdef extern void DXF2ViewEx_DXFI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void GetRange_DXFI(void*, const int32_t*, double*, double*, double*, double*, double*, double*);



# Class EDB

# Miscellaneous




cdef extern void App_ApplyFormulaInternal_EDB(void*, const int32_t*, const void*);


cdef extern int32_t App_Current_EDB(void*);


cdef extern int32_t App_CurrentNoActivate_EDB(void*);


cdef extern int32_t App_CurrentIfExists_EDB(void*);


cdef extern void App_DelLine0_EDB(void*, const int32_t*);


cdef extern void App_Destroy_EDB(void*, const int32_t*);


cdef extern void App_DestroyView_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_GetCurChanSymb_EDB(void*, const int32_t*);


cdef extern int32_t App_GetCurLineSymb_EDB(void*, const int32_t*);


cdef extern void App_GetDisplFidRange_EDB(void*, const int32_t*, int32_t*, int32_t*);


cdef extern void App_GetFidRange_EDB(void*, const int32_t*, double*, double*, int32_t*);


cdef extern int32_t App_GetNextLineSymb_EDB(void*, const int32_t*);


cdef extern int32_t App_GetPrevLineSymb_EDB(void*, const int32_t*);


cdef extern void App_GetProfileRangeX_EDB(void*, const int32_t*, double*, double*, int32_t*);


cdef extern void App_GetProfileRangeY_EDB(void*, const int32_t*, const int32_t*, const int32_t*, double*, double*, int32_t*);


cdef extern void App_GetProfileSplit_EDB(void*, const int32_t*, double*, double*);


cdef extern void App_GetProfileSplit5_EDB(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void App_GetProfileSplitVV_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_GetProfileVerticalGridLines_EDB(void*, const int32_t*, int32_t*, double*);


cdef extern void App_GetProfileWindow_EDB(void*, const int32_t*, const int32_t*, int32_t*, int32_t*);


cdef extern void App_GotoColumn_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_GotoElem_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_GotoLine_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_Histogram_EDB(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern int32_t App_iAllChanList_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iChannels_EDB(void*, const int32_t*);


cdef extern int32_t App_iDispChanList_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iDispChanLST_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iDispClassChanLST_EDB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t App_iFindChannelColumn_EDB(void*, const int32_t*, const void*);


cdef extern int32_t App_iFindNearest_EDB(void*, const int32_t*, double*, double*, double*, const int32_t*);


cdef extern void App_IGetCurChan_EDB(void*, const int32_t*, void*, const int32_t*);


cdef extern void App_IGetCurFidString_EDB(void*, const int32_t*, void*, const int32_t*);


cdef extern void App_IGetCurLine_EDB(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iGetCurMark_EDB(void*, const int32_t*, double*, double*, double*);


cdef extern void App_IGetCurrentSelection_EDB(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iGetDatabasesLST_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetMarkChanVV_EDB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetMarkChanVA_EDB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_IGetName_EDB(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iGetProfileParm_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetWindowState_EDB(void*, const int32_t*);


cdef extern int32_t App_iHaveCurrent_EDB(void*);


cdef extern int32_t App_iIsLocked_EDB(void*, const int32_t*);


cdef extern int32_t App_iLoaded_EDB(void*, const void*);


cdef extern int32_t App_iProfileOpen_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iReadOnly_EDB(void*, const int32_t*);


cdef extern void App_GetWindowPosition_EDB(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_SetWindowPosition_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iShowProfileName_EDB(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t App_iGetWindowYAxisDirection_EDB(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iWindowProfiles_EDB(void*, const int32_t*, const int32_t*);


cdef extern void LaunchHistogram_EDB(void*, const int32_t*, const void*);


cdef extern void LaunchScatter_EDB(void*, const int32_t*);


cdef extern int32_t App_Load_EDB(void*, const void*);


cdef extern int32_t App_LoadNoActivate_EDB(void*, const void*);


cdef extern void App_LoadAllChans_EDB(void*, const int32_t*);


cdef extern void App_LoadChan_EDB(void*, const int32_t*, const void*);


cdef extern int32_t App_LoadNew_EDB(void*, const void*);


cdef extern int32_t App_LoadPass_EDB(void*, const void*, const void*, const void*);


cdef extern int32_t App_LoadWithView_EDB(void*, const void*, const int32_t*);


cdef extern int32_t App_Lock_EDB(void*, const int32_t*);


cdef extern void App_MakeCurrent_EDB(void*, const int32_t*);


cdef extern void App_RemoveProfile_EDB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double App_rGetCurFid_EDB(void*, const int32_t*);


cdef extern double App_rGetProfileParm_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern double App_rGetSplit_EDB(void*, const int32_t*);


cdef extern void App_RunChannelMaker_EDB(void*, const int32_t*, const void*);


cdef extern void App_RunChannelMakers_EDB(void*, const int32_t*);


cdef extern void App_SetCurLine_EDB(void*, const int32_t*, const void*);


cdef extern void App_SetCurLineNoMessage_EDB(void*, const int32_t*, const void*);


cdef extern void App_SetCurMark_EDB(void*, const int32_t*, const double*, const double*);


cdef extern void App_SetProfileParmI_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetProfileParmR_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void App_SetProfileRangeX_EDB(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void App_SetProfileRangeY_EDB(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void App_SetProfileSplit_EDB(void*, const int32_t*, const double*, const double*);


cdef extern void App_SetProfileSplit5_EDB(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_SetProfileSplitVV_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_SetSplit_EDB(void*, const int32_t*, const double*);


cdef extern void App_SetWindowState_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_ShowProfile_EDB(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_Statistics_EDB(void*, const int32_t*, const int32_t*);


cdef extern void App_UnLoad_EDB(void*, const void*);


cdef extern void App_UnLoadAll_EDB(void*);


cdef extern void App_UnLoadAllChans_EDB(void*, const int32_t*);


cdef extern void App_UnLoadChan_EDB(void*, const int32_t*, const void*);


cdef extern void App_UnLoadDiscard_EDB(void*, const void*);


cdef extern void App_UnLoadVerify_EDB(void*, const void*, const int32_t*);


cdef extern void App_UnLock_EDB(void*, const int32_t*);


# External Window




cdef extern void App_LoadControl_EDB(void*, const void*, int32_t);


cdef extern void App_LoadNewControl_EDB(void*, const void*, int32_t);


cdef extern void App_LoadPassControl_EDB(void*, const void*, const void*, const void*, int32_t);


cdef extern void App_LoadWithViewControl_EDB(void*, const void*, const int32_t*, int32_t);




# Class EDOC

# GMSYS 3D Models




cdef extern int32_t App_CreateNewGMS3D_EDOC(void*, const void*, const int32_t*, const int32_t*, const int32_t*);


# Miscellaneous




cdef extern int32_t App_Current_EDOC(void*, const int32_t*);


cdef extern int32_t App_CurrentNoActivate_EDOC(void*, const int32_t*);


cdef extern int32_t App_CurrentIfExists_EDOC(void*, const int32_t*);


cdef extern void App_Destroy_EDOC(void*, const int32_t*);


cdef extern int32_t App_iGetDocumentsLST_EDOC(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_IGetName_EDOC(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iGetWindowState_EDOC(void*, const int32_t*);


cdef extern int32_t App_iHaveCurrent_EDOC(void*, const int32_t*);


cdef extern int32_t App_iLoaded_EDOC(void*, const void*, const int32_t*);


cdef extern void App_GetWindowPosition_EDOC(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_SetWindowPosition_EDOC(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iReadOnly_EDOC(void*, const int32_t*);


cdef extern int32_t App_Load_EDOC(void*, const void*, const int32_t*);


cdef extern int32_t App_LoadNoActivate_EDOC(void*, const void*, const int32_t*);


cdef extern void App_MakeCurrent_EDOC(void*, const int32_t*);


cdef extern void App_SetWindowState_EDOC(void*, const int32_t*, const int32_t*);


cdef extern void App_Sync_EDOC(void*, const void*, const int32_t*);


cdef extern void App_SyncOpen_EDOC(void*, const int32_t*);


cdef extern void App_UnLoad_EDOC(void*, const void*, const int32_t*);


cdef extern void App_UnLoadAll_EDOC(void*, const int32_t*);


cdef extern void App_UnLoadDiscard_EDOC(void*, const void*, const int32_t*);


cdef extern void App_UnLoadVerify_EDOC(void*, const void*, const int32_t*, const int32_t*);




# Class EMAP

# Drag-and-drop methods




cdef extern void App_DropMapClipData_EMAP(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iDragDropEnabled_EMAP(void*, const int32_t*);


cdef extern void App_SetDragDropEnabled_EMAP(void*, const int32_t*, const int32_t*);


# Drawing




cdef extern void App_CopyToClip_EMAP(void*, const int32_t*);


cdef extern void App_DrawLine_EMAP(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_DrawRect_EMAP(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_DrawRect3D_EMAP(void*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern void App_GetDisplayArea_EMAP(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void App_GetDisplayAreaRaw_EMAP(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void App_GetMapLayoutProps_EMAP(void*, const int32_t*, int32_t*, double*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_GetMapSnap_EMAP(void*, const int32_t*, double*);


cdef extern int32_t App_iGetWindowState_EMAP(void*, const int32_t*);


cdef extern void App_SetDisplayArea_EMAP(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_SetMapLayoutProps_EMAP(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetMapSnap_EMAP(void*, const int32_t*, const double*);


cdef extern void App_SetWindowState_EMAP(void*, const int32_t*, const int32_t*);


# General




cdef extern void App_ActivateGroup_EMAP(void*, const int32_t*, const void*);


cdef extern void App_ActivateView_EMAP(void*, const int32_t*, const void*);


cdef extern int32_t App_Current_EMAP(void*);


cdef extern int32_t App_CurrentNoActivate_EMAP(void*);


cdef extern int32_t App_CurrentIfExists_EMAP(void*);


cdef extern void App_Destroy_EMAP(void*, const int32_t*);


cdef extern void App_DestroyView_EMAP(void*, const int32_t*, const int32_t*);


cdef extern void App_FontLST_EMAP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iChangeCurrentView_EMAP(void*, const int32_t*, const void*);


cdef extern int32_t App_iCreateGroupSnapshot_EMAP(void*, const int32_t*, const int32_t*);


cdef extern void App_IGet3DViewName_EMAP(void*, const int32_t*, void*, const int32_t*);


cdef extern void App_IGetCurrentGroup_EMAP(void*, const int32_t*, void*, const int32_t*);


cdef extern void App_IGetCurrentView_EMAP(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iGetMapsLST_EMAP(void*, const int32_t*, const int32_t*);


cdef extern void App_IGetName_EMAP(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iHaveCurrent_EMAP(void*);


cdef extern int32_t App_iIGetSpecifiedMapName_EMAP(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iIsGrid_EMAP(void*, const int32_t*);


cdef extern void App_ReloadGrid_EMAP(void*, const void*);


cdef extern int32_t App_iIs3DView_EMAP(void*, const int32_t*);


cdef extern int32_t App_iIsLocked_EMAP(void*, const int32_t*);


cdef extern int32_t App_iLoaded_EMAP(void*, const void*);


cdef extern int32_t App_iReadOnly_EMAP(void*, const int32_t*);


cdef extern void App_GetWindowPosition_EMAP(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_SetWindowPosition_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iRealizeGroupSnapshot_EMAP(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iSetCurrentView_EMAP(void*, const int32_t*, const void*);


cdef extern void App_GetViewIPJ_EMAP(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t App_Load_EMAP(void*, const void*);


cdef extern int32_t App_LoadNoActivate_EMAP(void*, const void*);


cdef extern int32_t App_LoadWithView_EMAP(void*, const void*, const int32_t*);


cdef extern int32_t App_Lock_EMAP(void*, const int32_t*);


cdef extern void App_MakeCurrent_EMAP(void*, const int32_t*);


cdef extern void App_Print_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void App_Redraw_EMAP(void*, const int32_t*);


cdef extern void App_SelectGroup_EMAP(void*, const int32_t*, const void*);


cdef extern void App_SetRedrawFlag_EMAP(void*, const int32_t*, const int32_t*);


cdef extern void App_UnLoad_EMAP(void*, const void*);


cdef extern void App_UnLoadAll_EMAP(void*);


cdef extern void App_UnLoadVerify_EMAP(void*, const void*, const int32_t*);


cdef extern void App_UnLock_EMAP(void*, const int32_t*);


# Input




cdef extern void App_GetCurPoint_EMAP(void*, const int32_t*, double*, double*);


cdef extern void App_GetCurPointMM_EMAP(void*, const int32_t*, double*, double*);


cdef extern void App_GetCursor_EMAP(void*, const int32_t*, double*, double*);


cdef extern void App_GetCursorMM_EMAP(void*, const int32_t*, double*, double*);


cdef extern int32_t App_iDigitize_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t App_iDigitize2_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t App_iDigitizePeaks_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t App_iDigitizePolygon_EMAP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetBox_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iGetBox2_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t App_iGetGrid_EMAP(void*, const int32_t*, const void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern int32_t App_iGetLine_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iGetLineEx_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iGetLineXYZ_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*, double*, double*);


cdef extern int32_t App_iGetPoint_EMAP(void*, const int32_t*, const void*, double*, double*);


cdef extern int32_t App_iGetPointEx_EMAP(void*, const int32_t*, const void*, double*, double*);


cdef extern int32_t App_iGetPoint3D_EMAP(void*, const int32_t*, const void*, double*, double*, double*);


cdef extern int32_t App_iGetPolyLine_EMAP(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetPolyLineXYZ_EMAP(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetRect_EMAP(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iTrackPoint_EMAP(void*, const int32_t*, const int32_t*, double*, double*);


# Map Viewport Mode Methods




cdef extern void App_GetAOIArea_EMAP(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void App_SetAOIArea_EMAP(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_SetViewportMode_EMAP(void*, const int32_t*, const int32_t*);


# Tracking Methods




cdef extern void App_GetSelectedVertices_EMAP(void*, const int32_t*, const int32_t*, const int32_t*);


# Virtual




cdef extern int32_t App_CreateVirtual_EMAP(void*, const void*);


# External Window




cdef extern void App_LoadControl_EMAP(void*, const void*, int32_t);


cdef extern void App_LoadWithViewControl_EMAP(void*, const void*, const int32_t*, int32_t);




# Class EMAPTEMPLATE

# Drag-and-drop methods




cdef extern int32_t App_iDragDropEnabled_EMAPTEMPLATE(void*, const int32_t*);


cdef extern void App_SetDragDropEnabled_EMAPTEMPLATE(void*, const int32_t*, const int32_t*);


# General




cdef extern int32_t App_Current_EMAPTEMPLATE(void*);


cdef extern int32_t App_CurrentNoActivate_EMAPTEMPLATE(void*);


cdef extern int32_t App_CurrentIfExists_EMAPTEMPLATE(void*);


cdef extern void App_Destroy_EMAPTEMPLATE(void*, const int32_t*);


cdef extern int32_t App_iGetMapTemplatesLST_EMAPTEMPLATE(void*, const int32_t*, const int32_t*);


cdef extern void App_IGetName_EMAPTEMPLATE(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_iHaveCurrent_EMAPTEMPLATE(void*);


cdef extern int32_t App_iIGetSpecifiedMapName_EMAPTEMPLATE(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iIsLocked_EMAPTEMPLATE(void*, const int32_t*);


cdef extern int32_t App_iLoaded_EMAPTEMPLATE(void*, const void*);


cdef extern void App_GetWindowPosition_EMAPTEMPLATE(void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_SetWindowPosition_EMAPTEMPLATE(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iReadOnly_EMAPTEMPLATE(void*, const int32_t*);


cdef extern int32_t App_Load_EMAPTEMPLATE(void*, const void*);


cdef extern int32_t App_LoadNoActivate_EMAPTEMPLATE(void*, const void*);


cdef extern int32_t App_Lock_EMAPTEMPLATE(void*, const int32_t*);


cdef extern void App_MakeCurrent_EMAPTEMPLATE(void*, const int32_t*);


cdef extern void App_UnLoad_EMAPTEMPLATE(void*, const void*);


cdef extern void App_UnLoadAll_EMAPTEMPLATE(void*);


cdef extern void App_UnLoadVerify_EMAPTEMPLATE(void*, const void*, const int32_t*);


cdef extern void App_UnLock_EMAPTEMPLATE(void*, const int32_t*);


# Input




cdef extern int32_t App_iGetBox_EMAPTEMPLATE(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iGetLine_EMAPTEMPLATE(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iGetPoint_EMAPTEMPLATE(void*, const int32_t*, const void*, double*, double*);


cdef extern int32_t App_iGetRect_EMAPTEMPLATE(void*, const int32_t*, const void*, double*, double*, double*, double*);


cdef extern int32_t App_iTrackPoint_EMAPTEMPLATE(void*, const int32_t*, const int32_t*, double*, double*);


# Selection Methods




cdef extern int32_t App_iGetItemSelection_EMAPTEMPLATE(void*, const int32_t*, void*, const int32_t*);


cdef extern void App_SetItemSelection_EMAPTEMPLATE(void*, const int32_t*, const void*);


# View Window




cdef extern void App_GetDisplayArea_EMAPTEMPLATE(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void App_GetTemplateLayoutProps_EMAPTEMPLATE(void*, const int32_t*, int32_t*, double*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern int32_t App_iGetWindowState_EMAPTEMPLATE(void*, const int32_t*);


cdef extern void App_SetDisplayArea_EMAPTEMPLATE(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void App_SetTemplateLayoutProps_EMAPTEMPLATE(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetWindowState_EMAPTEMPLATE(void*, const int32_t*, const int32_t*);


# Virtual




cdef extern int32_t App_CreateVirtual_EMAPTEMPLATE(void*, const void*);




# Class EUL3


cdef extern void _Destr_EUL3(void*, const int32_t*);


cdef extern int32_t Creat_EUL3(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const double*, const double*);


cdef extern void GetResult_EUL3(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Write_EUL3(void*, const int32_t*, const void*);


cdef extern int32_t ExEulerDerive_EUL3(void*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t ExEulerCalc_EUL3(void*, const int32_t*, const double*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class EXP


cdef extern int32_t Create_EXP(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t CreateFile_EXP(void*, const int32_t*, const void*);


cdef extern void Destroy_EXP(void*, const int32_t*);



# Class FFT


cdef extern void AppDens_FFT(void*, const int32_t*, const double*, const double*);


cdef extern void AppSusc_FFT(void*, const int32_t*, const double*);


cdef extern void BandPass_FFT(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void BWorth_FFT(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void RCFilter_FFT(void*, const int32_t*, const double*, const int32_t*);


cdef extern void Contin_FFT(void*, const int32_t*, const double*);


cdef extern void CosRoll_FFT(void*, const int32_t*, const double*, const double*, const double*, const int32_t*);


cdef extern int32_t Create_FFT(void*, const int32_t*, const double*, const int32_t*);


cdef extern int32_t CreateEx_FFT(void*, const int32_t*, const double*, const int32_t*, const double*);


cdef extern int32_t CreateRef_FFT(void*, const int32_t*, const double*, const int32_t*);


cdef extern int32_t CreateRefEx_FFT(void*, const int32_t*, const double*, const int32_t*, const double*, const double*);


cdef extern void Destroy_FFT(void*, const int32_t*);


cdef extern void Gaus_FFT(void*, const int32_t*, const double*, const int32_t*);


cdef extern void GetVV_FFT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void HDrv_FFT(void*, const int32_t*, const double*);


cdef extern void HighPass_FFT(void*, const int32_t*, const double*, const double*);


cdef extern void HInt_FFT(void*, const int32_t*);


cdef extern void Inverse_FFT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LowPass_FFT(void*, const int32_t*, const double*);


cdef extern void RedPol_FFT(void*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern double rNyquist_FFT(void*, const int32_t*);


cdef extern double rSampIncr_FFT(void*, const int32_t*);


cdef extern double rWaveIncr_FFT(void*, const int32_t*);


cdef extern void SetVV_FFT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Spectrum_FFT(void*, const int32_t*, const int32_t*);


cdef extern void VDrv_FFT(void*, const int32_t*, const double*);


cdef extern void VInt_FFT(void*, const int32_t*);


cdef extern void WriteSpectrum_FFT(void*, const int32_t*, const int32_t*, const void*);



# Class FFT2


cdef extern void Fft2In_FFT2(void*, const int32_t*, const void*, const void*);


cdef extern void FilterPG_FFT2(void*, const int32_t*, const void*, const int32_t*, const double*, const double*, const double*);


cdef extern void Flt_FFT2(void*, const int32_t*, const void*, const void*);


cdef extern void FltInv_FFT2(void*, const int32_t*, const void*, const void*);


cdef extern void PowSpc_FFT2(void*, const int32_t*, const void*);


cdef extern void RadSpc_FFT2(void*, const int32_t*, const void*);


cdef extern void RadSpc1_FFT2(void*, const int32_t*, const int32_t*);


cdef extern void RadSpc2_FFT2(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TdXdY_FFT2(void*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void TransPG_FFT2(void*, const int32_t*, const int32_t*);



# Class FLT


cdef extern int32_t Create_FLT(void*, const void*);


cdef extern void Destroy_FLT(void*, const int32_t*);


cdef extern int32_t Load_FLT(void*, const void*);



# Class GD


cdef extern int32_t Create_GD(void*, const void*, const int32_t*);


cdef extern void Destroy_GD(void*, const int32_t*);



# Class GER


cdef extern int32_t Create_GER(void*, const void*);


cdef extern void Destroy_GER(void*, const int32_t*);


cdef extern int32_t IiGet_GER(void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern void SetInt_GER(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SetReal_GER(void*, const int32_t*, const void*, const double*);


cdef extern void SetString_GER(void*, const int32_t*, const void*, const void*);



# Class GMSYS


cdef extern void Launch_GMSYS(void*, const void*);



# Class GU


cdef extern void DipoleMag_GU(void*, const void*, const double*, const double*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void EMHalfSpaceInv_GU(void*, const double*, const double*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void EMHalfSpaceVV_GU(void*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Geometrics2DB_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void Geometrics2TBL_GU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GeometricsQC_GU(void*, const int32_t*, const void*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void Geonics3138Dump2DB_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void Geonics61Dump2DB_GU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void GeonicsDAT2DB_GU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void GrCurvCor_GU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GrCurvCorEx_GU(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void GrDEMVV_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GrTest_GU(void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GravityStillReadingCorrection_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iEMLayer_GU(void*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*, double*);


cdef extern int32_t iEMPlate_GU(void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IGenUXDetectSymbolsGroupName_GU(void*, const void*, const void*, void*, const int32_t*);


cdef extern void ImportDAARC500Ethernet_GU(void*, const void*, const void*, int32_t*);


cdef extern void ImportDAARC500Serial_GU(void*, const void*, const int32_t*, const void*, int32_t*);


cdef extern void ImportP190_GU(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void LagDAARC500GPS_GU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MaxwellPlateCorners_GU(void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void ScanDAARC500Ethernet_GU(void*, const void*, int32_t*, int32_t*);


cdef extern void ScanDAARC500Serial_GU(void*, const void*, const int32_t*, const int32_t*);


cdef extern void VVEuler_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void VVEuler2_GU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);



# Class GUI


cdef extern int32_t App_CreateWNDFromHWND_GUI(void*, int32_t);


cdef extern void App_Fft2SpecFilter_GUI(void*, const void*, const void*);


cdef extern int32_t App_GetParentWND_GUI(void*);


cdef extern void App_GetPrinterLST_GUI(void*, const int32_t*);


cdef extern int32_t App_iGetWindowState_GUI(void*);


cdef extern void App_SetWindowState_GUI(void*, const int32_t*);


cdef extern void App_GetWindowPosition_GUI(void*, int32_t*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_SetWindowPosition_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_GetClientWindowArea_GUI(void*, int32_t*, int32_t*, int32_t*, int32_t*);


cdef extern void App_GridStatHist_GUI(void*, const void*);


cdef extern void App_VoxelStatHist_GUI(void*, const void*);


cdef extern int32_t App_iColorForm_GUI(void*, int32_t*, const int32_t*);


cdef extern int32_t App_iColorTransform_GUI(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iCoordSysWizard_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern int32_t App_iCoordSysWizardLicensed_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern int32_t App_iCoordSysWizardGrid_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*);


cdef extern int32_t App_iDatabaseType_GUI(void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iDatamineType_GUI(void*, const void*, int32_t*);


cdef extern int32_t App_iExportXYZTemplateEditor_GUI(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t App_iExportXYZTemplateEditorEx_GUI(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iFileFilterIndex_GUI(void*, const void*);


cdef extern int32_t iGCSDatumWarningSHP_GUI(void*, const void*, const int32_t*);


cdef extern int32_t iGCSDatumWarningSHPDBEx_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iGCSDatumWarningSHPEx_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetAreaOfInterest_GUI(void*, double*, double*, double*, double*, const int32_t*, const int32_t*);


cdef extern int32_t App_iGetAreaOfInterest3D_GUI(void*, double*, double*, double*, double*, double*, double*, const int32_t*, const int32_t*);


cdef extern void IGetDATDefaults_GUI(void*, const int32_t*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern void IGetFileFilter_GUI(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, int32_t*);


cdef extern void IGetGSDirectory_GUI(void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_IiBrowseDir_GUI(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_IiColorTransformEx_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_IiCumulativePercent_GUI(void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t App_IiDatFileForm_GUI(void*, const void*, const void*, void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_IiGenFileForm_GUI(void*, const void*, const int32_t*, const int32_t*, const void*, void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_IiImportDrillDatabaseADO2_GUI(void*, const void*, void*, const int32_t*, void*, const int32_t*, int32_t*, const int32_t*);


cdef extern int32_t App_IiImportDrillDatabaseESRI_GUI(void*, const void*, void*, const int32_t*, void*, const int32_t*, int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t App_IiImportDrillDatabaseODBC_GUI(void*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, int32_t*, const int32_t*);


cdef extern int32_t App_IiImportDrillDatabaseODBCMaxwell_GUI(void*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, int32_t*, const int32_t*);


cdef extern int32_t App_iImportAsciiWizard_GUI(void*, const void*, const void*);


cdef extern int32_t App_iImportChemDatabase_GUI(void*, const void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iImportChemDatabaseADO_GUI(void*, const void*, const void*, void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iImportDatabase_GUI(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iImportDatabaseADO_GUI(void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iImportDatabaseSQL_GUI(void*, const void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iImportDatabaseSQLADO_GUI(void*, const void*, const void*, const void*, void*, const int32_t*);


cdef extern int32_t App_iImportDrillDatabaseADO_GUI(void*, const void*, const void*, void*, const int32_t*, int32_t*, const int32_t*);


cdef extern int32_t App_iImportTemplateSQL_GUI(void*, const void*, const void*, const void*, const void*);


cdef extern int32_t App_iImportTemplateSQLADO_GUI(void*, const void*, const void*, const void*, const void*);


cdef extern int32_t App_iImportXYZTemplateEditor_GUI(void*, const int32_t*, const void*, const int32_t*, const void*);


cdef extern int32_t App_IiODBCFileConnect_GUI(void*, const void*, void*, const int32_t*, const int32_t*, void*, const int32_t*);


cdef extern int32_t App_IiSymbolForm_GUI(void*, void*, const int32_t*, int32_t*, int32_t*, int32_t*, double*, double*, int32_t*, int32_t*);


cdef extern int32_t App_iMetaDataTool_GUI(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_ImportChemWizard_GUI(void*, const void*, const void*, const int32_t*);


cdef extern void App_ImportDrillWizard_GUI(void*, const void*, const void*, const void*, const int32_t*, int32_t*, const int32_t*);


cdef extern void App_InternetTrust_GUI(void*);


cdef extern int32_t App_iPatternForm_GUI(void*, int32_t*, double*, int32_t*, double*, int32_t*, int32_t*);


cdef extern int32_t App_iLinePatternForm_GUI(void*, int32_t*, double*, double*, int32_t*);


cdef extern int32_t App_iTwoPanelSelection_GUI(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t App_iTwoPanelSelection2_GUI(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t App_iTwoPanelSelectionEx_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t App_iTwoPanelSelectionEx2_GUI(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void App_LaunchSingleGeoDOTNETXTool_GUI(void*, const void*, const void*, const int32_t*);


cdef extern void App_LaunchGeoDOTNETXTool_GUI(void*, const void*, const void*, const int32_t*);


cdef extern void App_LaunchGeoXTool_GUI(void*, const void*, const void*, const int32_t*);


cdef extern void App_LaunchSingleGeoDOTNETXToolEx_GUI(void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_LaunchGeoDOTNETXToolEx_GUI(void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_LaunchGeoXToolEx_GUI(void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_MetaDataViewer_GUI(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_PrintFile_GUI(void*, const void*);


cdef extern void App_RenderPattern_GUI(void*, int32_t, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_RenderLinePattern_GUI(void*, int32_t, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void App_SetParentWND_GUI(void*, const int32_t*);


cdef extern void App_SetPrinter_GUI(void*, const void*);


cdef extern void App_SetProgAlwaysOn_GUI(void*, const int32_t*);


cdef extern void App_ShowDirectHist_GUI(void*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void App_ShowHist_GUI(void*, const int32_t*);


cdef extern void App_SimpleMapDialog_GUI(void*, const int32_t*, const void*, const void*);


cdef extern void App_ThematicVoxelInfo_GUI(void*, const int32_t*);


cdef extern void App_Show3DViewerDialog_GUI(void*, const void*, const void*, const void*);



# Class HTTP


cdef extern int32_t Create_HTTP(void*, const void*, const void*, const void*, const void*);


cdef extern void Destroy_HTTP(void*, const int32_t*);


cdef extern void Download_HTTP(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void SilentDownload_HTTP(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void Get_HTTP(void*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void Post_HTTP(void*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void SetProxyCredentials_HTTP(void*, const int32_t*, const void*, const void*);



# Class IEXP


cdef extern void AddGrid_IEXP(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t Create_IEXP(void*);


cdef extern void Destroy_IEXP(void*, const int32_t*);


cdef extern void DoFormula_IEXP(void*, const int32_t*, const void*, const int32_t*);



# Class INTERNET


cdef extern int32_t iDownloadHTTP_INTERNET(void*, const void*, const void*, const int32_t*);


cdef extern void SendMail_INTERNET(void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*);



# Class IP

# Plot Jobs




cdef extern void ConvertUBCIP2DToGrid_IP(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void CreateDefaultJob_IP(void*, const int32_t*, const void*, const int32_t*);


cdef extern void ExportUBCIP3_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const double*);


cdef extern void ExportUBCIPControl_IP(void*, const void*, const int32_t*, const int32_t*, const double*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*);


cdef extern void ExportUBCIPControlV5_IP(void*, const void*, const int32_t*, const double*, const void*, const void*, const int32_t*, const void*, const int32_t*, const void*, const int32_t*, const void*, const int32_t*, const void*, const int32_t*, const void*, const void*);


cdef extern void ExportUBCRes3_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const double*);


cdef extern void ExportUBCResControl_IP(void*, const void*, const int32_t*, const int32_t*, const double*, const void*, const void*, const void*, const void*, const double*, const void*, const void*);


cdef extern void ExportUBCResControlV5_IP(void*, const void*, const int32_t*, const double*, const void*, const void*, const int32_t*, const void*, const int32_t*, const void*, const int32_t*, const void*, const int32_t*, const void*, const void*);


cdef extern void ExportDataToUBC3D_IP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const void*, const void*);


cdef extern int32_t ImportUBC2DMOD_IP(void*, const void*, const int32_t*);


cdef extern void ImportUBC2DMSH_IP(void*, const void*, double*, double*, const int32_t*, const int32_t*);


cdef extern void ImportUBC2DTopo_IP(void*, const void*, double*, const int32_t*, const int32_t*);


cdef extern void OpenJob_IP(void*, const int32_t*, const void*, const int32_t*);


cdef extern void SaveJob_IP(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t TrimUBC2DModel_IP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, double*);


cdef extern void WriteDistantElectrodes_IP(void*, const int32_t*, const int32_t*);


cdef extern void WriteDistantElectrodesLST_IP(void*, const int32_t*, const int32_t*, const int32_t*);


# Miscellaneous




cdef extern void AverageDuplicatesQC_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern int32_t Create_IP(void*);


cdef extern void Destroy_IP(void*, const int32_t*);


cdef extern void ExportI2X_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*);


cdef extern void ExportIPDATA_IP(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ExportIPDATADir_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void ExportIPRED_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const void*, const double*, const double*, const int32_t*);


cdef extern void ExportIPREDDir_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*, const void*, const double*, const double*, const int32_t*, const void*);


cdef extern void ExportLineIPDATA_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void ExportSGDF_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void GetNValueLST_IP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetTopoLine_IP(void*, const int32_t*, const int32_t*, const void*, const double*, const double*, const double*, const int32_t*);


cdef extern int32_t iGetChanDomain_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void IGetChanLabel_IP(void*, const void*, void*, const int32_t*, void*, const int32_t*);


cdef extern void GetChannelInfo_IP(void*, const int32_t*, const int32_t*, const void*, int32_t*, double*, int32_t*, const int32_t*);


cdef extern void SetChannelInfo_IP(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*, const int32_t*, const int32_t*);


cdef extern void ImportDump_IP(void*, const int32_t*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportGrid_IP(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ImportI2X_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void ImportI2XEx_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void ImportInstrumentationGDD_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportIPDATA_IP(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ImportIPDATA2_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void ImportIPRED_IP(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ImportMergeIPRED_IP(void*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void ImportSGDF_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportTopoCSV_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportTopoGrid_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void ImportZongeAVG_IP(void*, const int32_t*, const int32_t*, const void*, const double*, const int32_t*, const double*);


cdef extern void ImportZongeFLD_IP(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const double*);


cdef extern void NewXYDatabase_IP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*);


cdef extern void PseudoPlot_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void PseudoPlot2_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*);


cdef extern void PseudoPlot2Dir_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const void*);


cdef extern void PSStack_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void PSStack2_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const void*);


cdef extern void PSStack2Dir_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const void*, const void*);


cdef extern void QCChanLST_IP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Recalculate_IP(void*, const int32_t*, const int32_t*);


cdef extern void RecalculateEx_IP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RecalculateZ_IP(void*, const int32_t*, const int32_t*);


cdef extern void SetImportMode_IP(void*, const int32_t*, const int32_t*);


cdef extern void Window_IP(void*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void WinnowChanList_IP(void*, const int32_t*);


cdef extern void WinnowChanList2_IP(void*, const int32_t*, const int32_t*);


cdef extern int32_t isValidLine_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t iLineArrayType_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern double rASpacing_IP(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t iPLDPConvention_IP(void*, const int32_t*);


cdef extern void GetElectrodeLocationsAndMaskValues_IP(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetElectrodeMaskValues_IP(void*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);




# Class IPGUI


cdef extern int32_t iModifyJob_IPGUI(void*, const int32_t*, const int32_t*, const void*, const int32_t*, int32_t*);


cdef extern void LaunchIPQCTool_IPGUI(void*, const void*, const void*, const void*);


cdef extern void LaunchOffsetIPQCTool_IPGUI(void*, const void*, const void*, const void*);


cdef extern int32_t iIPQCToolExists_IPGUI(void*);



# Class KGRD


cdef extern void _Clear_KGRD(void*, const int32_t*);


cdef extern int32_t Create_KGRD(void*);


cdef extern void Destroy_KGRD(void*, const int32_t*);


cdef extern int32_t iLoadParms_KGRD(void*, const int32_t*, const void*);


cdef extern int32_t iRun_KGRD(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iRun2_KGRD(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t iRun3_KGRD(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t iSaveParms_KGRD(void*, const int32_t*, const void*);



# Class LMSG


cdef extern void GotoPoint_LMSG(void*, const double*, const double*, const double*, const int32_t*);


cdef extern void ViewArea_LMSG(void*, const double*, const double*, const double*, const double*, const int32_t*);



# Class MISC


cdef extern void ConvertCG3toRAW_MISC(void*, const void*, const void*, const int32_t*);


cdef extern void ConvertCG5toRAW_MISC(void*, const void*, const void*, const int32_t*);


cdef extern void Ukoa2Tbl_MISC(void*, const void*, const void*, const void*);



# Class MSTK


cdef extern int32_t AddSTK_MSTK(void*, const int32_t*);


cdef extern void ChanListVV_MSTK(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t Create_MSTK(void*);


cdef extern void Destroy_MSTK(void*, const int32_t*);


cdef extern void DrawProfile_MSTK(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetYAxisDirection_MSTK(void*, const int32_t*, const int32_t*);


cdef extern void FindSTK2_MSTK(void*, const int32_t*, const void*, int32_t*, const int32_t*);


cdef extern int32_t GetSTK_MSTK(void*, const int32_t*, const int32_t*);


cdef extern void IDelete_MSTK(void*, const int32_t*, const int32_t*);


cdef extern void IFindSTK_MSTK(void*, const int32_t*, const void*, int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*);


cdef extern int32_t iGetNumSTK_MSTK(void*, const int32_t*);


cdef extern void ReadINI_MSTK(void*, const int32_t*, const int32_t*);


cdef extern void SaveProfile_MSTK(void*, const int32_t*, const int32_t*);



# Class MVG


cdef extern void AxisX_MVG(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void AxisY_MVG(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern int32_t Create_MVG(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void Destroy_MVG(void*, const int32_t*);


cdef extern int32_t GetMVIEW_MVG(void*, const int32_t*);


cdef extern void Grid_MVG(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void LabelX_MVG(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LabelY_MVG(void*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyLineVA_MVG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyLineVV_MVG(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RescaleXRange_MVG(void*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern void RescaleYRange_MVG(void*, const int32_t*, const int32_t*, const double*, const double*, const double*);



# Class PDF3D


cdef extern void Render_PDF3D(void*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void RenderToPage_PDF3D(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Export2D_PDF3D(void*, const void*, const void*, const int32_t*, const int32_t*, const int32_t*);



# Class PGEXP


cdef extern void AddPager_PGEXP(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t Create_PGEXP(void*);


cdef extern void Destroy_PGEXP(void*, const int32_t*);


cdef extern void DoFormula_PGEXP(void*, const int32_t*, const void*, const int32_t*);



# Class PGU

# General




cdef extern void Bool_PGU(void*, const int32_t*, const void*);


cdef extern void DirectGriddingDAT_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void DirectGriddingDAT3D_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void DirectGriddingDB_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DirectGriddingDB3D_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DirectGriddingVV_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Expand_PGU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Fill_PGU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void FillValue_PGU(void*, const int32_t*, const double*);


cdef extern void FiltSym_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const int32_t*);


cdef extern void FiltSym5_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*);


cdef extern void GridPeak_PGU(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDWGriddingDAT_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDWGriddingDAT3D_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDWGriddingDB_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDWGriddingDB3D_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void IDWGriddingVV_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void NumericToThematic_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Peakedness_PGU(void*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PeakednessGrid_PGU(void*, const void*, const void*, const int32_t*, const double*);


cdef extern void RefFile_PGU(void*, const int32_t*, const void*);


cdef extern void SaveFile_PGU(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const void*);


cdef extern void ThematicToNumeric_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Trend_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


# Math Operations




cdef extern void AddScalar_PGU(void*, const int32_t*, const double*);


cdef extern void MultiplyScalar_PGU(void*, const int32_t*, const double*);


# Matrix Operation




cdef extern void CorrelationMatrix_PGU(void*, const int32_t*, const int32_t*);


cdef extern void CorrelationMatrix2_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void InvertMatrix_PGU(void*, const int32_t*, const int32_t*);


cdef extern void Jacobi_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LUBackSub_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void LUDecomp_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MatrixMult_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MatrixVectorMult_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SVDecompose_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SVRecompose_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


# Principal Component Analysis




cdef extern void PCCommunality_PGU(void*, const int32_t*, const int32_t*);


cdef extern void PCLoadings_PGU(void*, const int32_t*, const int32_t*);


cdef extern void PCLoadings2_PGU(void*, const int32_t*, const int32_t*);


cdef extern void PCScores_PGU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PCStandardize_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PCStandardize2_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PCTransform_PGU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PCVarimax_PGU(void*, const int32_t*, const int32_t*);


# Specialized Operations




cdef extern double rMaximumTerrainSteepness_PGU(void*, const int32_t*, const int32_t*);




# Class PRAGA3


cdef extern int32_t iLaunch_PRAGA3(void*);



# Class PROJ

# Drag-and-drop methods




cdef extern void App_DropMapClipData_PROJ(void*, const int32_t*);


# Miscellaneous




cdef extern int32_t App_iAddDocument_PROJ(void*, const void*, const void*, const int32_t*);


cdef extern int32_t App_iAddDocumentWithoutOpening_PROJ(void*, const void*, const void*);


cdef extern int32_t App_iGetCommandEnvironment_PROJ(void*);


cdef extern int32_t App_iListDocuments_PROJ(void*, const int32_t*, const void*);


cdef extern int32_t App_iListTools_PROJ(void*, const int32_t*, const int32_t*);


cdef extern int32_t App_iRemoveDocument_PROJ(void*, const void*);


cdef extern int32_t App_iRemoveTool_PROJ(void*, const void*);


cdef extern int32_t App_iSaveCloseDocuments_PROJ(void*, const void*);


cdef extern void App_IGetName_PROJ(void*, void*, const int32_t*);




# Class RGRD


cdef extern void _Clear_RGRD(void*, const int32_t*);


cdef extern int32_t Create_RGRD(void*);


cdef extern int32_t CreateIMG_RGRD(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);


cdef extern void Destroy_RGRD(void*, const int32_t*);


cdef extern int32_t iDefault_RGRD(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iLoadParms_RGRD(void*, const int32_t*, const void*);


cdef extern int32_t iRun_RGRD(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iRun2_RGRD(void*, const int32_t*, const void*, const void*, const void*, const void*, const void*);


cdef extern int32_t iSaveParms_RGRD(void*, const int32_t*, const void*);


cdef extern void RunVV_RGRD(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*);



# Class SEMPLOT


cdef extern void ApplyFilterToMask_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void ConvertDummies_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern void CreateGroups_SEMPLOT(void*, const int32_t*, const void*);


cdef extern void DefaultGroups_SEMPLOT(void*, const int32_t*);


cdef extern void EditMapPlotParameters_SEMPLOT(void*, const int32_t*, const void*, const void*, const int32_t*, const void*);


cdef extern void EditPlotComponents_SEMPLOT(void*, const int32_t*, const void*);


cdef extern void EditPlotParameters_SEMPLOT(void*, const int32_t*, const void*);


cdef extern void ExportOverlay_SEMPLOT(void*, const void*, const void*, const int32_t*, const void*, const int32_t*, const void*, const void*, const void*, const void*, const void*, const void*, const int32_t*);


cdef extern void ExportView_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*);


cdef extern void ExportView2_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern void FilterLST_SEMPLOT(void*, const int32_t*);


cdef extern void FilterMineralPosData_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern void GetAssociatedLST_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetCurrentMineralLST_SEMPLOT(void*, const int32_t*, const void*, const int32_t*);


cdef extern void GetCurrentPositionLST_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern void GetFullMineralLST_SEMPLOT(void*, const int32_t*);


cdef extern void GetFullPositionLST_SEMPLOT(void*, const int32_t*);


cdef extern void GetGroupingLST_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern int32_t iCreateASCIITemplate_SEMPLOT(void*, const void*, const void*);


cdef extern int32_t iCreateDatabaseTemplate_SEMPLOT(void*, const void*, const void*);


cdef extern int32_t iEditFilter_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const void*);


cdef extern void IGetMineralChannelName_SEMPLOT(void*, const int32_t*, void*, const int32_t*);


cdef extern void IImportAsciiWizard_SEMPLOT(void*, const void*, const void*, void*, const int32_t*);


cdef extern void IImportDatabaseODBC_SEMPLOT(void*, void*, const int32_t*, void*, const int32_t*);


cdef extern void ImportBIN_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const int32_t*, const double*);


cdef extern void ImportDatabaseADO_SEMPLOT(void*, const void*, const void*);


cdef extern void InitGroupSymbolsUsed_SEMPLOT(void*, const int32_t*);


cdef extern int32_t iTemplateType_SEMPLOT(void*, const void*);


cdef extern int32_t iViewType_SEMPLOT(void*, const int32_t*, const void*);


cdef extern void MineralID_SEMPLOT(void*, const int32_t*, const double*, const int32_t*, const int32_t*);


cdef extern void NewFilter_SEMPLOT(void*, const void*, const void*);


cdef extern void NewTemplate_SEMPLOT(void*, const void*, const int32_t*, const void*);


cdef extern void OverlayLST_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Plot_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void PlotSymbolLegend_SEMPLOT(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void PropSymb_SEMPLOT(void*, const int32_t*, const int32_t*, const void*, const void*, const void*, const void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Replot_SEMPLOT(void*, const int32_t*, const void*, const void*, const int32_t*, const void*);


cdef extern void RePlotSymbolLegend_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern void ResetGroups_SEMPLOT(void*, const int32_t*, const void*);


cdef extern void ResetUsedChannel_SEMPLOT(void*, const int32_t*);


cdef extern void SelectPoly_SEMPLOT(void*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void SetChannelOrder_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern void SetChannelUnits_SEMPLOT(void*, const int32_t*);


cdef extern void SetITR_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetMask_SEMPLOT(void*, const int32_t*, const void*, const void*, const void*, const int32_t*, const int32_t*);


cdef extern void SortData_SEMPLOT(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TemplateLST_SEMPLOT(void*, const int32_t*, const int32_t*);


cdef extern void TileWindows_SEMPLOT(void*);


cdef extern void TotalOxides_SEMPLOT(void*, const int32_t*, const void*);



# Class SHP


cdef extern void AppendItem_SHP(void*, const int32_t*);


cdef extern int32_t Create_SHP(void*, const void*, const int32_t*);


cdef extern void Destroy_SHP(void*, const int32_t*);


cdef extern int32_t iAddIntField_SHP(void*, const int32_t*, const void*);


cdef extern int32_t iAddRealField_SHP(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iAddStringField_SHP(void*, const int32_t*, const void*, const int32_t*);


cdef extern int32_t iFindField_SHP(void*, const int32_t*, const void*);


cdef extern int32_t iMaxIDNum_SHP(void*, const int32_t*);


cdef extern int32_t iNumFields_SHP(void*, const int32_t*);


cdef extern int32_t iNumRecords_SHP(void*, const int32_t*);


cdef extern int32_t iType_SHP(void*, const int32_t*);


cdef extern int32_t Open_SHP(void*, const void*);


cdef extern void SetArc_SHP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetArcZ_SHP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetInt_SHP(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_SHP(void*, const int32_t*, const int32_t*);


cdef extern void SetPoint_SHP(void*, const int32_t*, const double*, const double*);


cdef extern void SetPointZ_SHP(void*, const int32_t*, const double*, const double*, const double*);


cdef extern void SetPolygon_SHP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetPolygonZ_SHP(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetReal_SHP(void*, const int32_t*, const int32_t*, const double*);


cdef extern void SetString_SHP(void*, const int32_t*, const int32_t*, const void*);


cdef extern void WriteItem_SHP(void*, const int32_t*);



# Class SQLSRV


cdef extern int32_t iAttachMDF_SQLSRV(void*, const void*, const void*, const void*, const void*, const void*, const void*);


cdef extern int32_t iDetachDB_SQLSRV(void*, const void*, const void*, const void*, const void*);


cdef extern int32_t iGetDatabaseLanguagesLST_SQLSRV(void*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern int32_t iGetDatabasesLST_SQLSRV(void*, const int32_t*, const void*, const void*, const void*, const int32_t*);


cdef extern void IGetLoginGUI_SQLSRV(void*, const void*, void*, const int32_t*, void*, const int32_t*, const int32_t*, int32_t*);


cdef extern int32_t iGetServersLST_SQLSRV(void*, const int32_t*);



# Class STK


cdef extern void GetTransParms_STK(void*, const int32_t*, int32_t*, double*, const int32_t*, const int32_t*, int32_t*, double*, const int32_t*, const int32_t*);


cdef extern int32_t iGetAxisFormat_STK(void*, const int32_t*, const int32_t*);


cdef extern void IGetAxisParms_STK(void*, const int32_t*, int32_t*, double*, double*, double*, void*, const int32_t*, double*, double*, double*, int32_t*, const int32_t*);


cdef extern void IGetFidParms_STK(void*, const int32_t*, double*, double*, double*, void*, const int32_t*, double*, void*, const int32_t*);


cdef extern int32_t iGetFlag_STK(void*, const int32_t*, const int32_t*);


cdef extern void IGetGenParms_STK(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, double*, double*, double*, double*, double*, double*, double*, double*);


cdef extern void IGetGridParms_STK(void*, const int32_t*, int32_t*, double*, double*, double*, double*, double*, double*, double*, double*, void*, const int32_t*, const int32_t*);


cdef extern void IGetLabelParms_STK(void*, const int32_t*, int32_t*, double*, int32_t*, double*, int32_t*, double*, void*, const int32_t*, double*, void*, const int32_t*, int32_t*, const int32_t*);


cdef extern void IGetProfile_STK(void*, const int32_t*, int32_t*, double*, double*, void*, const int32_t*, int32_t*, int32_t*, int32_t*, const int32_t*, void*, const int32_t*, int32_t*, void*, const int32_t*, double*, void*, const int32_t*, int32_t*);


cdef extern void IGetProfileEx_STK(void*, const int32_t*, int32_t*, double*, double*, void*, const int32_t*, int32_t*, int32_t*, int32_t*, int32_t*, const int32_t*, void*, const int32_t*, int32_t*, void*, const int32_t*, double*, void*, const int32_t*, int32_t*);


cdef extern void IGetSymbParms_STK(void*, const int32_t*, void*, const int32_t*, double*, void*, const int32_t*, void*, const int32_t*, int32_t*, int32_t*, double*, int32_t*, const int32_t*, const int32_t*, int32_t*, void*, const int32_t*, double*, void*, const int32_t*);


cdef extern void IGetTitleParms_STK(void*, const int32_t*, void*, const int32_t*, void*, const int32_t*, int32_t*, double*, double*, int32_t*, double*, double*, void*, const int32_t*, double*, void*, const int32_t*, const int32_t*);


cdef extern void ISetFlag_STK(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetArrayColors_STK(void*, const int32_t*, const int32_t*);


cdef extern void SetAxisFormat_STK(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SetAxisParms_STK(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const void*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void SetFidParms_STK(void*, const int32_t*, const double*, const double*, const double*, const void*, const double*, const void*);


cdef extern void SetGenParms_STK(void*, const int32_t*, const void*, const void*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);


cdef extern void SetGridParms_STK(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const void*, const int32_t*);


cdef extern void SetLabelParms_STK(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const double*, const int32_t*, const double*, const void*, const double*, const void*, const int32_t*, const int32_t*);


cdef extern void SetLineParm_STK(void*, const int32_t*, const int32_t*);


cdef extern void SetProfile_STK(void*, const int32_t*, const int32_t*, const double*, const double*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const void*, const double*, const void*, const int32_t*);


cdef extern void SetProfileEx_STK(void*, const int32_t*, const int32_t*, const double*, const double*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const int32_t*, const void*, const double*, const void*, const int32_t*);


cdef extern void SetSymbParms_STK(void*, const int32_t*, const void*, const double*, const void*, const void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const void*, const double*, const void*);


cdef extern void SetTitleParms_STK(void*, const int32_t*, const void*, const void*, const int32_t*, const double*, const double*, const int32_t*, const double*, const double*, const void*, const double*, const void*, const int32_t*);


cdef extern void SetTransParms_STK(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*);


cdef extern void SetVAIndexStart_STK(void*, const int32_t*, const int32_t*);



# Class STRINGS


cdef extern void LaunchDigitizationUI_STRINGS(void*, const void*, const void*);



# Class TC


cdef extern int32_t Create_TC(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const int32_t*);


cdef extern int32_t CreateEx_TC(void*, const int32_t*, const double*, const double*, const double*, const double*, const double*, const double*, const int32_t*, const double*, const int32_t*, const int32_t*);


cdef extern void Destroy_TC(void*, const int32_t*);


cdef extern void Grregter_TC(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Grterain_TC(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void Grterain2_TC(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void GGterain_TC(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);



# Class TEST


cdef extern void EnableDisableArcEngineLicense_TEST(void*, const int32_t*);


cdef extern int32_t iArcEngineLicense_TEST(void*);


cdef extern int32_t iTestMode_TEST(void*);


cdef extern void WrapperTest_TEST(void*, const void*, const void*);


cdef extern void CoreClass_TEST(void*, const void*, const void*);



# Class TIN


cdef extern void Copy_TIN(void*, const int32_t*, const int32_t*);


cdef extern int32_t Create_TIN(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t CreateS_TIN(void*, const int32_t*);


cdef extern void Destroy_TIN(void*, const int32_t*);


cdef extern void ExportXML_TIN(void*, const void*, int32_t*, const void*);


cdef extern void GetConvexHull_TIN(void*, const int32_t*, const int32_t*);


cdef extern void GetIPJ_TIN(void*, const int32_t*, const int32_t*);


cdef extern void GetJoins_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetMesh_TIN(void*, const int32_t*, const int32_t*);


cdef extern void GetNodes_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetTriangles_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void GetTriangle_TIN(void*, const int32_t*, const int32_t*, double*, double*, double*, double*, double*, double*);


cdef extern void GetVoronoiEdges_TIN(void*, const int32_t*, const int32_t*);


cdef extern int32_t iIsZValued_TIN(void*, const int32_t*);


cdef extern int32_t iLocateTriangle_TIN(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern int32_t iNodes_TIN(void*, const int32_t*);


cdef extern void InterpVV_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iTriangles_TIN(void*, const int32_t*);


cdef extern void LinearInterpVV_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void NearestVV_TIN(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RangeXY_TIN(void*, const int32_t*, double*, double*, double*, double*);


cdef extern void Serial_TIN(void*, const int32_t*, const int32_t*);


cdef extern void SetIPJ_TIN(void*, const int32_t*, const int32_t*);



# Class TRND


cdef extern void GetMaxMin_TRND(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void GetMesh_TRND(void*, const int32_t*, const void*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void TrndDB_TRND(void*, const int32_t*, const void*, const double*, const double*, const double*, const double*, const double*, const double*, const double*, const double*);



# Class UNC


cdef extern int32_t iIsValidUTF16Char_UNC(void*, const int32_t*);


cdef extern int32_t iValidSymbol_UNC(void*, const void*, const int32_t*, const int32_t*);


cdef extern void UTF16ValToSTR_UNC(void*, const int32_t*, void*, const int32_t*);


cdef extern void ValidateSymbols_UNC(void*, const int32_t*, const void*, const int32_t*);



# Class VAU


cdef extern void Prune_VAU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void TotalVector_VAU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);



# Class VVEXP


cdef extern void AddVV_VVEXP(void*, const int32_t*, const int32_t*, const void*);


cdef extern int32_t Create_VVEXP(void*);


cdef extern void Destroy_VVEXP(void*, const int32_t*);


cdef extern void DoFormula_VVEXP(void*, const int32_t*, const void*, const int32_t*);



# Class VVU


cdef extern void AverageRepeat_VVU(void*, const int32_t*, const int32_t*);


cdef extern void AverageRepeatEx_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AverageRepeat2_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void AverageRepeat2Ex_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void BinarySearch_VVU(void*, const int32_t*, const double*, int32_t*, int32_t*);


cdef extern void BoxCox_VVU(void*, const int32_t*, const double*);


cdef extern void BPFilt_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void Clip_VVU(void*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void ClipToDetectLimit_VVU(void*, const int32_t*, const double*, const int32_t*);


cdef extern void Decimate_VVU(void*, const int32_t*, const int32_t*);


cdef extern void Deviation_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void Distance_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void DistanceNonCumulative_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*);


cdef extern void Distance3D_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void FindGaps3D_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void DummyRange_VVU(void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void DummyRangeEx_VVU(void*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void DummyRepeat_VVU(void*, const int32_t*, const int32_t*);


cdef extern void DupStats_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void ExpDist_VVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void Filter_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FindStringItems_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void FractalFilter_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iCloseXY_VVU(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern int32_t iCloseXYM_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern int32_t iCloseXYZ_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern int32_t iCloseXYZM_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*);


cdef extern int32_t iDummyBackTracks_VVU(void*, const int32_t*);


cdef extern int32_t iFindDummy_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Interp_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iQCFillGaps_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern int32_t iSearchText_VVU(void*, const int32_t*, const void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Mask_VVU(void*, const int32_t*, const int32_t*);


cdef extern void MaskAND_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void MaskOR_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void NLFilt_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*);


cdef extern void NoiseCheck_VVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void NoiseCheck2_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void NormalDist_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);


cdef extern void OffsetCircles_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void OffsetCorrect_VVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void OffsetCorrect2_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void OffsetCorrect3_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void OffsetCorrectXYZ_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void OffsetRectangles_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void PickPeak_VVU(void*, const int32_t*, const int32_t*, const double*, const int32_t*);


cdef extern void PickPeak2_VVU(void*, const int32_t*, const int32_t*, const double*, const double*);


cdef extern void PickPeak3_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyFill_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolyFill2_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void PolygonMask_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Prune_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void QC_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const double*, const int32_t*);


cdef extern void RangeVectorMag_VVU(void*, const int32_t*, const int32_t*, double*, double*);


cdef extern void Regress_VVU(void*, const int32_t*, const int32_t*, double*, double*);


cdef extern void RelVarDup_VVU(void*, const int32_t*, const int32_t*, double*, int32_t*);


cdef extern void RemoveDummy_VVU(void*, const int32_t*);


cdef extern void RemoveDummy2_VVU(void*, const int32_t*, const int32_t*);


cdef extern void RemoveDummy3_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RemoveDummy4_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RemoveDup_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RemoveXYDup_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RemoveXYDupIndex_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void RollingStats_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void SearchReplace_VVU(void*, const int32_t*, const double*, const double*);


cdef extern void SearchReplaceText_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*);


cdef extern void SearchReplaceTextEx_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const void*, const void*, const int32_t*, int32_t*);


cdef extern void Spline_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const double*, const double*, const double*, const int32_t*, const int32_t*);


cdef extern void Spline2_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern int32_t iTokenizeToValues_VVU(void*, const int32_t*, const void*);


cdef extern void Translate_VVU(void*, const int32_t*, const double*, const double*);


cdef extern void Trend_VVU(void*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void Trend2_VVU(void*, const int32_t*, const int32_t*, const int32_t*, const int32_t*);


cdef extern void UniformDist_VVU(void*, const int32_t*, const int32_t*, const double*, const double*, const int32_t*);



cdef extern void* pCreate_GEO(const char*, const char*, int32_t, void*, int32_t, char*, int32_t);
cdef extern void Destroy_GEO(void *);

cdef unicode tounicode(char* s):
    return s.decode('UTF-8', 'strict')

cdef unicode tounicode_with_length(
        char* s, size_t length):
    return s[:length].decode('UTF-8', 'strict')

cdef unicode tounicode_with_length_and_free(
        char* s, size_t length):
    try:
        return s[:length].decode('UTF-8', 'strict')
    finally:
        free(s)

cdef class WrapPGeo:
    cdef void* p_geo
    
    def __cinit__(self, const char* app, const char* ver, wind_id=0):
        cdef void* hParentWnd = <void *>wind_id
        cdef char* err = <char*>malloc(4096)
        try:
            tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
            if not tls_geo is None:
                raise GXAPIError("Only one gxapi_cy.WrapPGeo instance per thread allowed.");
            self.p_geo = pCreate_GEO(app, ver, 0, hParentWnd, 0, err, 4096)
            if self.p_geo == NULL:
                raise GXAPIError(tounicode(err))
            thread_local.gxapi_cy_geo = <size_t>self.p_geo
        finally:
            free(err)
        
    def __dealloc__(self):
        if self.p_geo != NULL:
            Destroy_GEO(self.p_geo)
        thread_local.gxapi_cy_geo = None

    cdef _raise_on_gx_errors(self, void* p_geo):
        cdef int32_t term
        cdef char* module
        cdef char* err
        cdef int32_t error_number
        if iCheckTerminate_SYS(p_geo, &term) > 0:
            if term == 0:
                raise GXExit()
            elif term == -1:
                raise GXCancel()
            else:
                module = <char*>malloc(1024)
                err = <char*>malloc(4096)
                try:
                    sGetError_GEO(p_geo, module, 1024, err, 4096, &error_number)
                    if (error_number == 21023 or error_number == 21031 or # These two due to GXX asserts, Abort_SYS etc
                        error_number == 31009 or error_number == 31011):  # wrapper bind errors
                        raise GXAPIError(tounicode(err));
                    else:
                        raise GXError(tounicode(err), tounicode(module), error_number)
                finally:
                    if module != NULL:
                        free(module)
                    if err != NULL:
                        free(err)
    
    def dot_product(self, p1, p2, p3, p4, p5, p6):
        cdef double dp1 = p1, dp2 = p2, dp3 = p3, dp4 = p4, dp5 = p5, dp6 = p6
        retval = rDotProduct3D_MATH(self.p_geo, &dp1, &dp2, &dp3, &dp4, &dp5, &dp6)
        self._raise_on_gx_errors(self.p_geo)
        return retval

cdef void* get_p_geo():
    tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
    if not tls_geo is None:
        raise GXAPIError("A gxapi_cy.WrapPGeo instance has not been instantiated on current thread yet.");
    return <void*>tls_geo




cdef class Wrap3DN:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_3DN(get_p_geo(), &self.handle)





cdef class Wrap3DV:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destr_SYS(get_p_geo(), &self.handle)





cdef class WrapAGG:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_AGG(get_p_geo(), &self.handle)





cdef class WrapBF:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            DestroyEx_BF(get_p_geo(), &self.handle)





cdef class WrapDAT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DAT(get_p_geo(), &self.handle)





cdef class WrapDATALINKD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DATALINKD(get_p_geo(), &self.handle)





cdef class WrapDATAMINE:
    
    
    pass





cdef class WrapDB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DB(get_p_geo(), &self.handle)





cdef class WrapDBREAD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DBREAD(get_p_geo(), &self.handle)





cdef class WrapDBWRITE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DBWRITE(get_p_geo(), &self.handle)





cdef class WrapDSEL:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DSEL(get_p_geo(), &self.handle)





cdef class WrapEXT:
    
    
    pass





cdef class WrapGEO:
    
    
    pass





cdef class WrapGEOSOFT:
    
    
    pass





cdef class WrapGEOSTRING:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_GEOSTRING(get_p_geo(), &self.handle)





cdef class WrapGIS:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_GIS(get_p_geo(), &self.handle)





cdef class WrapHGD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_HGD(get_p_geo(), &self.handle)





cdef class WrapHXYZ:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_HXYZ(get_p_geo(), &self.handle)





cdef class WrapIGRF:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_IGRF(get_p_geo(), &self.handle)





cdef class WrapIMG:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_IMG(get_p_geo(), &self.handle)





cdef class WrapIMU:
    
    
    pass





cdef class WrapIPJ:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_IPJ(get_p_geo(), &self.handle)





cdef class WrapITR:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_ITR(get_p_geo(), &self.handle)





cdef class WrapLAYOUT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_LAYOUT(get_p_geo(), &self.handle)





cdef class WrapLL2:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_LL2(get_p_geo(), &self.handle)





cdef class WrapLPT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_LPT(get_p_geo(), &self.handle)





cdef class WrapLST:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_LST(get_p_geo(), &self.handle)





cdef class WrapLTB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_LTB(get_p_geo(), &self.handle)





cdef class WrapMAP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MAP(get_p_geo(), &self.handle)





cdef class WrapMAPL:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MAPL(get_p_geo(), &self.handle)





cdef class WrapMAPTEMPLATE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MAPTEMPLATE(get_p_geo(), &self.handle)





cdef class WrapMATH:
    
    
    pass





cdef class WrapMETA:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_META(get_p_geo(), &self.handle)





cdef class WrapMVIEW:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MVIEW(get_p_geo(), &self.handle)





cdef class WrapMVU:
    
    
    pass





cdef class WrapMXD:
    
    
    pass





cdef class WrapPAT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_PAT(get_p_geo(), &self.handle)





cdef class WrapPG:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_PG(get_p_geo(), &self.handle)





cdef class WrapPJ:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_PJ(get_p_geo(), &self.handle)





cdef class WrapPLY:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_PLY(get_p_geo(), &self.handle)





cdef class WrapRA:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_RA(get_p_geo(), &self.handle)





cdef class WrapREG:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_REG(get_p_geo(), &self.handle)





cdef class WrapSBF:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_SBF(get_p_geo(), &self.handle)





cdef class WrapST:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_ST(get_p_geo(), &self.handle)





cdef class WrapST2:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_ST2(get_p_geo(), &self.handle)





cdef class WrapSTR:
    
    
    pass





cdef class WrapSURFACE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_SURFACE(get_p_geo(), &self.handle)





cdef class WrapSURFACEITEM:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_SURFACEITEM(get_p_geo(), &self.handle)





cdef class WrapSYS:
    
    
    pass





cdef class WrapTB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_TB(get_p_geo(), &self.handle)





cdef class WrapTPAT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_TPAT(get_p_geo(), &self.handle)





cdef class WrapTR:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_TR(get_p_geo(), &self.handle)





cdef class WrapUSERMETA:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_USERMETA(get_p_geo(), &self.handle)





cdef class WrapVA:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VA(get_p_geo(), &self.handle)





cdef class WrapVM:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VM(get_p_geo(), &self.handle)





cdef class WrapVOX:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VOX(get_p_geo(), &self.handle)





cdef class WrapVOXD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VOXD(get_p_geo(), &self.handle)





cdef class WrapVOXE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VOXE(get_p_geo(), &self.handle)





cdef class WrapVULCAN:
    
    
    pass





cdef class WrapVV:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VV(get_p_geo(), &self.handle)





cdef class WrapWA:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_WA(get_p_geo(), &self.handle)





cdef class WrapACQUIRE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_ACQUIRE(get_p_geo(), &self.handle)





cdef class WrapARCDB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destr_SYS(get_p_geo(), &self.handle)





cdef class WrapARCDH:
    
    
    pass





cdef class WrapARCMAP:
    
    
    pass





cdef class WrapARCSYS:
    
    
    pass





cdef class WrapBIGRID:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_BIGRID(get_p_geo(), &self.handle)





cdef class WrapCHIMERA:
    
    
    pass





cdef class WrapCOM:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_COM(get_p_geo(), &self.handle)





cdef class WrapCSYMB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_CSYMB(get_p_geo(), &self.handle)





cdef class WrapDGW:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            App_Destroy_DGW(get_p_geo(), &self.handle)





cdef class WrapDH:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DH(get_p_geo(), &self.handle)





cdef class WrapDMPPLY:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DMPPLY(get_p_geo(), &self.handle)





cdef class WrapDOCU:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DOCU(get_p_geo(), &self.handle)





cdef class WrapDU:
    
    
    pass





cdef class WrapDXFI:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_DXFI(get_p_geo(), &self.handle)





cdef class WrapEDB:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            App_Destroy_EDB(get_p_geo(), &self.handle)





cdef class WrapEDOC:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            App_Destroy_EDOC(get_p_geo(), &self.handle)





cdef class WrapEMAP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            App_Destroy_EMAP(get_p_geo(), &self.handle)





cdef class WrapEMAPTEMPLATE:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            App_Destroy_EMAPTEMPLATE(get_p_geo(), &self.handle)





cdef class WrapEUL3:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destr_SYS(get_p_geo(), &self.handle)





cdef class WrapEXP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_EXP(get_p_geo(), &self.handle)





cdef class WrapFFT:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_FFT(get_p_geo(), &self.handle)





cdef class WrapFFT2:
    
    
    pass





cdef class WrapFLT:
    
    
    pass





cdef class WrapGD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_GD(get_p_geo(), &self.handle)





cdef class WrapGER:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_GER(get_p_geo(), &self.handle)





cdef class WrapGMSYS:
    
    
    pass





cdef class WrapGU:
    
    
    pass





cdef class WrapGUI:
    
    
    pass





cdef class WrapHTTP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_HTTP(get_p_geo(), &self.handle)





cdef class WrapIEXP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_IEXP(get_p_geo(), &self.handle)





cdef class WrapINTERNET:
    
    
    pass





cdef class WrapIP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_IP(get_p_geo(), &self.handle)





cdef class WrapIPGUI:
    
    
    pass





cdef class WrapKGRD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_KGRD(get_p_geo(), &self.handle)





cdef class WrapLMSG:
    
    
    pass





cdef class WrapMISC:
    
    
    pass





cdef class WrapMSTK:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MSTK(get_p_geo(), &self.handle)





cdef class WrapMVG:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_MVG(get_p_geo(), &self.handle)





cdef class WrapPDF3D:
    
    
    pass





cdef class WrapPGEXP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_PGEXP(get_p_geo(), &self.handle)





cdef class WrapPGU:
    
    
    pass





cdef class WrapPRAGA3:
    
    
    pass





cdef class WrapPROJ:
    
    
    pass





cdef class WrapRGRD:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_RGRD(get_p_geo(), &self.handle)





cdef class WrapSEMPLOT:
    
    
    pass





cdef class WrapSHP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_SHP(get_p_geo(), &self.handle)





cdef class WrapSQLSRV:
    
    
    pass





cdef class WrapSTK:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destr_SYS(get_p_geo(), &self.handle)





cdef class WrapSTRINGS:
    
    
    pass





cdef class WrapTC:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_TC(get_p_geo(), &self.handle)





cdef class WrapTEST:
    
    
    pass





cdef class WrapTIN:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_TIN(get_p_geo(), &self.handle)





cdef class WrapTRND:
    
    
    pass





cdef class WrapUNC:
    
    
    pass





cdef class WrapVAU:
    
    
    pass





cdef class WrapVVEXP:
    
    

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_VVEXP(get_p_geo(), &self.handle)





cdef class WrapVVU:
    
    
    pass




