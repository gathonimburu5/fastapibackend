from sqlalchemy.orm import Session
from application.models.journal_model import JournalHeader, JournalDetails
from application.schemas.journal_schema import JournalHeaderCreate
from application.models.trail_model import AuditTrail

class JournalService:
    def createJournalRecord(self, journal: JournalHeaderCreate, db: Session, current_user):
        try:
            user_id = current_user.id
            new_header = JournalHeader(
                journal_description = journal.journal_description,
                journal_date = journal.journal_date,
                transaction_period = journal.transaction_period,
                transaction_year = journal.transaction_year,
                transaction_form = journal.transaction_form,
                sale_reference = journal.sale_reference,
                purchase_reference = journal.purchase_reference,
                credit_reference = journal.credit_reference,
                created_by = user_id
            )
            db.add(new_header)
            db.flush()

            #adding journal details
            for detail in journal.details:
                new_detail = JournalDetails(
                    journal_id = new_header.id,
                    account_id = detail.account_id,
                    dr_amount = detail.dr_amount,
                    cr_amount = detail.cr_amount,
                    total_amount = detail.total_amount,
                    narrations = detail.narrations,
                    folio_number = detail.folio_number
                )
                db.add(new_detail)

            #create audit trail
            create_trail = AuditTrail(
                module_id = new_header.id,
                module_name = "createJournalRecord",
                action_taken = "CREATING JOURNAL RECORD",
                user_id = user_id
            )
            db.add(create_trail)

            db.commit()
            db.refresh(new_header)
            return new_header

        except Exception as e:
            db.rollback()
            return f"an error occurred: {str(e)}"