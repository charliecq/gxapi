"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" cysetup.py build_ext --inplace
xcopy /Y /D gxapi_cy.cp36-win_amd64.pyd ..\gxpy\
xcopy /Y /D gxapi_cy_extend.cp36-win_amd64.pyd ..\gxpy\
xcopy /Y /D gxapi_cy.cp36-win_amd64.pyd ..\gxpy\geosoft\gxapi\gxapi_cy.pyd
xcopy /Y /D gxapi_cy_extend.cp36-win_amd64.pyd ..\gxpy\geosoft\gxapi\gxapi_cy_extend.pyd

"C:\git\python35\python.exe" cysetup.py build_ext --inplace

xcopy /Y /D gxapi_cy.cp35-win_amd64.pyd ..\gxpy\
xcopy /Y /D gxapi_cy_extend.cp35-win_amd64.pyd ..\gxpy\


