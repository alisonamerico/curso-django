from pypro.aperitivos.models import Video
from django.shortcuts import render, get_object_or_404


videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='422595352'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='423624747'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
