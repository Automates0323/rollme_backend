import random
from django.contrib.auth.models import User
from User_Profile.models import User_Profile
from Functions.RestApi.JSONSerializers import User_ProfileSerializer

def calculate_match_scores(user):
    user_profile = User_Profile.objects.filter(user_id=user).first()
    user_professions = set(user_profile.UserProfession.values_list('title', flat=True))
    user_interests = set(user_profile.IntresetedIn.all())
    user_expectations = set(user_profile.UserExpected.all())

    all_user_profiles = User_Profile.objects.exclude(pk=user_profile.id)
    match_scores = []

    # Use the User_ProfileSerializer to serialize the User_Profile instances
    user_profile_serializer = User_ProfileSerializer(user_profile)

    for other_user_profile in all_user_profiles:
        other_professions = set(other_user_profile.UserProfession.values_list('title', flat=True))
        other_interests = set(other_user_profile.IntresetedIn.all())
        other_expectations = set(other_user_profile.UserExpected.all())

        # Check if all professions, interests, and expectations match exactly
        profession_match = user_professions == other_professions
        interest_match = user_interests.intersection(other_interests)
        expectation_match = user_expectations.intersection(other_expectations)

        # Calculate match score based on your criteria
        match_score = 0

        if profession_match:
            match_score += 1

        # Consider the number of common interests and expectations
        match_score += len(interest_match) + len(expectation_match)

        # Serialize other_user_profile using the serializer
        other_user_profile_data = user_profile_serializer.to_representation(other_user_profile)

        # Remove 'profile_picture' if it has no file associated
        if not other_user_profile.profile_picture:
            other_user_profile_data.pop('profile_picture', None)

        # Convert UserProfession objects to a list of titles
        other_user_profile_data['UserProfession'] = list(other_user_profile.UserProfession.values_list('title', flat=True))
        
        match_scores.append({
            'user_profile': other_user_profile_data,
            'match_score': match_score
        })

    # Shuffle the list randomly
    # random.shuffle(match_scores)

    # Sort the list by match score in descending order
    match_scores.sort(key=lambda x: x['match_score'], reverse=True)

    return match_scores
