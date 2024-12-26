import json


def serialize_events(events):
    return json.dumps(
        [
            {
                "id": str(event.id),
                "name": event.name,
                "start_date": event.start_date.strftime("%d-%m-%Y"),
                "end_date": event.end_date.strftime("%d-%m-%Y"),
                "description": event.description,
                "location": event.location,
                "type": event.type,
                "is_aerial": event.is_aerial,
                "main_link": event.main_link,
                "additional_url_1": event.additional_url_1,
                "additional_label_1": event.additional_label_1,
                "additional_url_2": event.additional_url_2,
                "additional_label_2": event.additional_label_2,
            }
            for event in events
        ]
    )
