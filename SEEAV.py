import wmi
import random
import json

phrases = ["[i] Rushing B...",
    "[i] Squeezing lemons...",
    "[i] Hatching chickens...",
    "[i] Going sneaky-beaky-like...",
    "[i] Inspecting weapons...",
    "[i] Holding an angle...",
    "[i] Taking a windy stroll...",
    "[i] Adjusting crosshair settings...",
    "[i] Setting up the server...",
    "[i] Calibrating the sound...",
    "[i] Filling grenades...",
    "[i] Defusing a ticking time bomb...",
    "[i] You'll die if you don't...",
    "[i] Doing some light reading...",
    "[i] Warming up the servers...",
    "[i] Hoping no one is cheating...",
    "[i] Trying to join the game..."
]
phrases1 = random.choice(phrases)

print(f"""


   ▄▄▄▄▄   ▄███▄   ▄███▄       ██       ▄   
  █     ▀▄ █▀   ▀  █▀   ▀      █ █       █  
▄  ▀▀▀▀▄   ██▄▄    ██▄▄        █▄▄█ █     █ 
 ▀▄▄▄▄▀    █▄   ▄▀ █▄   ▄▀     █  █  █    █ 
           ▀███▀   ▀███▀          █   █  █  
                                 █     █▐   
                                ▀      ▐    


                [By: dv00x1]
                

[i] Scanning for processes...
{phrases1}
""")




