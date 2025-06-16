import random

def get_random_template():
    """Returns a randomly selected Arabic sentence template."""
    templates = [
        "تُعَدّ [K1] من المواضيع المهمة في مجال [K2]، لما لها من تأثير على [K3].",
        "يُعتبر موضوع [K1] من أبرز القضايا المتعلقة بـ [K2]، حيث يؤثر بشكل كبير على [K3].",
        "يتناول البحث موضوع [K1] وأهميته في سياق [K2] وتأثيره على [K3]."
    ]
    return random.choice(templates)

def construct_prompt(keywords):
    """
    Constructs an Arabic prompt by inserting keywords into a randomly selected template.
    Keywords should be a list of 3 strings.
    """
    if len(keywords) != 3:
        raise ValueError("Exactly 3 keywords are required.")

    template = get_random_template()
    prompt = template.replace("[K1]", keywords[0])
    prompt = prompt.replace("[K2]", keywords[1])
    prompt = prompt.replace("[K3]", keywords[2])
    return prompt 