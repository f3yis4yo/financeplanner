import kivy
from kivy.event import EventDispatcher

class PredictionApp(EventDispatcher):
    """
    This class manages prediction data and dispatches events.
    It uses Kivy's EventDispatcher to allow other components to react to prediction updates.
    """
    __events__ = ('on_predictions',) # Declare the custom event 'on_predictions'.

    def show_predictions(self, predictions=None):
        """
        Dispatches the 'on_predictions' event with prediction data.

        Args:
            predictions (dict, optional): A dictionary containing prediction data.
                                         If None, default static data is used.
                                         Example: {"Food": 220.0, "Rent": 300.0, ...}
        """
        if predictions is None:
            # Default static prediction data if no data is provided.
            predictions = {
                "Food": 220.0,
                "Rent": 300.0,
                "Utilities": 100.0,
                "Entertainment": 50.0,
                "Transportation": 80.0,
                "Other": 30.0
            }
        try:
            # Dispatch the 'on_predictions' event, sending the prediction data.
            self.dispatch('on_predictions', predictions)
        except Exception as e:
            # Handle any exceptions that occur during event dispatch.
            print(f"Error dispatching predictions: {e}")

    def on_predictions(self, predictions):
        """
        This method is called when the 'on_predictions' event is dispatched.

        Args:
            predictions (dict): The prediction data dictionary.

        Note:
            In this class, this method is empty (pass).
            Other components can bind to this event and handle the prediction data.
        """
        pass # Placeholder for future implementation or external handling.