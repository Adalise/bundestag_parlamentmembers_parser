OUTPUT_FILE = 'output.json'

import json

def main():
    number_deputies = {}
    number_social_media = {}
    number_social_media_per_deputy = {}

    # facebook_propability = {}
    # twitter_propability = {}
    # tiktok_propability = {}
    # instagram_propability = {}
    # linkedin_propability = {}
    # youtube_propability = {}

    with open(OUTPUT_FILE, 'r') as fp:
        deputies = json.load(fp)

    for deputy in deputies:
        party = deputy['party']

        if not party in number_deputies:
            number_deputies[party] = 0
            number_social_media[party] = 0
            number_social_media_per_deputy[party] = 0

            # facebook_propability[party] = 0
            # twitter_propability[party] = 0
            # tiktok_propability[party] = 0
            # instagram_propability[party] = 0
            # linkedin_propability[party] = 0
            # youtube_propability[party] = 0

        number_deputies[party] += 1
        number_social_media[party] += len(deputy['social_media'])
        number_social_media_per_deputy[party] = number_social_media[party] // number_deputies[party]

    print('Number of deputies:',                        number_deputies)
    print('Number of social media links (total):',      number_social_media)
    print('Number of social media links (per deputy):', number_social_media_per_deputy)
    print()
    # print('Probability of Facebook usage:',     facebook_propability)
    # print('Probability of Twitter usage:',      twitter_propability)
    # print('Probability of TikTok usage:',       tiktok_propability)
    # print('Probability of Instagram usage:',    instagram_propability)
    # print('Probability of LinkedIn usage:',     linkedin_propability)
    # print('Probability of YouTube usage:',      youtube_propability)

if __name__ == '__main__':
    main()