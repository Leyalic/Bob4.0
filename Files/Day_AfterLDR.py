# Day After LDR Queries
import os

def do_day_after_ldr(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/LDR', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/LDR', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Financial Aid Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_PELL_TERM_AWARDS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_FC"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_SV"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_LDR_PELL_AWARDS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ATHLETE_AWARD_DISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_CBA_UNDISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_DL_MATH990"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_SUMMER_ENROLLMENT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_THESIS_STUDENTS_NONRES"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_REGISTERED_CENSUS_DATE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_NO_MTRC_STU_ATH_BAL_OWING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_FATERM_SOURCE_N_AWD_ATH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_FATERM_SOURCE_N_AWD_SV"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ATH_NO_MTRC_STU_BAL_OWING"):
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line
