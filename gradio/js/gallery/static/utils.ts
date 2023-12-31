import { uploadToHuggingFace } from "@gradio/utils";
import type { FileData } from "@gradio/upload";

export async function format_gallery_for_sharing(
	value: [FileData, string | null][] | null
): Promise<string> {
	if (!value) return "";
	let urls = await Promise.all(
		value.map(async ([image, _]) => {
			if (image === null) return "";
			return await uploadToHuggingFace(image.data, "url");
		})
	);

	return `<div style="display: flex; flex-wrap: wrap; gap: 16px">${urls
		.map((url) => `<img src="${url}" style="height: 400px" />`)
		.join("")}</div>`;
}
