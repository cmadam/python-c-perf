#include "qradar_kestrel.h"

char *transform_json(char *py_json) {
    cJSON *input_json = cJSON_Parse(py_json), *input_event = NULL;
    cJSON *output_json = cJSON_CreateArray();
    char *json_result = NULL;
    cJSON_ArrayForEach(input_event, input_json) {
	cJSON *new_event = cJSON_CreateObject();
	cJSON *name = cJSON_GetObjectItemCaseSensitive(input_event, "name");
	cJSON *greeting = cJSON_GetObjectItemCaseSensitive(input_event,
							   "greeting");
	char text_str[128];
	sprintf(text_str, "%s %s!", name->valuestring, greeting->valuestring);
	cJSON_AddStringToObject(new_event, "text", text_str);
	cJSON_AddItemToArray(output_json, new_event);
    }
    json_result = cJSON_Print(output_json);
 end:
    cJSON_Delete(input_json);
    cJSON_Delete(output_json);
    return json_result;
}
