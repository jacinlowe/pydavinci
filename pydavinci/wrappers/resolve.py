from typing import TYPE_CHECKING, Optional

import pydavinci.utils as utils
from pydavinci.main import resolve_obj

if TYPE_CHECKING:
    from pydavinci.wrappers.mediapool import MediaPool
    from pydavinci.wrappers.mediastorage import MediaStorage
    from pydavinci.wrappers.project import Project
    from pydavinci.wrappers.projectmanager import ProjectManager


class Resolve(object):
    def __init__(self, headless: Optional[bool] = None, path: Optional[str] = None):

        # utils.launch_resolve(headless, path)

        self.pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]
        self._obj = resolve_obj

    @property
    def project_manager(self) -> "ProjectManager":
        from pydavinci.wrappers.projectmanager import ProjectManager

        return ProjectManager()

    @property
    def project(self) -> "Project":
        from pydavinci.wrappers.project import Project

        return Project(resolve_obj.GetProjectManager().GetCurrentProject())

    @property
    def media_storage(self) -> "MediaStorage":
        from pydavinci.wrappers.mediastorage import MediaStorage

        return MediaStorage()

    @property
    def media_pool(self) -> "MediaPool":
        from pydavinci.wrappers.mediapool import MediaPool

        return MediaPool()

    @property
    def fusion(self):
        return resolve_obj.Fusion()

    @property
    def page(self) -> str:
        """Page Attribute

        Returns:
            str: Returns page name
        """
        return self._obj.GetCurrentPage()

    @page.setter
    def page(self, page: str) -> None:
        if page in self.pages:
            self._obj.OpenPage(page)
        else:
            validpages = " ".join(map(str, self.pages))
            raise ValueError(f'"{page}" is not a valid page. Available pages are: {validpages}')

    @property
    def product_name(self) -> str:
        return self._obj.GetProductName()

    @property
    def version(self):
        return self._obj.GetVersionString()

    def load_layout(self, layout_name: str) -> bool:
        return self._obj.LoadLayoutPreset(layout_name)

    def update_layout(self, layout_name: str) -> bool:
        return self._obj.UpdateLayoutPreset(layout_name)

    def save_layout(self, layout_name: str) -> bool:
        return self._obj.SaveLayoutPreset(layout_name)

    def import_layout(self, path: str, layout_name: str) -> bool:

        return self._obj.ImportLayoutPreset(path, layout_name)

    def quit(self):
        return self._obj.Quit()

    @property
    def active_timeline(self):
        from pydavinci.wrappers.timeline import Timeline

        return Timeline(resolve_obj.GetProjectManager().GetCurrentTimeline())

    def __repr__(self) -> str:
        return f'Resolve(Page: "{self.page}")'
