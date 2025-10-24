import logging

def transform_data(input_data: dict):
    logging.info(f"incoming data: {input_data}")
    # payload = input_data.get(payload, {})
    # transformed = {
    #     "target": "downstream-system",
    #     "mapped": {
    #         "id": payload.get("id"),
    #         "name": payload.get("user_name", "").title(),
    #         "timestamp": payload.get("created_at"),
    #         "meta": {"source": input_data.get("source")}
    #     }
    # }

    transformed = {}
    return transformed