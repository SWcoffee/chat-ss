import json

common_model = """
{
	"models": [{
		"capabilities": {},
		"description": "我们最快的模型，非常适合大多数日常任务。",
		"max_tokens": 8191,
		"product_features": {},
		"slug": "text-davinci-002-render-sha",
		"tags": ["gpt3.5"],
		"title": "Default (GPT-3.5)"
	}, {
		"capabilities": {},
		"description": "最新、最高级的模型",
		"enabled_tools": ["tools", "tools2"],
		"max_tokens": 8192,
		"product_features": {
			"attachments": {
				"accepted_mime_types": ["text/xml", "text/x-sh", "text/x-rst", "text/x-java", "text/x-python", "text/calendar", "text/x-shellscript", "message/rfc822", "text/x-csharp", "application/msword", "application/rtf", "application/x-sql", "application/x-scala", "application/x-powershell", "text/x-vcard", "text/x-c", "application/vnd.oasis.opendocument.text", "text/x-script.python", "application/vnd.apple.pages", "application/json", "text/markdown", "application/x-rust", "text/x-php", "text/x-asm", "application/javascript", "text/x-typescript", "application/pdf", "text/vbscript", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/javascript", "text/x-lisp", "application/x-yaml", "text/rtf", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "text/x-ruby", "text/x-makefile", "text/plain", "text/css", "text/x-tex", "application/vnd.apple.keynote", "text/x-diff", "text/x-c++", "text/html", "application/vnd.ms-powerpoint"],
				"can_accept_all_mime_types": true,
				"image_mime_types": ["image/png", "image/jpeg", "image/gif", "image/webp"],
				"type": "retrieval"
			}
		},
		"slug": "gpt-4o",
		"tags": ["gpt4", "gpt4o"],
		"title": "GPT-4o"
	}, {
		"capabilities": {},
		"description": "使用合适的模型来满足我的请求",
		"enabled_tools": ["tools", "tools2"],
		"max_tokens": 8192,
		"product_features": {
			"attachments": {
				"accepted_mime_types": ["text/xml", "text/x-sh", "text/x-rst", "text/x-java", "text/x-python", "text/calendar", "text/x-shellscript", "message/rfc822", "text/x-csharp", "application/msword", "application/rtf", "application/x-sql", "application/x-scala", "application/x-powershell", "text/x-vcard", "text/x-c", "application/vnd.oasis.opendocument.text", "text/x-script.python", "application/vnd.apple.pages", "application/json", "text/markdown", "application/x-rust", "text/x-php", "text/x-asm", "application/javascript", "text/x-typescript", "application/pdf", "text/vbscript", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/javascript", "text/x-lisp", "application/x-yaml", "text/rtf", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "text/x-ruby", "text/x-makefile", "text/plain", "text/css", "text/x-tex", "application/vnd.apple.keynote", "text/x-diff", "text/x-c++", "text/html", "application/vnd.ms-powerpoint"],
				"can_accept_all_mime_types": true,
				"image_mime_types": ["image/png", "image/jpeg", "image/gif", "image/webp"],
				"type": "retrieval"
			}
		},
		"slug": "auto",
		"tags": ["gpt4", "gpt4o"],
		"title": "Dynamic"
	}]
}
"""

plus_model = """
{
	"models": [{
		"capabilities": {},
		"description": "我们最快的模型，非常适合大多数日常任务。",
		"max_tokens": 8191,
		"product_features": {},
		"slug": "text-davinci-002-render-sha",
		"tags": ["gpt3.5"],
		"title": "Default (GPT-3.5)"
	}, {
		"capabilities": {},
		"description": "浏览、高级数据分析和 DALL·E 现已集成到 GPT-4 中",
		"enabled_tools": ["tools", "tools2"],
		"max_tokens": 32767,
		"product_features": {
			"attachments": {
				"accepted_mime_types": ["application/x-sql", "text/x-lisp", "application/rtf", "application/x-scala", "text/x-ruby", "text/x-c", "application/x-rust", "text/x-vcard", "application/vnd.apple.pages", "text/x-python", "application/vnd.apple.keynote", "text/markdown", "text/x-rst", "text/calendar", "text/x-csharp", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "text/x-java", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/x-makefile", "application/vnd.ms-powerpoint", "text/css", "text/vbscript", "text/html", "text/x-tex", "text/xml", "application/x-yaml", "text/javascript", "text/rtf", "text/x-php", "application/json", "text/x-typescript", "text/x-shellscript", "text/x-asm", "application/pdf", "text/plain", "text/x-sh", "text/x-diff", "text/x-script.python", "message/rfc822", "application/javascript", "application/x-powershell", "text/x-c++", "application/vnd.oasis.opendocument.text"],
				"can_accept_all_mime_types": true,
				"image_mime_types": ["image/jpeg", "image/gif", "image/webp", "image/png"],
				"type": "retrieval"
			}
		},
		"slug": "gpt-4",
		"tags": ["gpt4"],
		"title": "GPT-4 (All Tools)"
	}, {
		"capabilities": {},
		"description": "最新、最高级的模型",
		"enabled_tools": ["tools", "tools2"],
		"max_tokens": 32767,
		"product_features": {
			"attachments": {
				"accepted_mime_types": ["application/x-sql", "text/x-lisp", "application/rtf", "application/x-scala", "text/x-ruby", "text/x-c", "application/x-rust", "text/x-vcard", "application/vnd.apple.pages", "text/x-python", "application/vnd.apple.keynote", "text/markdown", "text/x-rst", "text/calendar", "text/x-csharp", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "text/x-java", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/x-makefile", "application/vnd.ms-powerpoint", "text/css", "text/vbscript", "text/html", "text/x-tex", "text/xml", "application/x-yaml", "text/javascript", "text/rtf", "text/x-php", "application/json", "text/x-typescript", "text/x-shellscript", "text/x-asm", "application/pdf", "text/plain", "text/x-sh", "text/x-diff", "text/x-script.python", "message/rfc822", "application/javascript", "application/x-powershell", "text/x-c++", "application/vnd.oasis.opendocument.text"],
				"can_accept_all_mime_types": true,
				"image_mime_types": ["image/jpeg", "image/gif", "image/webp", "image/png"],
				"type": "retrieval"
			}
		},
		"slug": "gpt-4o",
		"tags": ["gpt4o", "gpt4"],
		"title": "GPT-4o"
	}]
}
"""

user_model = """
{
	"user": {
		"email": "test@hotmail.com",
		"groups": [],
		"iat": 1717081109,
		"id": "user-FQ4OAaH4JNXYnPStCDbAnkDe",
		"idp": "auth0",
		"image": "https://s.gravatar.com/avatar/9e13b3aeff7dd78af8c04e4db49f01be?s=480\u0026r=pg\u0026d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fka.png",
		"intercom_hash": "ad2242fa52fc4fceffc86f413ab1cfbb081e8835644419c7be1e167006b5e6b4",
		"mfa": false,
		"name": "test@hotmail.com",
		"picture": "https://s.gravatar.com/avatar/9e13b3aeff7dd78af8c04e4db49f01be?s=480\u0026r=pg\u0026d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fka.png"
	}
}
"""

if __name__ == '__main__':
    print(json.loads(common_model))
    print(json.loads(plus_model))
    print(json.loads(user_model))
