import pandas as pd

# Data provided by the user
data = {
    "PostID":[6]*44,
    "Username": ["christianfrgsn93", "vanessamoore906gmail.com6330", "joycelovinglife", 
                 "valerie.buck", "wylmacarstafhnur", "ttimmons1", "lady_reneesings", 
                 "jossie13269", "sugaluvme", "royalpainsceo", "mjn1633", 
                 "crucified.stageplay", "incrediblerootsllc", "rebelliouz_1", 
                 "sundaylove11.59", "tacora02", "myzkita", "tiffanyschicproperties", 
                 "crystalkeepitrealatalltime", "nieceyboone", "sweetjewelrysensations", 
                 "freeda_jacksun", "rubygirl_62", "barbsbrowstudio", "shywachira", 
                 "eartha.jackson.98", "sisters1.1", "tomi_adefila", "baker6nan", 
                 "hunny63_", "iluv2sing2u", "vencilsdaughter", "electladyc", "getyou36", 
                 "the_only_nicci", "fifthbarnett", "jdunning15", "hallanntonia", 
                 "halo4680", "allfitnesflyco", "cheryl.boone.758", "nodancerleft_behindinc", 
                 "juliasspaces", "maryloveinc"],
    "Comment": [
        "I want this", "Happy Anniversary to you both 🍾🎁🎈💐🎊🎂❤️", "Look at God! Beautiful couple",
        "❤️👏Happy Anniversary", "Congratulations ❤️❤️❤️", "Come through GQ yall did that.",
        "Happy Anniversary 😍😍😍😍", "Happy Anniversary", "🙌🙌😍😍", "Yassssss 🥰🥰",
        "Tab look like she was bad as hell 😂😂 congratulations, love y'all's work!", "💪🏾",
        "Beautiful", "❤️❤️❤️❤️❤️", "❤️❤️❤️🔥", "Happy Father's Day", "❤️", 
        "Happy Anniversary", "I love yall", "Congratulations beautiful couple ❤️🔥", 
        "Y'all look good❤️❤️❤️🔥🔥🔥", "20 year's and still together and in Love Powerful love.",
        "Congratulations 🔥🔥", "Congratulations", "You guys are beautiful!! Congratulations I got y’all by 1 year!!", 
        "Happy Anniversary Again ❤️", "Ok beauty", "Beautiful ❤️", "Congratulations!!!",
        "🖤💪🏽✊🏽🖤", "Happy Anniversary 😊 🥂", "Happy anniversary 👏👏", "Happy Anniversary ❤️",
        "Y’all look good ❤️ ❤️", "I love it. Congratulations to you both. It warms my heart to see beautiful love. The type of love where I can feel the growth. Because I know from my own marriage you have to meet the other where they are at times. ❤️",
        "Congratulations 🎊", "Nice couple", "Beautiful couple❤️…. Congratulations 🎊", "Congratulations ❤️",
        "Blessings ❤️❤️", "Happy Anniversary", "❤️❤️❤️", "❤️🙌🏾", "HAPPY ANNIVERSARY"
    ],
    "Sentiment": ["Neutral", "Positive", "Positive", "Positive", "Positive", "Positive", 
                  "Positive", "Positive", "Positive", "Positive", "Positive", "Neutral", 
                  "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", 
                  "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", 
                  "Positive", "Positive", "Neutral", "Positive", "Positive", "Neutral", 
                  "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", 
                  "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", 
                  "Positive", "Positive"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to CSV content
csv_content = df.to_csv('analysis.csv')

