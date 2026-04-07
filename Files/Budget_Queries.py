# Budget Queries 
import os

def do_budget_queries(test, date, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]
    
    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Budgets', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Budget Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'
    
    if query.startswith("UUFA_BR_ACAD_LVLS_OUT_SYNC")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_ATH_TUIT_INCR_NR")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_ATH_TUITION_INCRS")  :
        return (query, renamed, directory, move_directory)

    if "_BR_BDGT_DOUBLE_BUDGETS" in query :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_COA_LESS_HT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_COA_TUIT_ZERO")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_DN_LW_MD_AID_ATRB")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_FT_CLASS_OVERRIDES")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_COA_ISIR_BDGT_DIFF")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_NO_BUDGET_ATTEND")  :
        return (query, renamed, directory, move_directory)

    if (("BR_PELL_COA_CHECK" in query) ) :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_PELL_COA_DOUBLE")  :
        return (query, renamed, directory, move_directory)

    if "BR_PELL_COA_DBLD_WRNG" in query  :
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_BR_PELL_COA_LESS_HT_20")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_PROC_STAT_RVW_STAT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_RES_NON_RES_BDGT")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_SCH_TUITION_FEES_NR")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_SCH_TUITION_ONLY_NR")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_SCHOLAR_TUIT_FEES")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BR_SCHOLAR_TUIT_ONLY")  :
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_BR_UFORM_CHANGE_BUD_DUR")  :
        return (query, renamed, directory, move_directory)

    if "BR_ACAD_LVLS_NOT_SYNC" in query  :
        return (query, renamed, directory, move_directory)

    if "UUFA_BR_COA_ONLINE" in query:
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_BR_MANUAL_BDGT_NO_FEE")  :
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_USA_HRE_HOUSING")  :
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_HOUSING_CIS_UPDT")  :
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_BUDGETED_STDNT_INFO")  :
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line




#Budget Testing Queries
def do_budget_test_queries(test, date, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Budgets', aid_year, month_folder,"Wrong Budget Queries"))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder, "Wrong Budget Queries"))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]

    move_directory = "Budget Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'
    
    if query.startswith("UUFA_BUDGET_20" + year + "_DN1"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_DN2"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_DN3"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_DN4"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_ACCTMAC"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_ARCHMAR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_BUSINESS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_COMDIS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_EAEMS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_EDUCATION"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_ED_PSYCH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_ENGINERING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_FINE_ARTS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENERAL_GR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENETICS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_HEALTH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PRO_HEALTH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_HUMANITIES"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_MBA_BUADMB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_MD_SCIENCE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_MEDICAL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_NURSING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PA"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PHARMACY"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PLANNING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PMBAMBA"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLICPOLI"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLIC_ADM"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_SCIENCE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_SOC_BEHAV"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_SW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_GR_XMBAMBA"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_LW1"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_LW2"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_LW3"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_MD1"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_MD2"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_MD3"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_MD4"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UNDERGRAD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUSINESS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUS_LTHT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENGINERING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENG_LTHT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_LTHT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSE_LTHT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSING"):
        return (query, renamed, directory, move_directory)
                
    return "Empty" #Leave as last line