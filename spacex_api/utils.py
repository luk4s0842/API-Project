from googleapiclient.discovery import build

# yt api key: AIzaSyBkHv5f-VM9_HWf6mBo2D77fs_AczKdpw8
DEVELOPER_KEY = 'AIzaSyBkHv5f-VM9_HWf6mBo2D77fs_AczKdpw8'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(search_query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=search_query,
        part="id,snippet",
        maxResults=10
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(str(search_result["id"]["videoId"]))

    print("Videos:\n", "\n".join(videos), "\n")
    return videos
