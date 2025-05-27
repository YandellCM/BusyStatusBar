import reflex as rx

def index():
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.link("Home", href="#", class_name="text-gray-700 hover:text-black transition-colors"),
                    rx.link("Shop", href="#", class_name="text-gray-700 hover:text-black transition-colors"),
                    rx.link("Downloads", href="#", class_name="text-gray-700 hover:text-black transition-colors"),
                    rx.link("Blog", href="#", class_name="text-gray-700 hover:text-black transition-colors"),
                    class_name="space-x-6"
                ),
                rx.spacer(),
                rx.link("Cloud Access", href="#", class_name="text-gray-700 hover:text-black transition-colors"),
                class_name="flex justify-between items-center py-6 px-8"
            ),

            rx.flex(
                rx.image(
                    src=rx.asset("imgPrincipal.jpg"),
                    alt="Busy Status Bar",
                    class_name="w-full h-auto rounded-2xl shadow-md object-cover",
                    style={
                        "position":"relative",
                    }
                ),
                rx.box(
                    rx.text(
                        "Busy Status Bar",
                        class_name="font-bold text-3xl text-gray-900 text-center mt-7"
                    ),
                    rx.text(
                        "is a productivity multi-tool device with an LED pixel screen. Displays a personal busy message. Built-in Pomodoro timer and Apps. Fully customizable, open-source, and hacker-friendly.",
                        class_name="text-gray-600 max-w-2xl mx-auto",

                    ),
                    rx.button(
                        "BUY",
                        class_name="mt-4 bg-orange-500 text-white px-6 py-2 rounded-full shadow hover:bg-orange-600 transition mx-auto",
                        size="4",
                        style={
                            "margin-bottom": "10dvh"
                        }
                    ),
                    class_name="flex flex-col items-center",
                    style={
                        "position":"absolute",
                        "top":"70dvh",
                    }
                ),
                class_name="space-y-4 mb-16",
                text_align="center",
                direction="column",
                align="center",
                justify="center",
            ),

            rx.box(
                rx.hstack(
                    rx.box(
                        rx.text(
                            "Live Busy status",
                            class_name="font-bold text-3xl text-gray-900 mb-4"
                        ),
                        rx.text(
                            "Busy Status Bar can integrate with desktop software and automatically activate when you're on a call, live on stream, recording audio or when a certain program is active.",
                            class_name="text-gray-600 max-w-md mb-4 text-justify"
                        ),
                        rx.box(
                            rx.text("🔊 Automatic 'On Call' status", class_name="text-gray-600"),
                            rx.text("🎥 Streaming mode", class_name="text-gray-600"),
                            rx.text("💻 Multi-platform support", class_name="text-gray-600"),
                            class_name="space-y-1 mt-2"
                        ),
                        class_name="flex-1 p-4"
                    ),
                    rx.image(
                        src=rx.asset("imgsec2.jpg"),
                        alt="Live Busy Status",
                        class_name="rounded-2xl shadow-md object-cover",
                        style={
                            "width": "550px",
                            "height": "auto",
                            "borderRadius": "1rem"
                        }
                    ),
                    class_name="flex flex-col md:flex-row items-center gap-6 mb-16",
                    margin_y="20dvh",
                ),
            ),

            rx.box(
                rx.image(
                    src=rx.asset("imgsec3.jpeg"),
                    alt="Monochrome back screen",
                    class_name="mx-auto rounded-2xl shadow-md w-full max-w-4xl",
                    style={
                        "position": "relative",
                    }
                ),
                rx.box(
                    rx.text(
                        "Monochrome back screen",
                        class_name="font-bold text-3xl text-gray-900 text-center mt-4"
                    ),
                    rx.text(
                        "Eye-friendly back screen allows to control the device and see the status displayed on the main screen — even when it’s turned away from you.",
                        class_name="text-gray-600 max-w-3xl text-center mx-auto mt-2"
                    ),
                    style={
                        "position": "absolute",
                        "bottom": "90dvh",
                    }
                ),
                class_name="space-y-2 mb-16"
            ),

            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src=rx.asset("logoFooter.png"),
                            alt="Flipper Devices",
                            class_name="h-12"
                        ),
                        rx.spacer(),
                        rx.hstack(
                            rx.link("Shop", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            rx.link("Downloads", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            rx.link("Blog", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            rx.link("About Us", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            rx.link("Contacts", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            rx.link("Privacy Policy", href="#", class_name="text-sm text-gray-400 hover:text-white transition"),
                            class_name="space-x-6"
                        ),
                        class_name="w-full items-center"
                    ),
                    rx.hstack(
                        rx.text(
                            "2630 Philadelphia Pike, Suite B #508, Claymont, DE 19703, USA",
                            class_name="text-xs text-gray-400"
                        ),
                        rx.spacer(),
                        rx.text(
                            "D-U-N-S Number: 117565668",
                            class_name="text-xs text-gray-400"
                        ),
                        class_name="w-full items-center"
                    ),
                    class_name="bg-black w-full py-10 px-8 mt-10 space-y-4 rounded-t-2xl"
                ),
                class_name="w-full"
            ),

            class_name="space-y-12 bg-white p-8"
        ),
        class_name="bg-white"
    )

app = rx.App()
app.add_page(index)
