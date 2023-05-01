from export_channel import export_channel, mm, own_id
import os
import json

if not os.path.exists('../downloaded/channels.json'):
    import export_channel_list
    # No need to do anything else, we have created the file now

channels = json.load(open('../downloaded/channels.json', 'r'))
teams = json.load(open('../downloaded/teams.json', 'r'))

def team_by_id(team_id):
    for team in teams:
        if team['id'] == team_id:
            return team

for channel in channels:
    print('Downloading channel', channel['display_name'], 'in', team_by_id(channel['team_id'])['display_name'])

    # Hardcoded behavior for my use-case. TODO: generalize to a list of blocked channels or keywords
    if 'High Volume' in channel['display_name']:
        print('   skipping')
        continue

    # Join if necessary
    mm.add_user_to_channel(channel['id'], own_id)

    # Download channel
    export_channel(channel['id'])

