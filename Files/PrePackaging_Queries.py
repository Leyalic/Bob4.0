# Pre-Repackaging Queries
import os

def do_pre_repackaging(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Pell Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_PP_RPKG_AGGREGATE_LIMITS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_AWD_AY_NO_BDGT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_AWD_STRM_INACTIVE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_AWRD_LOCK"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_COA_DOUBLE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_LTHT_PELL_COA"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_RPKG_NO_BUDGET"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_RPKG_SNAPSHOT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_PP_RPKG_TOTAL_WDRN_DRP"):
        return (query, renamed, directory, move_directory)
                
    if query.startswith("UUFA_READY_REPACKAGE"):
            return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line