if __name__ == "__main__":
    _c_ = wmi.WMI()
    
    _l_ = {
        "AcisEagEnt.exe": "cisCo uMbrellA roaMing securitY - secuRiTy dnS",
        "aCnAMLoGonagenT.exe": "absolutE perSisteNce - AssEt mAnAgement",
        "aCnamagenT.exe": "abSoluTe peRsisTencE - aSsEt manAgement",
        "acuMbrelLAAgENT.exe": "CiScO UmbRELLA roaminG seCurITy - secURitY dNs",
        "AgmservIce.EXe": "adoBe - teleMetry",
        "agsSerViCe.exE": "AdObE - TeLeMEtRY",
        "appCOnTRolagEnt.exe": "applicaTion cOnTroL - TreNd miCro",
        "ASWIDSAgENt.EXE": "aV - AVasT",
        "aVASTSvc.exe": "Av - aVAST",
        "aVasTUieXe": "av - avasT",
        "avgnT.EXE": "av - avIRa",
        "aVGUard.exE": "aV - aVira",
        "aVp.exe": "aV - KasPersKY",
        "AVpui.EXe": "aV - KASPERSkY",
        "axCRYpt.exe": "aXCrYpT - encrYPtIon",
        "bdagEnt.exe": "aV - bitDeFenDer toTal sEcURitY",
        "BDNTwrK.exe": "aV - biTdefEnDEr",
        "BRowsEReXPLOItDetectIOn.EXE": "ExpLOiT DEtecTIOn - TrenD MicrO",
        "carbOnSENsor.exe": "eDr - vMwaRe cArbon BlaCk eDr",
        "cbCoMms.exe": "cRoWDstrIKe fAlCon inSighT xDr - Xdr",
        "ccsVCHsT.EXE": "av - norTon AnTIvIruS",
        "ccsvCHST.exe": "Av - sYManteC endPoInt PrOTecTion",
        "cLieNTcommUNIcatiONservICE.exe": "aNtiViRus/EDR - TREND miCrO",
        "CliEntLOgSerViCe.Exe": "antIVirUs/edR - TREnD miCrO",
        "cLienTSoluTIoNframewoRK.exE": "AntIVIrUs/eDR - TREnD MiCro",
        "cmRcsErViCe.exe": "MicROSOft ConFIgURatiOn MaNager ReMOtE COntrOL SerVIce - ReMOtE cOnTroL",
        "conCeNTr.exe": "paLo al To nEtwoRks gLoBAlPROtecT - vPn",
        "coreSerViCeSheLL.exe": "aV - TREnD micrO",
        "CPd.EXE": "cheCk POinT daEmOn - SecURitY",
        "cPx.exe": "SenTinELonE sinGUlaRitY xDR - xDr",
        "CSfALconconTAinEr.ExE": "CRoWdstrIKe fALCon - edr",
        "CSFalConDATErePAir.eXe": "CRoWdsTRike falCoN - eDr",
        "csFALcOnServiCE.exe": "croWDSTRikE FAlCOn InsIGHt xDr - xdr",
        "cYbereaSoN.exE": "cYBerEASOn eDR - Edr",
        "cYTOmicEnDPoINT.exE": "cytOmIC oRiOn - SECuriTY",
        "cyVERacONsOLe.eXE": "edR - paLo aLTO neTworks (CYveRa)",
        "cyVErASERvicE.EXe": "eDR - PalO AltO neTwORks (corTex xdr)",
        "CyVrAGentSVC.EXe": "eDr - PaLO aLTO netwOrkS (cOrtex xdR)",
        "cyvrFsFlT.EXE": "Edr - palO aLTO neTwORKs (COrtEX xdR)",
        "darKTRAceTsA.exe": "DarKTraCE - EdR",
        "dATAPRoTeCtiOnsERVIcE.exe": "datA proTeCtion - trenD miCro",
        "dlPAgEnt.exe": "DlP - sYmAnteC dlp agEnT",
        "dLpSenSOR.exe": "Dlp - mcAFeE dlP sensOr",
        "dSmONiToR.Exe": "DriVESENtrY - SECurity",
        "dweNginE.EXE": "DriVeSenTry - SecURitY",
        "eDpa.EXE": "aV - mcafEE endPoInT SeCuRItY",
        "EegosERViCe.EXe": "enCRYptiOn - mcAfEE eNdpoInT EnCRyptIon",
        "eGui.exe": "Av - EsEt Nod32 aV",
        "ekRn.ExE": "av - esEt Nod32 Av",
        "EnDPoINtBaseCAmP.exe": "EdR - tREnD miCrO",
        "firEsvc.exe": "firEEyE endPOinT AgENt - SeCurItY",
        "firETRaY.exe": "FirEeyE enDPOInt AGent - SECUriTY",
        "foRTieDr.exe": "edR - forTIeDR",
        "fw.exe": "cHecK PoiNt FiREWall - fiRewAll",
        "HEALTHSerVICe.EXE": "MiCroSofT omS - MoniToring",
        "HiPs.exE": "hiPs - hoSt iNtrUsIon PreVenTion sYstem",
        "kLwTbLFs.exe": "AV - KasPeRSkY",
        "klWtpwrs.srv": "Av - KaspERSKY",
        "kpf4ss.exe": "fiREwaLL - kERIo pErSOnal FirEWAll",
        "KSDEx.eXE": "kaSpERskY sEcUre conNectIOn - vpN",
        "kSdeUi.EXe": "kAsPeRsKY seCurE conNEctIOn - VpN",
        "MaCmnSvc.exe": "aV - mcaFEe EnDPoINt SeCuRitY",
        "masVC.EXe": "AV - mCafee ENdPoINt SeCUriTY",
        "mBAE64.syS": "av - mAlwarEbyTeS",
        "mbamaGEnT.ExE": "mALwaRebyTeS aGEnt - aNtiviRus",
        "mBAmseRVicE.exe": "aV - MaLwarebYtEs",
        "mbAMsWISsARmY.sYS": "av - malWareBytES",
        "mbamTraY.EXe": "AV - MALwarebyTes",
        "mcshIElD.EXe": "av - mcAfEE ViRUsSCan",
        "mdecrYptSErvICE.exe": "enCrYpTiOn - mcAFee endPoiNT eNcrYptIOn",
        "mDNSrEsPondeR.Exe": "bONjoUR serViCe - NeTwoRk SerVIce",
        "mfeAnn.EXE": "Av - mCAFee",
        "mFeepeHosT.EXe": "enCryPtioN - mcAfEe ENdPoiNt ENCrYPTioN",
        "mfEFiRe.exe": "hiPS - mcafeE hoST inTruSIOn pRevenTIon",
        "mFemACtl.exe": "FiReWAll - mcAFee ENDPoiNt sEcuriTY FiREwaLL",
        "mFemMS.EXe": "aV - mcaFee",
        "MonitoRInGhOST.exe": "MicRosOFt MOnItoRINg AGenT - monItOrinG",
        "mpDeFeNDerCOreSERvicE.exe": "wINdows defEnDer CoRE SeRvicE - aNtIViruS",
        "mSAsCuIl.exe": "aV - winDowS DefeNDER",
        "msmpeng.exe": "av - WinDoWs DeFendeR",
        "MSSECes.EXe": "aV - MiCrosOFt sEcuRitY eSseNtiAls",
        "MssEnse.EXE": "MicRoSoFt DeFenDer AtP - secURitY",
        "nissrV.exe": "Av neTWORK INSpecTiOn - miCrOSOft SeCuritY eSseNTials",
        "NoRtOnSECurItY.EXe": "aV - nOrTon aNTiViruS",
        "npMDaGeNT.ExE": "neTwoRk MonITorINg - soLARWInDS nPm",
        "NS.exE": "av - norTon antIVIruS",
        "nssERVIcE.exE": "av - nOrtOn anTIViruS",
        "opENvPnSErv.exe": "oPenVPn - Vpn",
        "outPOsT.exe": "agNitUm ouTPoST fIrEwalL - FirEwAll",
        "PAnDA_urL_FilTErinG.Exe": "Av - PanDa secuRiTy",
        "PaNgpS.ExE": "paLo AlTO NeTwoRks glOBaLprOtect - vPn",
        "PavFnsVR.EXE": "aV - PanDa SecURiTy",
        "paVSrV.Exe": "Av - PanDa sEcUriTy",
        "perSonaLfireWAlLseRvICE.exe": "fiREwalL - treNd MiCrO",
        "pSanhOsT.exE": "aV - PanDa secURity",
        "ReAlTImescANSERvICE.EXe": "anTivIRus/eDR - TREnd MICRo",
        "rTvsCan.Exe": "aV - SymANTec enDpoinT pROTeCtiOn",
        "SamPLinGservICE.exe": "aNTIViruS/EdR - tRend MicRo",
        "SaVsERvice.exe": "aV - soPhOs EndPOinT SEcURitY",
        "sBieSvc.EXe": "saNdbOxie - sEcuritY",
        "SecuRITYAGEntMONitOR.EXE": "anTIvIRus/eDR - TREnD mICro",
        "SECURITyheaLThSeRvIce.exe": "wiNDOWs sEcuRiTy HeaLth ServICE - SecUriTY",
        "SECuriTYHeALThSYstRAy.ExE": "winDowS SecUritY systrAY - secURitY",
        "SensEIReX.eXE": "WINDows DeFENdEr IR - SEcuRiTY",
        "SENsENdr.exe": "winDowS DEfendEr nDR - sEcUriTY",
        "senSetVm.EXe": "wInDoWS DeFenDeR tVm - SECURiTy",
        "SenTINeL.ExE": "EDr - UnKnOWN (PotEnTiAl: MiCrOsoft dEFendEr)",
        "SenTInELAgenT.EXe": "Edr - senTineLoNe",
        "SenTineLcTL.ExE": "edR - SENtineloNE",
        "senTinElmEMOrysCaNnEr.exE": "sEntinEloNE - EDR",
        "SenTineLSeRvicehoSt.exe": "SenTINeLOnE - eDR",
        "SenTineLsTAticenGinE.ExE": "SENTinELOne - eDr",
        "sENTinELstAticengINeSCaNneR.exe": "sEnTinElOne - edR",
        "sGRMBroKeR.exe": "wIndoWS sYstEm InTegrItY mANagemENT brOKer - sYstem iNTegRITy",
        "shStAT.exE": "AV - mCafEE virUSSCan",
        "sMsVchOST.EXe": "ApPLicATion - micrOSOfT .neT FrAmewORK",
        "sOPhoSAv.exe": "Av - SopHoS EndPOinT SecURitY",
        "SopHOSCLEAN.exe": "aV - SOPhoS",
        "SoPhoShEalTH.EXE": "aV - sOPHos",
        "soPHOSsps.exe": "aV - SopHOs EnDpOint sEcuRITY",
        "SoPhoSUieXe": "av - sopHOs eNDPoiNt SeCurITY",
        "SYSmON.Exe": "MiCroSofT SYSMON - SecuriTY",
        "sYsmon64.exe": "MICRoSoFt sYsmon - secuRiTy",
        "TaNcLient.exE": "EDR - TaNiUM edR",
        "teleMEtRYagENTseRviCe.EXe": "TelEMetrY - trENd MICro",
        "TeleMetRySErvice.EXE": "TelEmEtrY - uNkNown",
        "tmntSRv.exe": "aV - TREnd miCro oFficEScan",
        "TmpROxY.Exe": "aV - tReND miCRo OFficescan",
        "TRAps.EXe": "EdR - paLo AlTo NeTwORks (CortEX xdr)",
        "TRaPSAGenT.exe": "PAlO aLTO neTWORKs cOrtex xDR - xDr",
        "TrApSD.exE": "pAlO aLTO NetwoRkS CORteX xdR - Xdr",
        "tRuecRYpT.exe": "EnCrYPtion - TRueCRyPT",
        "uiWiNmGR.exe": "aV - TrEND mICRo",
        "UPdaTESrv.exe": "AV - bITdeFendeR",
        "VGauThSerVICe.EXE": "vmWARe - vIRtuALizAtIoN",
        "VM3dsERVicE.exE": "VMwaRe - ViRTuALIZatioN",
        "vmTooLsD.exe": "vmwArE - VirTuaLiZatIon",
        "vPnAGeNT.Exe": "cIsco anYCOnnECt seCUre MoBIlitY clIENt - vpn",
        "VPNuI.EXe": "ciSCO AnYcOnnEcT - vpn",
        "VSSErV.EXE": "AV - bITDefENder toTAL SEcURitY",
        "VulNERaBiliTYpRoTecTIonagenT.EXE": "TrenD MiCro - vuLneRABIlitY PrOTecTIon",
        "WinDEFEnD.ExE": "av - winDowS DefenDer",
        "WinLOgBeAT.exe": "ElaSTic WinlOgbeaT - secURitY",
        "WiREGuarD.EXe": "VpN - wiReGuARD",
        "WRsa.EXE": "av - WeBrOOT ANywHEre",
        "WsCSERviCE.Exe": "SEcurItY SerVicE - tREnd mICro",
        "xAgT.Exe": "firEye Hx - SeCUriTY"
    }

    _m_ = {k.lower(): v for k, v in _l_.items()}
    
    try:
        for _s_ in _c_.query('select * from win32_process'):
            _k_ = _s_.Caption
            if _k_.lower() in _m_:
                print(f"[+]Process found: {_k_} - {_m_[_k_.lower()]}.")
    except Exception as e:
        print(f"erro: {e}")
        
    print("\nin this digital abyss, the greatest sin is to believe you are unmonitored.")
