import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# endpoint = "https://testmoataz.cognitiveservices.azure.com/"
# k = "4e6bc33146354464b2d06b8ca6af35a3"

e = "https://topicclass.cognitiveservices.azure.com/"
k = "89569623fa4d40aa82e35dcf221279e4"

text_analytics_client = TextAnalyticsClient(endpoint=e, credential=AzureKeyCredential(k))

print(text_analytics_client)

articles = [
        """
        Washington, D.C. Autumn in DC is a uniquely beautiful season. The leaves fall from the trees
        in a city chock-full of forests, leaving yellow leaves on the ground and a clearer view of the
        blue sky above...
        """,
        """
        Redmond, WA. In the past few days, Microsoft has decided to further postpone the start date of
        its United States workers, due to the pandemic that rages with no end in sight...
        """,
        """
        Redmond, WA. Employees at Microsoft can be excited about the new coffee shop that will open on campus
        once workers no longer have to work remotely...
        """,
        """
        To support our diversity at Staffbase, we nurture a work environment that is cooperative, friendly, and inclusive. We treat one another with dignity and respect– and we reject prejudice, bigotry, intolerance, discrimination, and harassment in all forms. 

At Staffbase we treasure our unique cultures, backgrounds, and experiences. It strengthens our team and helps our customers.

Soon, we’ll be meeting in Frankfurt a.M., Germany, and most of us are meeting for the first time in person. With the help of this code of conduct, we want to ensure that everyone has a great time at Camp.

The foundation of that is that everyone feels safe and respected. Disobeying this code will lead to disciplinary actions and immediate exclusion from Camp.
        """
    ]

result = text_analytics_client.extract_key_phrases(articles)
for idx, doc in enumerate(result):
    if not doc.is_error:
        print("Key phrases in article #{}: {}".format(
            idx + 1,
            ", ".join(doc.key_phrases)
        ))