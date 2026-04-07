# Monday Weekly Queries 
import os

def do_monday_weeklies(test, date, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory               = os.path.realpath(os.path.join('C:/Testing Bob/Monday Weekly', aid_year, month_folder))
        packaging_directory     = os.path.realpath(os.path.join('C:/Testing Bob/Packaging', aid_year, month_folder))
        disb_failure_directory  = os.path.realpath(os.path.join('C:/Testing Bob/Disb Failure ' + aid_year))
        save_directory          = os.path.realpath(os.path.join('C:/Testing Bob/SAVE', aid_year))
        daily_ea_directory      = os.path.realpath("O:/Testing Bob/External Awards/External Award Queries")
    else:
        directory               = os.path.realpath(os.path.join('O:/Systems/QUERIES/Monday Weekly', aid_year, month_folder))
        packaging_directory     = os.path.realpath(os.path.join('O:/Systems/QUERIES/Packaging', aid_year, month_folder))
        disb_failure_directory  = os.path.realpath(os.path.join('O:/Disbursement Failure/Disb Failure ' + aid_year))
        save_directory          = os.path.realpath(os.path.join('O:/Systems/QUERIES/SAVE', aid_year))
        daily_ea_directory      = os.path.realpath("O:/Systems/External Awards/External Award Queries")

    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(packaging_directory):
        os.makedirs(packaging_directory)
    if not os.path.isdir(disb_failure_directory):
        os.makedirs(disb_failure_directory)
    if not os.path.isdir(save_directory):
        os.makedirs(save_directory)

    move_directory = "Weekly Reports"
    move_pack_directory = "Packaging Reports"
    move_disb_directory = "Weekly Reports"
    move_save_directory = "Weekly Reports"
    
    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'
    
    if "UUFA_UOSFA_1690_LN_TYPES" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ACAD_LVLS_OUT_SYNC" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ADV_FSOI_INITIATED" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AGG_CK_MLT_YR_AWDED" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AID_DISB_NO_ENR_ATH" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AID_DISB_NO_ENR_FED" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AID_DISB_NO_ENR_SCH" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ALL_V4_V5_VER" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AMERICORP_AWD_POST" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ATHLETE_NOT_DISB" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ATH_HRS_AFTR_CENSUS" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ATH_SF_TERM_BALANCE" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AUDIT_CLSS_AID_DISB" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_ISA_PER_TERM" in query :
        return (query, renamed, directory, move_directory) 

    if "UUFA_WR_AWD_UG_NOW_GRAD_ATH" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AWD_UG_NOW_GRAD_FC" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_AWD_UG_NOW_GRAD_SV" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_CHKLST_STATUS_ERROR" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_CMT_CDE_O_AGR_LMT_2" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_DISB_ATH_FAILURE" in query :
        return (query, renamed, disb_failure_directory, move_disb_directory)

    if "UUFA_WR_DL_DISBURSED_LTHT" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_WR_DL_EC_SUSPENDED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_DL_ORIG_TRNS_PEND" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_EFT_CONSENT_VERIF" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FAFSA_CKLST_INCMP" in query :
        return (query, renamed, directory, move_directory)

    if  "_WR_FALL_TOTAL_WDRN_DRP" in query :
        return (query, renamed, directory, move_directory)

    if  "_WR_SPR_TOTAL_WDRN_DRP" in query :
        return (query, renamed, directory, move_directory)

    if  "WR_SNGDO_CAMPUS" in query :
        return (query, renamed, directory, move_directory)

    if  "_WR_SUM_TOTAL_WDRN_DRP" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FARC_CHECKLIST" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FARC_CMNT_CODES" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FED_AID_OVERAWARD" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FGED_ISIR_DEGREE" in query :
        return (query, renamed, directory, move_directory)

    if ("_WR_FPEL" in query) and ("_INITIATED_AWDED" in query):
        return (query, renamed, directory, move_directory)

    if "WR_FREV_GR_WS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_GENDER" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_HEDU_PARAMEDIC" in query :
        return (query, renamed, directory, move_directory)

    if "R_HOME_SCHOOLED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_HRS_DECREASE_ATH" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_HRS_DECREASE_FC" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_HRS_DECREASE_SV" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_FHST_I_HST_COMPLETE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_AS_EFC" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_COR_ASSESSMENT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_CORR_REJECT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_DGR_ANSW_CHNG" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_DEP_STAT_PRB" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_REJECTED_CORR" in query :
        return (query, renamed, directory, move_directory)

    if ("UUFA_WR_ISIR_REJECT_CODES" in query ) \
            | (("UUFA_WR_ISIR_REJECT_CODES_20") in query ) :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_SS_MCH_NOT_CON" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_ISIR_SUSPENSE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LEGAL_ALIEN_WORK" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LN_ACCPT_STAF_31_32" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LOAN_CENSUS_DATE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LN_FA907_1_REVISED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LN_FA907_2_REVISED" in query :
        return (query, renamed, directory, move_directory)

    if "R_LOAN_ORIG_DEPT_REVIEW" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LN_SENT_NO_RESPONSE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LOAN_TRANSMIT_HOLD" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LW_MD_DN_AW_NO_DISB" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_MNTGMR_AMCORP_OVRAW" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_MULTIPLE_EMPLIDS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_NO_COMMENT_CODE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_NSLDS_LOAN_DATA" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_OVRD_ACAD_LVL" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PA_EXPECT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PA_FDEG_CHECKLIST" in query:
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_AWRD_LOCK" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_OVERPAYMENT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_SUMMER_NO_PELL" in query :
        return (query, renamed, directory, move_directory)

    if "WR_PELL_SUMMER_AGGS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_TERM_FT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_TERM_HT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_TERM_LH" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_TERM_NL" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PELL_TERM_TQ" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PERK_SPLIT_MISMATCH" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_PRK_LN_ACAD_LVL_CHG" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_QUALITY_ASSURANCE" in query :
        return (query, renamed, directory, move_directory)

    if "R_RT4_DROPPED_CLASSES" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SCH_NOT_DISB" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SCHOLAR_TBP_NO_AWRD" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_GRAD_FELLOW" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SSR_MATCH_NOT_CNFRM" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SSR_NOT_CNFRMD_VTRN" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SS_DB_OVERRIDE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUB_ISIR_PACKAGED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUB_ISIR_REAWD_AID" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUB_ISIR_SYSG" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUB_ISIR_VERIFIED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUMMER_NO_DL" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SUMMER_PELL_LTHT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SSP_DOB_PRB_APPLCNT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SSP_NAME_PRB_APLCNT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_SSP_SSN_PRB_APLCNT" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_TERM_NSLDS_LOAN_YR" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_TITLE_VII_MED_LOANS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_TRANSFER_ENT_CNS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_TRANSFER_STU_FA_SP" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_UG_GR_DIR_LN_GR_TRM" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_UG_GR_PLUS_GR_TERM" in query :
        return (query, renamed, directory, move_directory)

    if "WR_UAC_FASI_STATUS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_UAC_SNGDO" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_UNDOCUMENTED_STUDENTS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_VERI_CHKLST_MISSING" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_VERI_INCOME_ADJ" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_VER_NOT_CONSL" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_VETERAN_ACTIVE_DUTY" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_VETERAN_NO_QUALIFY" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_WEEKS_OF_INSTR_FIX" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_DL_AY_SP_CANCELED" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LOAN_TRANSMIT_HOLD_13" in query:
        return (query, renamed, directory, move_directory)

    if "_WR_REJECT_CODE_ON_ISIR" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_RT4_FA_DROP_CLASSES" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_RT4_SP_DROP_CLASSES" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_RT4_SU_DROP_CLASSES" in query :
        return (query, renamed, directory, move_directory)

    if "WR_AWARDS_OTHER_INST" in query :
        return (query, renamed, directory, move_directory)

    if "WR_DEP_PRNT_SSN_RVW" in query :
        return (query, renamed, directory, move_directory)

    if "WR_DN_LW_MD_AID_ATRB" in query :
        return (query, renamed, directory, move_directory)

    if "WR_FSEOG_NO_PELL" in query :
        return (query, renamed, directory, move_directory)

    if "WR_FT_CLASS_OVERRIDES" in query :
        return (query, renamed, directory, move_directory)

    if "WR_GR_ACAD_LV_OUT_SYNC" in query :
        return (query, renamed, directory, move_directory)

    if "WR_PELL_COA_DOUBLE" in query :
        return (query, renamed, directory, move_directory)

    if "WR_PKG_AWD_NO_BDGT" in query :
        return (query, renamed, directory, move_directory)

    if "WR_SCH_TUITION_FEES" in query :
        return (query, renamed, directory, move_directory)

    if "WR_SCHOL_GRAD_DATE" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_STDNT_NOT_PACKAGED" in query :
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_DSB_PLN_SPLT_CD_FD" in query :
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_PELL_ELG_NO_PELL" in query :
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_CTZN_IND_AWD_NO_LN" in query :
        return (query, renamed, directory, move_directory)

    if "WR_SAVE_CTZNSHIP_VER" in query :
        return (query, renamed, save_directory, move_save_directory)

    if "WR_ALL_C_FVRA_I_NO_COR" in query :
        return (query, renamed, save_directory, move_save_directory)

    if "WR_CORRECTION_NOT_SENT" in query :
        return (query, renamed, save_directory, move_save_directory)
    
    if "UUFA_WR_WITH_COMMENT_CODE" in query :
        return (query, renamed, save_directory, move_save_directory)
    
    if "UUFA_WR_BLANK_LOAN_TYPE" in query :
        return (query, renamed, save_directory, move_save_directory)
    
    if "UUFA_WR_TSM_ALERTS" in query :
        return (query, renamed, directory, move_directory)

    if "_WR_LOAN_EFT_DETAIL_ERROR" in query:
        return (query, renamed, directory, move_directory)

    if "_WR_NSL_PROMISSORY_NOTE" in query :
        return (query, renamed, directory, move_directory)

    if "UUFA_AP_RPKG_FPEL_AWARD_LCK" in query:
        return (query, renamed, directory, move_directory)

    if "_WR_FAVR_I_NO_FCOR_ALL_C" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_SCHADM_DUALCAR" in query :
        return (query, renamed, daily_ea_directory, move_directory)
    
    if "UUFA_WR_DEFERMENT_REPORT" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_BDGT_LN_FEE_MNL" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_RESIDENCY_RECLASS" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_SCH_PLACEHOLDER" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_BDGT_LN_FEE_MNL" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_OUTSIDE_RESOURCES" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_RESIDENCY_RECLASS" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_CTZN_IND_AWD_NO_LN" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_OUTSIDE_RESOURCES" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_PRO_STDNT_NOT_PACK" in query:
        return (query, renamed, directory, move_directory)
    
    if "UUFA_WR_PHARM_ENRL_W_LOAN" in query:
        return (query, renamed, directory, move_directory)
    
    # Packaging queries that are being manually run.
    if "PRT_ATH_ACCEPT_FED_AID" in query :
        return (query, renamed, packaging_directory, move_pack_directory)

    if "PRT_ATH_AWD_CBA_GRANT" in query :
        return (query, renamed, packaging_directory, move_pack_directory)

    if "PRT_ATHLETE_GRAD_DATE" in query :
        return (query, renamed, packaging_directory, move_pack_directory)

    if "PRT_ATH_OFFERED_FED_AID" in query :
        return (query, renamed, packaging_directory, move_pack_directory)

    return "Empty" #Leave as last line
