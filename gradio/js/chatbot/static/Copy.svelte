<script lang="ts">
	import { onDestroy } from "svelte";
	import { Copy, Check } from "@gradio/icons";

	let copied = false;
	export let value: string;
	let timer: NodeJS.Timeout;

	function copy_feedback(): void {
		copied = true;
		if (timer) clearTimeout(timer);
		timer = setTimeout(() => {
			copied = false;
		}, 2000);
	}

	async function handle_copy(): Promise<void> {
		if ("clipboard" in navigator) {
			await navigator.clipboard.writeText(value);
			copy_feedback();
		} else {
			const textArea = document.createElement("textarea");
			textArea.value = value;

			textArea.style.position = "absolute";
			textArea.style.left = "-999999px";

			document.body.prepend(textArea);
			textArea.select();

			try {
				document.execCommand("copy");
				copy_feedback();
			} catch (error) {
				console.error(error);
			} finally {
				textArea.remove();
			}
		}
	}

	onDestroy(() => {
		if (timer) clearTimeout(timer);
	});
</script>

<button on:click={handle_copy} title="copy">
	{#if !copied}
		<span><Copy /> </span>
	{/if}
	{#if copied}
		<span><Check /></span>
	{/if}
</button>

<style>
	button {
		position: relative;
		top: 0;
		right: 0;

		width: 22px;
		height: 22px;

		padding: 5px;

		cursor: pointer;
	}
</style>
