window.onload = () => {
    document.getElementById('predictForm').reset();
    document.getElementById('resultCard').classList.remove('show');
};

document.getElementById('predictForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = e.target.querySelector('button');
    submitBtn.textContent = 'Analyzing Deep Risk Profile...';
    submitBtn.disabled = true;

    const data = {
        age: parseInt(document.getElementById('age').value),
        employment_years: parseInt(document.getElementById('employment_years').value),
        dependents: parseInt(document.getElementById('dependents').value),
        annual_income: parseFloat(document.getElementById('annual_income').value),
        monthly_expenses: parseFloat(document.getElementById('monthly_expenses').value),
        savings_balance: parseFloat(document.getElementById('savings_balance').value),
        loan_amount: parseFloat(document.getElementById('loan_amount').value),
        loan_purpose: document.getElementById('loan_purpose').value,
        residence_type: document.getElementById('residence_type').value,
        credit_score: parseInt(document.getElementById('credit_score').value),
        total_debt: parseFloat(document.getElementById('total_debt').value),
        active_loans: parseInt(document.getElementById('active_loans').value),
        delayed_payments: parseInt(document.getElementById('delayed_payments').value),
        repayment_history_score: 85 // Mocked for simplicity or could be added to UI
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error('V3 Engine unreachable');

        const result = await response.json();
        
        const resultCard = document.getElementById('resultCard');
        resultCard.className = 'result-card show';
        
        // Dynamic Recommendation colors
        const rec = document.getElementById('recommendation');
        rec.textContent = result.recommendation;
        rec.style.color = result.risk_level === 'Low Risk' ? '#059669' : (result.risk_level === 'High Risk' ? '#dc2626' : '#d97706');

        document.getElementById('riskLevel').textContent = result.risk_level;
        document.getElementById('approvalChance').textContent = result.approval_chance;
        document.getElementById('confidenceScore').textContent = result.confidence_score;
        
        // Ratios
        if (result.financial_ratios) {
            document.getElementById('financialRatiosArea').style.display = 'block';
            document.getElementById('ratioDTI').textContent = result.financial_ratios.DTI;
            document.getElementById('ratioSTD').textContent = result.financial_ratios.Savings_to_Debt;
        }

        // Reasons
        const reasonsList = document.getElementById('riskReasonsList');
        reasonsList.innerHTML = result.risk_reasons.map(r => `<li>${r}</li>`).join('');
        
        // PDF Link
        const pdfBtn = document.getElementById('downloadReport');
        pdfBtn.href = `http://127.0.0.1:8000${result.report_url}`;
        pdfBtn.style.display = 'block';

    } catch (error) {
        console.error('Error:', error);
        alert('Critical Error: ' + error.message);
    } finally {
        submitBtn.textContent = 'Execute Intelligence Engine';
        submitBtn.disabled = false;
    }
});
