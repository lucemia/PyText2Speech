from text_to_speech.exceptions import LanguageNotSupportError, VoiceNotSupportError


class Speech(object):
    def __init__(self, name, password, file_name=None):
        self.__file_name = file_name if file_name else 'out'

    def make_file(self, **kwargs):

        lang = kwargs.get('lang', '')
        voice = kwargs.get('voice', '')

        self._validate_language(lang)
        self._validate_voices(voice, lang)

        binary, ext = self.speech(**kwargs)

        file_path = self.__file_name + '.' + ext
        with open( file_path, 'wb') as fp:
            fp.write(binary)
        return file_path

    def _validate_language(self, lang):

        if lang not in self.languages():
            raise LanguageNotSupportError("{} is not support".format(lang))

    def _validate_voices(self, voice, lang):

        if not voice:
            return

        if voice not in self.voices(lang):
            raise ("Voice {} is not support".format(voice))

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        :param narration:
        :param lang:
        :param voice:
        :param kwargs:
        :return binary and type:
        """
        pass

    def voices(self, lang):
        return []

    def languages(self):
        return []

