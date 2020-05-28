from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 422595352},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 423624747},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
