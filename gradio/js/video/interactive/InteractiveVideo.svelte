<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import type { FileData } from "@gradio/upload";
	import { normalise_file } from "@gradio/upload";
	import { Block } from "@gradio/atoms";
	import Video from "./Video.svelte";
	import { UploadText } from "@gradio/atoms";

	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { _ } from "svelte-i18n";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: [FileData, FileData | null] | null = null;
	let old_value: [FileData, FileData | null] | null = null;

	export let label: string;
	export let source: "upload" | "webcam";
	export let root: string;
	export let root_url: null | string;
	export let show_label: boolean;
	export let loading_status: LoadingStatus;
	export let height: number | undefined;
	export let width: number | undefined;
	export let mirror_webcam: boolean;
	export let include_audio: boolean;
	export let container = false;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let autoplay = false;
	export let gradio: Gradio<{
		change: never;
		clear: never;
		play: never;
		pause: never;
		upload: never;
		stop: never;
		end: never;
		start_recording: never;
		stop_recording: never;
	}>;

	let _video: FileData | null = null;
	let _subtitle: FileData | null = null;

	$: {
		if (value != null) {
			_video = normalise_file(value[0], root, root_url);
			_subtitle = normalise_file(value[1], root, root_url);
		} else {
			_video = null;
			_subtitle = null;
		}
	}

	let dragging = false;

	function handle_change({ detail }: CustomEvent<FileData | null>): void {
		if (detail != null) {
			value = [detail, null] as [FileData, FileData | null];
		} else {
			value = null;
		}
	}

	$: {
		if (JSON.stringify(value) !== JSON.stringify(old_value)) {
			old_value = value;
			gradio.dispatch("change");
		}
	}
</script>

<Block
	{visible}
	variant={value === null && source === "upload" ? "dashed" : "solid"}
	border_mode={dragging ? "focus" : "base"}
	padding={false}
	{elem_id}
	{elem_classes}
	{height}
	{width}
	{container}
	{scale}
	{min_width}
	allow_overflow={false}
>
	<StatusTracker {...loading_status} />

	<Video
		value={_video}
		subtitle={_subtitle}
		on:change={handle_change}
		on:drag={({ detail }) => (dragging = detail)}
		on:error={({ detail }) => {
			loading_status = loading_status || {};
			loading_status.status = "error";
			loading_status.message = detail;
		}}
		{label}
		{show_label}
		{source}
		{mirror_webcam}
		{include_audio}
		{autoplay}
		on:clear={() => gradio.dispatch("clear")}
		on:play={() => gradio.dispatch("play")}
		on:pause={() => gradio.dispatch("pause")}
		on:upload={() => gradio.dispatch("upload")}
		on:stop={() => gradio.dispatch("stop")}
		on:end={() => gradio.dispatch("end")}
		on:start_recording={() => gradio.dispatch("start_recording")}
		on:stop_recording={() => gradio.dispatch("stop_recording")}
	>
		<UploadText type="video" />
	</Video>
</Block>
