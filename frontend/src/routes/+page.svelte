<script>
    import axios from "axios";
    import { onMount } from "svelte";

    let currencies = [];
    let fromcurrency = "";
    let tocurrency = "";
    let amount = 0;
    let converted_amount = null;

    const apiBaseUrl = "http://127.0.0.1:8000";

    async function fetch_currency() {
        try{
            const res = await axios.get(`${apiBaseUrl}/currencies`);
            currencies = res.data.currencies;
        }catch (error){
            alert("failed to fetch currencie: " + error.message);
        }
    }

    async function convertCurrency() {
        if(!fromcurrency || !tocurrency || amount <= 0){
            alert("please fill all the fields with valid values.");
            return;
        }
        try{
            const response = await axios.post(`${apiBaseUrl}/convert`,{
                from_currency: fromcurrency,
                to_currency: tocurrency,
                amount: parseFloat(amount),
            });
            converted_amount = response.data.converted_amount;
        }catch (error){
            alert("conversion failed: " + error.response?.data?.detail || error.message)
        }
    }

    onMount(fetch_currency)


</script>
<div class="hero bg-base-200 min-h-screen">
    <div class="hero-content text-center">
        <div class="max-w-md">
            <h1 class="text-5xl font-bold mb-6">Currency Converter</h1>
            <select bind:value={fromcurrency} class="select select-bordered mb-6">
                <option value="" disabled selected>Select From Currency</option>
                {#each currencies as currency }
                    <option value={currency}>{currency}</option>
                {/each}
            </select>
            <select bind:value={tocurrency} class="select select-bordered mb-6">
                <option value="" disabled selected>Select To Currency</option>
                {#each currencies as currency }
                    <option value={currency}>{currency}</option>
                {/each}
            </select>
        
            <input 
            type="number"
            min="0"
            bind:value={amount}
            placeholder="Enter amount"
            class="input input-bordered mb-6"
            />
        
            <button on:click={convertCurrency} class="btn btn-primary" >Convert</button>
        
            {#if converted_amount !== null}
                <p class="py-6">Converted Amount: {converted_amount}</p>
            {/if}
        </div>
        
    </div>

</div>
