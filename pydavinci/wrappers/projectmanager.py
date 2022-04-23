from typing import TYPE_CHECKING, Any, Dict, List

# from pydavinci.wrappers._basewrappers import BaseResolveWrapper
from pydavinci.main import resolve_obj
from pydavinci.wrappers.project import Project

if TYPE_CHECKING:
    from pydavinci.wrappers._resolve_stubs import PyRemoteProjectManager
    from pydavinci.wrappers.project import Project

# import fusionscript as dvr_script


class ProjectManager(object):  # type: ignore
    # try:  ## this is for when we do auto-launch
    #     _obj = resolve_obj.GetProjectManager()  # if using this one here, everything fails
    # except AttributeError:
    #     _obj = get_resolve().GetProjectManager()  # if using this here, closing projects fail

    def __init__(self) -> None:

        self._obj: PyRemoteProjectManager = resolve_obj.GetProjectManager()

    def create_project(self, project_name: str) -> "Project":
        """
        Creates a project with ``project_name``

        Args:
            project_name (str): project name

        Returns:
            Project: Project
        """
        created = self._obj.CreateProject(project_name)
        return Project(created)

    def delete_project(self, project_name: str) -> bool:
        return self._obj.DeleteProject(project_name)

    def load_project(self, project_name: str) -> "Project":
        """
        Loads project ``project_name``

        Args:
            project_name (str): project name

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return Project(self._obj.LoadProject(project_name))

    def close_project(self, project: "Project") -> bool:
        return self._obj.CloseProject(project._obj)

    def create_folder(self, folder_name: str) -> bool:
        """
        Creates folder ``folder_name``

        Args:
            folder_name (str): folder name

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.CreateFolder(folder_name)

    def delete_folder(self, folder_name: str) -> bool:
        """
        Deletes folder ``folder_name

        Args:
            folder_name (str): folder name

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.DeleteFolder(folder_name)

    def project_list(self) -> List[str]:
        """
        Returns a list with project names

        Returns:
            List[str]: list of project names
        """
        return self._obj.GetProjectListInCurrentFolder()

    def folder_list(self) -> List[str]:
        """
        Returns a list with folder names

        Returns:
            List[str]: list of folder names
        """
        return self._obj.GetFolderListInCurrentFolder()

    def goto_root_folder(self) -> bool:
        """
        Goes to root project manager folder

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.GotoRootFolder()

    def goto_parent_folder(self) -> bool:
        """
        Goes to parent folder

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.GotoParentFolder()

    @property
    def folder(self) -> str:
        """
        Returns current folder name

        Returns:
            str: folder name
        """
        return self._obj.GetCurrentFolder()

    def open_folder(self, folder_name: str) -> bool:
        """
        Open folder named ``folder_name``

        Args:
            folder_name (str): folder name

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        print("entru open folder")
        return self._obj.OpenFolder(folder_name)

    def import_project(self, path: str) -> bool:
        """
        Imports ``.drp`` project located at ``path``

        Args:
            path (str): path to ``.drp`` project

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.ImportProject(path)

    def export_project(self, project_name: str, path: str, stills_and_luts: bool = True) -> bool:
        """
        Exports project

        Args:
            project_name (str): project to be exported
            path (str): path to export to
            stills_and_luts (bool, optional): whether to export with Stills and LUTs. Defaults to False.

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.ExportProject(project_name, path, stills_and_luts)

    def restore_project(self, path: str) -> bool:
        """
        Restore project from ``path``

        Args:
            path (str): project path

        Returns:
            bool: ``True`` if successful, ``False`` otherwise
        """
        return self._obj.RestoreProject(path)

    @property
    def db(self) -> Dict[Any, Any]:
        return self._obj.GetCurrentDatabase()

    @db.setter
    def db(self, db_info: Dict[Any, Any]) -> bool:
        """
        Sets current database according to ``db_info``

         Args:
             db_info (dict): valid ``db_info`` dict.

         Info:
             Valid dictionary:
             ```python
             ProjectManager.db = {
             'DbType': 'Disk',
             'DbName': 'Local Database'
             }
             ```
             For PostgresSQL:
             ```python
             ProjectManager.db = {
             'DbType': 'PostgreSQL',
             'DbName': 'PosgresDB',
             'IpAddress': '127.0.0.1'
             }
             ```

        Returns:
             bool: ``True`` if successful, ``False`` otherwise

        """
        return self._obj.SetCurrentDatabase(db_info)

    @property
    def db_list(self) -> List[Dict[Any, Any]]:
        """
        Returns list of all databases

        Returns:
            list of databases
        """
        return self._obj.GetDatabaseList()