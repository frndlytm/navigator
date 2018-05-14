import logging

from manager import Manager
from source import SourceFactory
from paginator import DefaultPaginator

class Main:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.config.name)

        self.manager = Manager()
        self.manager.docs = self.config.docs
        self.manager.session = self.config.session
        self.manager.factory = SourceFactory(
            self.config.name, self.config.host, self.config.port
        )
        self.manager.setup()


    def __call__(self):
        for src in self.manager.sources:
            print(src)


if __name__ == '__main__':
    from settings import config
    main = Main(config)
    main()
