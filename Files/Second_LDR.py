# 2nd LDR Queries 
import os

def do_2nd_ldr(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Term', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Term', aid_year))

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

    if query.startswith("UUFA_CBA_UNDISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_HRS_DECREASE_ATH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_HRS_DECREASE_FC"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_HRS_DECREASE_SV"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_DL_MATH990"):
        return (query, renamed, directory, move_directory)

    if "PELL_DL_MATH980" in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
        return (query, renamed, directory, move_directory)
                
    return "Empty" #Leave as last line
