import gradio as gr  # Create web-based user interfaces
from utils import mask_pii  # Handles detection and masking of PII in the email text
from models import predict_category  # Function classifies the email text into a category

# Function logic that Gradio can use
def classify_email(email_text):
    # Calls the mask_pii function on the input text to get masked_email and entities
    masked_email, entities = mask_pii(email_text)
    # Classifies the masked email using the model
    category = predict_category(masked_email)
    # Returns all the relevant results in a dictionary (Gradio will format this as JSON)
    return {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

# Create the Gradio UI
iface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(
        lines=12,
        placeholder="Paste support email here...",
        label="Support Email",
        info="Please make sure names start with a capital letter and use your first name Example:- Mr. Jhon ,Sai"
    ),
    outputs="json",
    title="Email Classifier for Support Team",
    description="This app masks PII and classifies support emails into categories like Billing, Tech Support, etc."
)

# Launch the App
if __name__ == "__main__":
    iface.launch()
