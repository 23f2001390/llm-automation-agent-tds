import io
from PIL import Image
from core.config import get_data_dir
from models.task import RunTaskRequest, RunTaskResponse


def execute_task(request: RunTaskRequest) -> RunTaskResponse:
    """Executes a task based on the request."""
    try:
        if request.task.startswith("Get the card number"):
            image_path = get_data_dir() / "credit_card.png"

            # Check if the image file exists
            if not image_path.exists():
                return RunTaskResponse(result=None, error=f"Image file not found: {image_path}")

            try:
                # Open the image using Pillow library
                img = Image.open(image_path)
                # Convert the image to bytes
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                # Placeholder: In a real application, you would send img_byte_arr to your LLM
                #  along with the task description.  For this example, we'll simulate a result.
                #  Replace this with your actual LLM interaction.
                card_number = "1234-5678-9012-3456"  # Simulated result

                return RunTaskResponse(result=card_number, error=None)

            except Exception as e:
                return RunTaskResponse(result=None, error=f"Image processing error: {e}")

        else:
            return RunTaskResponse(result=None, error=f"Unknown task: {request.task}")

    except Exception as e:
        return RunTaskResponse(result=None, error=f"An unexpected error occurred: {e}") 