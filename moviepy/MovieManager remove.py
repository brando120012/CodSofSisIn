from moviepy.editor import VideoFileClip

class MovieManager:

    def get_audio(self, mp4_file, mp3_file):
        try:
            vc = VideoFileClip(mp4_file)
            ac = vc.audio
            ac.write_audiofile(mp3_file)
        finally:
            if 'ac' in locals() and ac:
                ac.close()
            if 'vc' in locals() and vc:
                vc.close()

    def remove_audio(self, mp4_file, output_mp4):
        try:
            video = VideoFileClip(mp4_file)
            video_wa = video.without_audio()
            video_wa.write_videofile(output_mp4, codec='libx264', audio=False)
        finally:
            if 'video_wa' in locals() and video_wa:
                video_wa.close()
            if 'video' in locals() and video:
                video.close()

mm = MovieManager()
mm.get_audio('video.mp4', 'audio.mp3')
mm.remove_audio('video.mp4', 'video_no_audio.mp4')

