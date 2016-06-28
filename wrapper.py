import os
from pelican import signals
from pelican.readers import RstReader


class RstReaderWrapper(RstReader):
    enabled = RstReader.enabled
    file_extensions = ['rst']

    class FileInput(RstReader.FileInput):
        def __init__(self, *args, **kwargs):
            RstReader.FileInput_.__init__(self, *args, **kwargs)
            self.source = RstReaderWrapper.SourceWrapper(self.source)

    # Hook into RstReader
    RstReader.FileInput_ = RstReader.FileInput
    RstReader.FileInput = FileInput

    class SourceWrapper():
        """
            Mimics and wraps the result of a call to `open`
        """
        content_to_prepend = None

        def __init__(self, source):
            self.source = source

        def read(self):
            content = self.source.read()
            if self.content_to_prepend is not None:
                content = "{}\n{}".format(self.content_to_prepend, content)
            return content

        def close(self):
            self.source.close()


def process_settings(pelicanobj):
    include_files = pelicanobj.settings.get('RST_GLOBAL_INCLUDES', []) or []
    base_path = pelicanobj.settings.get('PATH', ".")

    def read(fn):
        with open(os.path.join(base_path, fn), 'r') as res:
            content = res.read()
            return ".. INLCUSION FROM {}\n{}\n".format(fn, content)

    inclusion = "".join(map(read, include_files)) if include_files else None
    RstReaderWrapper.SourceWrapper.content_to_prepend = inclusion


def register():
    signals.initialized.connect(process_settings)
