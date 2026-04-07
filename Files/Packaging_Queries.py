# Packaging Queries
import os

def do_packaging_queries(test, date, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Packaging', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Packaging', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Packaging Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'
                
    if query.startswith("UUFA_PRT_ACAD_LVLS_OUT_SYNC"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ACAD_PROG_REVIEW")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ATH_ACCEPT_FED_AID"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ATH_AWD_CBA_GRANT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ATH_GRAD_DATE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ATH_OFFRD_FED_AID"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ATH_OFFR_ACCPT_AID")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWARD_TERM_HAD_SAP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWARDS_OTHER_INST"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWD_CMB_OVR_AG_RVW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_PRT_AWD_MASS_P_NO_AWARDS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWD_SUB_OVR_AG_RVW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_CTZN_IND_AWD_NO_LN"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DEFR_ENROLLMENT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DEP_PRNT_SSN_RVW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DIAG_AWD_PELL_TERM")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_PRT_DISB_PLAN_SPLT_CODE")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DL_DPAY_SCSP")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_FD")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_SC")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_EXPECT_GRAD_TERM_11"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_DL_GRAD_TERM_FALL")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_GRAD_TRM_FALL")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_GRAD_TRM_SPRING")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_HEAL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_LEU_C_PELL_FSEOG")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_LEU_C_PELL_AWARD")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_LEU_E_PELL_FSEOG")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_LN_CBA_AWD_NO_ELIG"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_NSL_LOAN_RPT_VERI")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_NURSING_LOAN_RPT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_ON_LINE_PACKAGING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PELL_COMMENT_037")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PLL_EL_CTZN_NOT_INDCT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PELL_UG_5TH_YR_2ND_BA"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PHARM_NO_HEAL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PKG_AWD_NO_BDGT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PKG_SCH_AWD_NO_BGT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PRIOR_TERM_STFFRD_OFR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_SCHOL_GRAD_DATE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_SUB_UNSUB_SP_SP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_SET_HEAL_FLAG")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_STATE_OF_RES_FM_MH_PW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_PRT_STILL_UNPRCD_AFTER_PKG"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_STDNT_NOT_PACKAGED")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_TEACH_CREDENTIAL")  :
        return (query, renamed, directory, move_directory)

    if ("PRT_SUB_UNSUB_FA_FA") in query  :
        return (query, renamed, directory, move_directory)

    if ("PRT_PELL_PKG_LOAD_CHCK") in query  :
        return (query, renamed, directory, move_directory)

    if ("PRT_COUNT_ITEM_TYPE") in query  :
        return (query, renamed, directory, move_directory)

    if ("PKG_NOT_PKGD_NO_UNITS") in query  :
        return (query, renamed, directory, move_directory)
                    
    if query.startswith("UUFA_READY_PACKAGE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_NO_FALL"):
        return (query, renamed, directory, move_directory)

    if ("UUFA_PRT_PELL_FPEL" in query) and ("_INITIATED" in query):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_READY_PKG"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_RPKG_LVL"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_PLACE_FA9"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_PELL_LEU_450"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_BATCH_PKG_DETAIL"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_PKG_SELECT_1ST_RUN"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_PKG_SELECT_SMR"):
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line
