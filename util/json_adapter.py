# https://qiita.com/Thiru0000/items/35554f523565e4b12b51

import json


class JsonAdapter(object):

    def serialize(self, json_data):
        """
        JSONからシリアライズする。
        jsonから一旦Dictionaryを作成し変数名をkeyとして値を取る。
        またクラスの場合はクラスを生成して再度シリアライズする。
        :param json_data:
        :return:
        """
        _json = json_data
        if isinstance(json_data, str):
            _json = json.loads(json_data)

        for key in self.__dict__.keys():
            if isinstance(getattr(self, key), JsonAdapter) or getattr(self, key) is None:
                _val_class = getattr(self, key)
                _val_class.serialize(_json[key])
                setattr(self, key, _val_class)
            elif isinstance(getattr(self, key), float):
                setattr(self, key, float(_json[key]))
            elif isinstance(getattr(self, key), int):
                setattr(self, key, int(_json[key]))
            else:
                setattr(self, key, _json[key])

    def to_json(self):
        """
        JSONで出力する。
        逆に変数名をkeyとしたDictionaryを作成しJson化する。
        :return:
        """
        _dict = self.__to_dict()
        _json_str = json.dumps(_dict, ensure_ascii=False)
        return _json_str

    def __to_dict(self):
        """
        mapを作成する。
        :return:
        """
        _dict = {}
        for key in self.__dict__.keys():
            if isinstance(getattr(self, key), JsonAdapter):
                _dict.update({key: getattr(self, key).__to_dict()})
            else:
                _dict.update({key: getattr(self, key)})
        return _dict
