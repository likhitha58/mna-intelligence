from utils.evidence import generate_evidence_id
from utils.evidence_factory import create_evidence


def test_evidence_id():

    evidence_id = generate_evidence_id()

    print("\nGENERATED EVIDENCE ID")
    print(evidence_id)

    assert evidence_id.startswith("EV-")


def test_create_evidence():

    evidence = create_evidence(
        source_name="Test Source",
        source_type="financial_data",
        content="Revenue information",
        relevance="Used to evaluate financial performance.",
        credibility="high",
    )

    print("\nEVIDENCE OBJECT")
    print(evidence)

    assert evidence.evidence_id.startswith("EV-")
    assert evidence.source_name == "Test Source"
    assert evidence.credibility == "high"


if __name__ == "__main__":
    test_evidence_id()
    test_create_evidence()