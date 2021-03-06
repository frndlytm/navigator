import logging
from pathlib import Path

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
        self.manager.paginator = DefaultPaginator
        self.manager.factory = SourceFactory(
            self.config.name, self.config.host, self.config.port
        )
        self.manager.setup()


    def __call__(self):
        rules = Path(self.config.path).joinpath('rules')
        valids = [item.stem for item in rules.iterdir()]
        srcs = filter(lambda src: src.endpoint in valids, self.manager.sources)
        for src in srcs: print(src+str(self.manager.paginator))


if __name__ == '__main__':
    from settings import config
    main = Main(config)
    main()
