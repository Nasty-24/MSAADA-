import json


def build_citizen_response(
    service: dict,
    validation: dict
) -> str:
    """
    Build the final MSAADA citizen-facing response.

    This function does NOT use an LLM.
    It only presents information that exists in the
    MSAADA knowledge base and has passed validation.
    """

    if not service:
        return (
            "MSAADA could not identify the government service.\n\n"
            "Please describe the service you need."
        )

    service_name = service.get(
        "name",
        "Unknown service"
    )

    agency = service.get(
        "agency",
        "Unknown government agency"
    )

    validation_status = validation.get(
        "validation_status",
        "INCOMPLETE"
    )

    official_url = service.get("official_url")

    # --------------------------------------------------
    # VERIFIED
    # --------------------------------------------------

    if validation_status == "VERIFIED":

        requirements = service.get(
            "requirements",
            []
        )

        steps = service.get(
            "steps",
            []
        )

        fees = service.get(
            "fees"
        )

        response = [
            "🇰🇪 MSAADA",
            "",
            f"### {service_name}",
            "",
            f"**Agency:** {agency}",
            "",
            "✅ **Status: VERIFIED**",
            "",
            "### What you need",
        ]

        if requirements:
            for requirement in requirements:
                response.append(
                    f"- {requirement}"
                )
        else:
            response.append(
                "- No verified requirements available."
            )

        response.extend([
            "",
            "### How to apply"
        ])

        if steps:
            for index, step in enumerate(
                steps,
                start=1
            ):
                response.append(
                    f"{index}. {step}"
                )
        else:
            response.append(
                "- No verified application steps available."
            )

        if fees:

            response.extend([
                "",
                "### Fees"
            ])

            if isinstance(fees, dict):

                for name, amount in fees.items():
                    response.append(
                        f"- {name.replace('_', ' ').title()}: {amount}"
                    )

            else:
                response.append(
                    str(fees)
                )

        response.extend([
            "",
            "### Next step"
        ])

        if official_url:
            response.append(
                f"Visit the official government source: {official_url}"
            )
        else:
            response.append(
                "Contact the responsible government agency "
                "to confirm the next step."
            )

        response.extend([
            "",
            "MSAADA only presents information that has "
            "passed its verification checks."
        ])

        return "\n".join(response)

    # --------------------------------------------------
    # UNVERIFIED
    # --------------------------------------------------

    if validation_status == "UNVERIFIED":

        return (
            "🇰🇪 MSAADA\n\n"
            f"### {service_name}\n\n"
            f"**Agency:** {agency}\n\n"
            "⚠️ **Status: UNVERIFIED**\n\n"
            "MSAADA found this service, but the available "
            "information has not been verified.\n\n"
            "To prevent you from acting on inaccurate "
            "government information, MSAADA will not "
            "present the requirements, fees or procedures "
            "as confirmed facts.\n\n"
            "Please verify the information through the "
            "responsible government agency."
        )

    # --------------------------------------------------
    # INCOMPLETE
    # --------------------------------------------------

    if validation_status == "INCOMPLETE":

        return (
            "🇰🇪 MSAADA\n\n"
            f"### {service_name}\n\n"
            f"**Agency:** {agency}\n\n"
            "⚠️ **Status: INFORMATION INCOMPLETE**\n\n"
            "MSAADA found this service, but important "
            "information is missing from the verified "
            "knowledge base.\n\n"
            "Please verify the missing information through "
            "the responsible government agency before "
            "proceeding."
        )

    # --------------------------------------------------
    # NOT FOUND
    # --------------------------------------------------

    return (
        "🇰🇪 MSAADA\n\n"
        "I could not verify the government service you "
        "are looking for in the MSAADA knowledge base.\n\n"
        "Please describe the service in more detail."
    )