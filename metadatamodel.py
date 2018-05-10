"""
@author: cdimare@granitenet.com
@name: navigator.taggers

@description:
    An object that combines metadata to export a file to HDFS.
"""
import json

class MetadataModelFactory:
    def makeMetadataModel(self, file=None):
        if file:
            try:
                data = json.load(file)
            except ValueError:
                return ValueError

            return MetadataModel(data['name'], data['description'], data['properties'], data['tags'], file)

        else:
            return MetadataModel('', '', dict(), [], None)



class MetadataModel:
    def __init__(self, name, description, properties, tags, file):
        self._name = name
        self._description = description
        self._properties = properties
        self._tags = tags
        self._file = file

    def __repr__(self):
        return json.dumps(
            dict(
                name = self.name,
                description=self.description,
                properties=self.properties,
                tags = self.tags
            )
        )


    #
    # file is the import/export location for the Tagger object.
    #
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, name):
        self._file = '.{}.txt.navigator'.format(name)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        self.file = name


    #
    # description is imported from the file if accessbile, else it
    # is set manually.
    #
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, desc):
        self._description = desc


    #
    # properties for the HDFS file.
    #
    @property
    def properties(self):
        return self._properties
    @properties.setter
    def properties(self, props):
        self._properties = props

    def add_property(self, key, value):
        self._properties[key] = value


    #
    # tags are custom metadata to improve search.
    #
    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags

    def add_tag(self, tag):
        self._tags.append(tag)





if __name__ == '__main__':
    factory = MetadataModelFactory()
    model = factory.makeMetadataModel()
    print(model)
    model.name = 'helloworld'
    print(model, model.file)