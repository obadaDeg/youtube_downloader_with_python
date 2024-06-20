from enum import Enum


class VideoQualities(Enum):
    FHD_1080P = "1080p"
    HD_720P = "720p"
    SD_480P = "480p"
    LD_360P = "360p"
    LD_240P = "240p"
    LD_144P = "144p"

    @classmethod
    def list(cls):
        return list(map(lambda v: v.value, cls))


class AudioQualities(Enum):
    MP4 = "MP4"
    WEBM = "WEBM"
    THREE_GP = "3GP"
    AAC = "AAC"
    VORBIS = "VORBIS"
    OPUS = "OPUS"
    M4A = "M4A"
    WAV = "WAV"
    FLAC = "FLAC"
    MP3 = "MP3"

    @classmethod
    def list(cls):
        return list(map(lambda a: a.value, cls))
