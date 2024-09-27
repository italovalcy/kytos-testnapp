"""Main module of italovalcy/testnapp Kytos Network Application.
"""

from kytos.core.rest_api import HTTPException, JSONResponse, Request, get_json_or_400
from kytos.core import KytosNApp, log, rest
from kytos.core import KytosEvent
from kytos.core.helpers import listen_to

class Main(KytosNApp):
    """Main class of italovalcy/testnapp NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        log.info('SETUP testnapp')

    def execute(self):
        """Execute once when the napp is running."""
        log.info('EXECUTE testnapp')

    def shutdown(self):
        """Execute when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        log.info('SHUTDOWN testnapp')

    @rest('/v1/', methods=['GET'])
    def handle_get(self, request: Request) -> JSONResponse:
        """Endpoint to return nothing."""
        log.info('GET /v1/testnapp')
        return JSONResponse({})

    @rest("/v1/", methods=["POST"])
    def handle_post(self, request: Request) -> JSONResponse:
        """Endpoint to return nothing."""
        data = get_json_or_400(request, self.controller.loop)
        if not data:
            raise HTTPException(400, f"Empty request: {data}")
        return JSONResponse("Operation successful", status_code=201)

    @listen_to('.*.switch.(new|reconnected)')
    def handle_new_switch(self, event):
        """Handle the event of a new created switch"""
        log.info(f'handle_new_switch event={event} content={event.content}')

    @listen_to('.*.connection.lost')
    def handle_switch_conn_lost(self, event):
        """Handle the event of switch's connection lost"""
        log.info(f'handle_switch_conn_lost event={event} content={event.content}')
