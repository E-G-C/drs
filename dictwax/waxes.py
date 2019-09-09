from typing import Any, List


class RepWax:
    """Replacement Wax class"""

    def __init__(self, targets: dict):
        self.targets = targets


class RemWax:
    """Removal Wax class"""

    def __init__(self, targets: list):
        self.targets = targets


class WaxOn:
    def __init__(self, value: Any, wax: [RepWax or RemWax]):
        self.value = value
        self.wax = wax


class DictBodyShop:

    def __init__(self, source):
        self.source = source
        self.dirt = None
        self.replacement = None
        pass

    def wax_off(self):
        # self.dirt = dirt
        self._search_for_wax(self._wax_off, self.source)
        return self.source

    def wipe(self, dirt: List[Any]):
        self.dirt = dirt
        self._search_for_wax(self._wipe_off, self.source)
        return self.source

    def replace(self, replacement):
        self.replacement = replacement
        self._search_for_wax(self._replace, self.source)
        return self.source

    def _search_for_wax(self, action, value):
        if isinstance(value, dict):
            for k in list(value.keys()):
                if isinstance(value[k], dict) or isinstance(value[k], list):
                    self._search_for_wax(action, value[k])
                else:
                    action(k, value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict) or isinstance(item, list):
                    self._search_for_wax(action, item)
                else:
                    action(i, value)

    def _wipe_off(self, k, value):
        if value[k] in self.dirt:
            value.pop(k)

    def _replace(self, k, value):
        if value[k] in self.replacement:
            value[k] = self.replacement[value[k]]

    def _wax_off(self, k, value):
        if isinstance(value[k], WaxOn):
            _wax_item = value[k]
            item_value = _wax_item.value
            value[k] = item_value
            if _wax_item.wax and (item_value in _wax_item.wax.targets):
                if isinstance(_wax_item.wax, RepWax):
                    value[k] = _wax_item.wax.targets[item_value]
                    return
                elif isinstance(_wax_item.wax, RemWax):
                    value.pop(k)
                    return
