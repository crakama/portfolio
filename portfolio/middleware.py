from mainapp.models import Main


class ReferMiddleWare():

    def process_request(self, request):
        ref_id = request.GET.get("ref")
        try:
            obj = Main.objects.get(ref_id=ref_id)
        except:
            obj = None

        if obj:
            request.session["ref"] = obj.id
