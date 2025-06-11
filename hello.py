import preswald

from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df("personality_dataset_csv")  # Load data


from preswald import query

sql = 'SELECT * FROM personality_dataset_csv WHERE "Drained_after_socializing" = \'Yes\''
filtered_df = query(sql, "personality_dataset_csv")

sql_2 = 'SELECT * FROM personality_dataset_csv WHERE "Drained_after_socializing" = \'No\''
filtered_df_2 = query(sql_2, "personality_dataset_csv")

sql_3 = 'SELECT * FROM personality_dataset_csv WHERE "Personality" = \'Extrovert\''
filtered_df_3 = query(sql_3, "personality_dataset_csv")

sql_4 = 'SELECT * FROM personality_dataset_csv WHERE "Personality" = \'Introvert\''
filtered_df_4 = query(sql_4, "personality_dataset_csv")


from preswald import table, text


text("# Personality Data Analysis App")

text("## Extensive View of the Full Dataset")
text("This table shows the entire dataset loaded from the personality survey.")
table(df, title="Full Data")

text("---")

text("## Drained After Socializing")
text("This table filters the data to show entires of people who are drained after sociailizing.")
table(filtered_df, title="Filtered Data")

text("---")

text("## Not Drained After Socializing")
text("This table filters the data to show entires of people who are not drained after sociailizing.")
table(filtered_df_2, title="Filtered Data_2")

text("---")

text("## Extroverted")
text("This table filters the data to show entires of people who are extroverts.")
table(filtered_df_3, title="Filtered Data_3")

text("---")

text("## Introverted")
text("This table filters the data to show entires of people who are introverts.")
table(filtered_df_3, title="Filtered Data_4")

text("---")

from preswald import plotly
import plotly.express as px

text("## Histogram Plot of those Drained After Socializing based on Personality Type")

fig1 = px.histogram(
    df,
    x="Drained_after_socializing",
    color="Personality",
    barmode="group",
    title="Stage Fear Count by Personality Type",
    template="plotly_white"
)
plotly(fig1)
from preswald import sidebar


sidebar(
    title="Personality Data App",
    text="Explore the relationships between various different survey responses.",
    logo="images/PDA.png"
)